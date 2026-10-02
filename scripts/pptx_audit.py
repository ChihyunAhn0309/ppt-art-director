#!/usr/bin/env python3
"""Read-only, limited PPTX inventory and relationship/timing checks. No rendering."""
import argparse
import json
import posixpath
import re
import sys
import zipfile
from pathlib import Path
from urllib.parse import unquote
from xml.etree import ElementTree as ET

P = "http://schemas.openxmlformats.org/presentationml/2006/main"
A = "http://schemas.openxmlformats.org/drawingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
C = "http://schemas.openxmlformats.org/drawingml/2006/chart"
PR = "http://schemas.openxmlformats.org/package/2006/relationships"
NS = {"p": P, "a": A, "r": R, "c": C}


class NoDoctypeTreeBuilder(ET.TreeBuilder):
    def doctype(self, name, pubid, system):
        raise ValueError("DTD/entity declarations are not accepted")


def parse_xml(data):
    return ET.fromstring(data, parser=ET.XMLParser(target=NoDoctypeTreeBuilder()))


def resolve_target(owner, target):
    target = unquote(target.split("#", 1)[0])
    if target.startswith("/"):
        result = posixpath.normpath(target.lstrip("/"))
    else:
        result = posixpath.normpath(posixpath.join(posixpath.dirname(owner), target))
    if result == ".." or result.startswith("../"):
        raise ValueError(f"Relationship target escapes package: {target}")
    return result


def rel_owner(name):
    if name == "_rels/.rels":
        return ""
    directory, filename = name.rsplit("/", 1)
    if directory == "_rels" and filename.endswith(".rels"):
        return filename[:-5]
    if not directory.endswith("/_rels") or not filename.endswith(".rels"):
        raise ValueError(f"Unexpected relationship part: {name}")
    return directory[:-6] + "/" + filename[:-5]


