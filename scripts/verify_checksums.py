#!/usr/bin/env python3
"""Verify SHA-256 bytes and complete coverage of a manifest's directory.

The JSON object maps canonical forward-slash paths, relative to the manifest's
directory, to SHA-256 hex digests. Every regular file below that directory must
be listed except the manifest itself. Symlinks and paths outside that directory
are rejected. File bytes are hashed as stored; line endings are not normalized.
Exit codes: 0 verified, 1 integrity/coverage failure, 2 invalid input or I/O error.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import sys


def unique_object(pairs):
    result = {}
    for name, value in pairs:
        if name in result:
            raise ValueError(f"Duplicate manifest entry: {name!r}")
        result[name] = value
    return result


def entry_path(root, name):
    if (not isinstance(name, str) or not name or "\\" in name
            or ":" in name or "\0" in name):
        raise ValueError(f"Invalid manifest path: {name!r}")
    relative = PurePosixPath(name)
    if (relative.is_absolute() or ".." in relative.parts
            or relative.as_posix() != name or name == "."):
        raise ValueError(f"Manifest path must be a canonical relative path: {name!r}")
    candidate = root.joinpath(*relative.parts)
    # Check existing ancestors as well as the leaf, without reading their data.
    if any(path.is_symlink() for path in (candidate, *candidate.parents) if path != root):
        raise ValueError(f"Symlinks are unsupported in manifest paths: {name!r}")
    if not candidate.resolve().is_relative_to(root):
        raise ValueError(f"Manifest path escapes its directory: {name!r}")
    return candidate


def sha256_file(path):
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify(manifest):
    manifest = Path(manifest)
    if manifest.is_symlink():
        raise ValueError("The manifest must not be a symlink")
    manifest = manifest.resolve()
    root = manifest.parent
    entries = json.loads(manifest.read_text(encoding="utf-8-sig"),
                         object_pairs_hook=unique_object)
    if not isinstance(entries, dict) or not entries:
        raise ValueError("Manifest must be a nonempty JSON object")
    paths = {}
    for name, expected in entries.items():
        candidate = entry_path(root, name)
        if candidate == manifest:
            raise ValueError("Manifest must not include itself")
        if not isinstance(expected, str) or not re.fullmatch(r"[0-9a-fA-F]{64}", expected):
            raise ValueError(f"Expected a SHA-256 hex digest for {name!r}")
        paths[name] = candidate

    errors, found = [], set()

    def walk_error(error):
        raise error

    for directory, folders, files in os.walk(root, followlinks=False, onerror=walk_error):
        current = Path(directory)
        for name in list(folders):
            path = current / name
            if path.is_symlink():
                errors.append(f"Unsupported symlink: {path.relative_to(root).as_posix()}")
                folders.remove(name)
            elif not path.resolve().is_relative_to(root):
                # Windows junctions need not report is_symlink() on all Python versions.
                errors.append(f"Directory escapes manifest scope: {path.relative_to(root).as_posix()}")
                folders.remove(name)
        for name in files:
            path = current / name
            if path == manifest:
                continue
            relative = path.relative_to(root).as_posix()
            if path.is_symlink():
                errors.append(f"Unsupported symlink: {relative}")
            elif not path.resolve().is_relative_to(root):
                errors.append(f"File escapes manifest scope: {relative}")
            elif not path.is_file():
                errors.append(f"Not a regular file: {relative}")
            else:
                found.add(relative)
    for name in sorted(found - entries.keys()):
        errors.append(f"Unlisted file: {name}")
    checked = 0
    for name, candidate in paths.items():
        if name not in found:
            errors.append(f"Missing regular file: {name}")
            continue
        actual = sha256_file(candidate)
        checked += 1
        if actual != entries[name].lower():
            errors.append(f"SHA-256 mismatch: {name}; expected {entries[name]}, actual {actual}")
    return {"manifest": str(manifest), "entries": len(entries), "checked_files": checked,
            "errors": errors, "pass": not errors}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args(argv)
    try:
        report = verify(args.manifest)
    except (OSError, ValueError) as exc:
        # Escaped JSON also works on legacy Windows consoles with Unicode paths.
        print(json.dumps({"pass": False, "input_error": str(exc)}, ensure_ascii=True),
              file=sys.stderr)
        return 2
    print(json.dumps(report, ensure_ascii=True, indent=2))
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