def audit(path, expected=None):
    errors, warnings, slides = [], [], []
    with zipfile.ZipFile(path) as package:
        infos = package.infolist()
        if len(infos) > 10000 or sum(i.file_size for i in infos) > 512 * 1024 * 1024:
            raise ValueError("Package exceeds inventory limits (10,000 entries / 512 MiB)")
        names = {i.filename for i in infos}
        if len(names) != len(infos):
            errors.append("Duplicate ZIP member names")
        if any(n.startswith("/") or ".." in n.split("/") for n in names):
            errors.append("Unsafe package path")
        for required in ("[Content_Types].xml", "ppt/presentation.xml", "ppt/_rels/presentation.xml.rels"):
            if required not in names:
                raise ValueError(f"Missing required part: {required}")
        relationships = {}
        for name in sorted(n for n in names if n.endswith(".rels")):
            owner = rel_owner(name)
            mapping = {}
            for rel in parse_xml(package.read(name)):
                rid = rel.get("Id")
                if rid in mapping:
                    errors.append(f"Duplicate relationship ID in {name}: {rid}")
                external = rel.get("TargetMode") == "External"
                target = rel.get("Target", "")
                resolved = target if external else resolve_target(owner, target)
                mapping[rid] = {"type": rel.get("Type", ""), "target": resolved, "external": external}
                if not external and resolved not in names:
                    errors.append(f"Missing relationship target: {name} -> {resolved}")
            relationships[owner] = mapping
        pres = parse_xml(package.read("ppt/presentation.xml"))
        size = pres.find("p:sldSz", NS)
        slide_ids = pres.findall("p:sldIdLst/p:sldId", NS)
        if expected is not None and len(slide_ids) != expected:
            errors.append(f"Expected {expected} slides; found {len(slide_ids)}")
        for ordinal, slide_id in enumerate(slide_ids, 1):
            rid = slide_id.get(f"{{{R}}}id")
            rel = relationships["ppt/presentation.xml"].get(rid)
            if not rel or rel["external"] or not rel["type"].endswith("/slide"):
                errors.append(f"Invalid slide relationship at position {ordinal}: {rid}")
                continue
            part = rel["target"]
            if part not in names:
                continue
            root = parse_xml(package.read(part))
            props = root.findall(".//p:cNvPr", NS)
            object_ids = [p.get("id") for p in props]
            if len(object_ids) != len(set(object_ids)):
                errors.append(f"Duplicate object IDs: {part}")
            target_ids = [s.get("spid") for s in root.findall(".//p:timing//p:spTgt", NS)]
            missing = sorted(set(target_ids) - set(object_ids))
            if missing:
                errors.append(f"Unknown animation targets in slide {ordinal}: {missing}")
            timing_ids = [t.get("id") for t in root.findall(".//p:timing//p:cTn", NS)]
            if len(timing_ids) != len(set(timing_ids)):
                errors.append(f"Duplicate timing IDs: {part}")
            text = [t.text or "" for t in root.findall(".//a:t", NS)]
            if any(re.search(r"\b(lorem ipsum|TODO|PLACEHOLDER)\b", t, re.I) for t in text):
                warnings.append(f"Potential placeholder text on slide {ordinal}; inspect manually")
            notes = [v["target"] for v in relationships.get(part, {}).values() if v["type"].endswith("/notesSlide")]
            shapes = []
            for shape in root.findall(".//p:spTree//*", NS):
                if shape.tag.rsplit("}", 1)[-1] not in ("sp", "pic", "graphicFrame", "grpSp", "cxnSp"):
                    continue
                pr = shape.find(".//p:cNvPr", NS)
                if pr is not None:
                    shapes.append({"id": pr.get("id"), "name": pr.get("name"),
                                   "kind": shape.tag.rsplit("}", 1)[-1]})
            transition = root.find("p:transition", NS)
            native_charts = 0
            for chart in root.findall(".//c:chart", NS):
                chart_rid = chart.get(f"{{{R}}}id")
                chart_rel = relationships.get(part, {}).get(chart_rid)
                if (not chart_rel or chart_rel["external"]
                        or not chart_rel["type"].endswith("/chart")
                        or chart_rel["target"] not in names):
                    errors.append(f"Invalid chart relationship on slide {ordinal}: {chart_rid}")
                    continue
                chart_root = parse_xml(package.read(chart_rel["target"]))
                if chart_root.tag != f"{{{C}}}chartSpace":
                    errors.append(f"Invalid chart part on slide {ordinal}: {chart_rel['target']}")
                    continue
                native_charts += 1
            slides.append({"number": ordinal, "part": part, "text": text,
                           "shapes": shapes, "native_charts": native_charts,
                           "native_tables": len(root.findall(".//a:tbl", NS)), "notes_parts": notes,
                           "timing_present": root.find("p:timing", NS) is not None,
                           "animation_target_ids": sorted(set(target_ids)),
                           "transition_elements": [] if transition is None else [e.tag.rsplit("}", 1)[-1] for e in transition]})
    return {"file": str(Path(path).resolve()), "slide_count": len(slide_ids),
            "slide_size_emu": None if size is None else dict(size.attrib),
            "slides": slides, "errors": errors, "warnings": warnings,
            "scope": "Limited relationship/object/timing inventory; not full schema, visual, playback, or factual validation.",
            "pass": not errors}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pptx", type=Path)
    parser.add_argument("--expect-slides", type=int)
    parser.add_argument("--output", type=Path, help="Private JSON report; no deck modification")
    args = parser.parse_args()
    if args.output and (
        args.output.resolve() == args.pptx.resolve()
        or (args.output.exists() and args.output.samefile(args.pptx))
    ):
        raise ValueError("Report path must not refer to the input PPTX")
    result = audit(args.pptx, args.expect_slides)
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
        print(json.dumps({"pass": result["pass"], "slides": result["slide_count"],
                          "errors": result["errors"], "report": str(args.output.resolve())}, ensure_ascii=False))
    else:
        print(rendered)
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, KeyError, zipfile.BadZipFile, ET.ParseError) as exc:
        print(f"PPTX inventory error: {exc}", file=sys.stderr)
        raise SystemExit(2)
