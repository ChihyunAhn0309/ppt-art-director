"""Boundary regressions for bundled helpers; standard library, no Office COM.

Place this file under the package's tests/ directory. All generated fixtures and
outputs live in TemporaryDirectory. PowerShell checks skip if no shell exists.
"""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
P = "http://schemas.openxmlformats.org/presentationml/2006/main"
A = "http://schemas.openxmlformats.org/drawingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PR = "http://schemas.openxmlformats.org/package/2006/relationships"
C = "http://schemas.openxmlformats.org/drawingml/2006/chart"
SHELLS = [p for p in (shutil.which("powershell"), shutil.which("pwsh")) if p]


def make_package(path, *, comment=False, chart=None, root_relationship=False,
                 utf16_dtd=False, grouped=False, timing=False):
    """Small parser fixtures, not a substitute for a full PPTX schema validator."""
    shape = '<p:sp><p:nvSpPr><p:cNvPr id="2" name="target"/></p:nvSpPr><p:txBody><a:p><a:r><a:t>Fixture text</a:t></a:r></a:p></p:txBody></p:sp>'
    if grouped:
        shape = '<p:grpSp><p:nvGrpSpPr><p:cNvPr id="3" name="group"/></p:nvGrpSpPr>' + shape + '</p:grpSp>'
    if chart:
        shape += '<p:graphicFrame><p:nvGraphicFramePr><p:cNvPr id="4" name="chart"/></p:nvGraphicFramePr><a:graphic><a:graphicData><c:chart r:id="chart1"/></a:graphicData></a:graphic></p:graphicFrame>'
    slide = f'<p:sld xmlns:p="{P}" xmlns:a="{A}" xmlns:r="{R}" xmlns:c="{C}"><p:cSld><p:spTree>{shape}</p:spTree></p:cSld>'
    if timing:
        slide += '<p:timing><p:tnLst><p:par><p:cTn id="1"/></p:par></p:tnLst></p:timing>'
    slide += '</p:sld>'
    if utf16_dtd:
        slide = ('<?xml version="1.0" encoding="UTF-16"?><!DOCTYPE x [<!ENTITY e "expanded">]>' + slide.replace('Fixture text', '&e;')).encode('utf-16')
    with zipfile.ZipFile(path, "w") as package:
        package.writestr("[Content_Types].xml", '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/></Types>')
        package.writestr("ppt/presentation.xml", f'<p:presentation xmlns:p="{P}" xmlns:r="{R}"><p:sldIdLst><p:sldId id="256" r:id="slide1"/></p:sldIdLst><p:sldSz cx="12192000" cy="6858000"/></p:presentation>')
        comment_text = '<!-- valid XML comment -->' if comment else ''
        package.writestr("ppt/_rels/presentation.xml.rels", f'<Relationships xmlns="{PR}">{comment_text}<Relationship Id="slide1" Type="{R}/slide" Target="slides/slide1.xml"/></Relationships>')
        package.writestr("ppt/slides/slide1.xml", slide)
        if chart and chart != "missing-relationship":
            relationship_type = f"{R}/chart" if chart != "wrong-type" else f"{R}/image"
            package.writestr("ppt/slides/_rels/slide1.xml.rels", f'<Relationships xmlns="{PR}"><Relationship Id="chart1" Type="{relationship_type}" Target="../charts/chart1.xml"/></Relationships>')
            if chart != "missing-part":
                chart_xml = f'<c:chartSpace xmlns:c="{C}"/>' if chart != "wrong-root" else '<notAChart/>'
                package.writestr("ppt/charts/chart1.xml", chart_xml)
        if root_relationship:
            package.writestr("custom.xml", "<custom/>")
            package.writestr("_rels/custom.xml.rels", f'<Relationships xmlns="{PR}"><Relationship Id="custom1" Type="urn:fixture" Target="ppt/slides/slide1.xml"/></Relationships>')


class HelperRegressions(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="ppt-helper-regression-")
        self.addCleanup(self.temp.cleanup)
        self.work = Path(self.temp.name)
        self.deck = self.work / "fixture.pptx"
        make_package(self.deck)
        self.plan = self.work / "motion.json"
        self.write_plan()

    def write_plan(self, **changes):
        effect = {"shape_name": "target", "effect": "fade", "trigger": "click", "duration": 0.4}
        effect.update(changes)
        self.plan.write_text(json.dumps({"version": 1, "slides": [{"slide": 1, "effects": [effect]}]}), encoding="utf-8")

    def run_process(self, command, *, cwd=None):
        return subprocess.run(command, cwd=cwd or self.work, capture_output=True,
                              text=True, encoding="utf-8", errors="replace", timeout=30)

    def python_helper(self, name, *arguments):
        return self.run_process([sys.executable, "-B", str(SCRIPTS / name), *map(str, arguments)])

    def motion(self, shell):
        return self.run_process([shell, "-NoProfile", "-File", str(SCRIPTS / "apply_motion.ps1"),
                                 "-InputPptx", str(self.deck), "-Plan", str(self.plan),
                                 "-OutputPptx", str(self.work / "animated.pptx"), "-DryRun"])

    def assert_success(self, result):
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_report_path_cannot_replace_source(self):
        before = self.deck.read_bytes()
        result = self.python_helper("pptx_audit.py", self.deck, "--output", self.deck)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.deck.read_bytes(), before)

    def test_report_hardlink_cannot_replace_source(self):
        alias = self.work / "source-alias.json"
        try:
            os.link(self.deck, alias)
        except (OSError, NotImplementedError) as exc:
            self.skipTest(f"Hardlinks unavailable: {exc}")
        before = self.deck.read_bytes()
        result = self.python_helper("pptx_audit.py", self.deck, "--output", alias)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.deck.read_bytes(), before)

    def test_separate_report_succeeds_and_keeps_source(self):
        before = self.deck.read_bytes()
        output = self.work / "reports" / "audit.json"
        result = self.python_helper("pptx_audit.py", self.deck, "--output", output)
        self.assert_success(result)
        self.assertTrue(json.loads(output.read_text(encoding="utf-8"))["pass"])
        self.assertEqual(self.deck.read_bytes(), before)

    def test_utf16_dtd_rejected_in_real_zip_member(self):
        make_package(self.deck, utf16_dtd=True)
        result = self.python_helper("pptx_audit.py", self.deck)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("DTD", result.stderr)

    def test_root_level_relationship_owner_supported(self):
        make_package(self.deck, root_relationship=True)
        result = self.python_helper("pptx_audit.py", self.deck)
        self.assert_success(result)
        self.assertTrue(json.loads(result.stdout)["pass"])

    def test_broken_chart_not_counted_as_native_chart(self):
        for fault in ("missing-relationship", "wrong-type", "missing-part", "wrong-root"):
            with self.subTest(fault=fault):
                make_package(self.deck, chart=fault)
                result = self.python_helper("pptx_audit.py", self.deck)
                self.assertNotEqual(result.returncode, 0)
                report = json.loads(result.stdout)
                self.assertFalse(report["pass"])
                self.assertEqual(report["slides"][0]["native_charts"], 0)

    def test_chart_with_resolved_native_part_counted(self):
        make_package(self.deck, chart="valid")
        result = self.python_helper("pptx_audit.py", self.deck)
        self.assert_success(result)
        self.assertEqual(json.loads(result.stdout)["slides"][0]["native_charts"], 1)

    def test_palette_empty_or_bad_schema_cannot_pass(self):
        cases = [[], {"palettes": []}, {"colors": {}, "pairs": []},
                 {"colors": {"fg": "FFFFFF", "bg": "000000"}, "pairs": []},
                 None, {"palettes": None}]
        for data in cases:
            with self.subTest(data=data):
                path = self.work / "palette.json"
                path.write_text(json.dumps(data), encoding="utf-8")
                result = self.python_helper("palette_check.py", path)
                self.assertNotEqual(result.returncode, 0)
                self.assertNotIn("Traceback", result.stderr)

    def test_palette_nonfinite_thresholds_rejected(self):
        for minimum in ("nan", "inf", "-inf"):
            with self.subTest(minimum=minimum):
                path = self.work / "palette.json"
                data = {"colors": {"fg": "FFFFFF", "bg": "000000"}, "pairs": [{"fg": "fg", "bg": "bg", "minimum": minimum}]}
                path.write_text(json.dumps(data), encoding="utf-8")
                result = self.python_helper("palette_check.py", path)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("Palette input error", result.stderr)

    @unittest.skipUnless(SHELLS, "PowerShell is unavailable; no Office COM is required")
    def test_motion_accepts_comments_and_does_not_create_output(self):
        make_package(self.deck, comment=True)
        before = self.deck.read_bytes()
        for shell in SHELLS:
            with self.subTest(shell=shell):
                result = self.motion(shell)
                self.assert_success(result)
                self.assertFalse(json.loads(result.stdout)["powerpointStarted"])
                self.assertFalse((self.work / "animated.pptx").exists())
                self.assertEqual(self.deck.read_bytes(), before)

    @unittest.skipUnless(SHELLS, "PowerShell is unavailable; no Office COM is required")
    def test_motion_relative_output_uses_powershell_location(self):
        nested = self.work / "changed-location"
        nested.mkdir()
        sentinel = self.work / "relative.pptx"
        sentinel.write_bytes(b"must remain untouched")
        probe = self.work / "location-probe.ps1"
        probe.write_text('''param([string]$Helper,[string]$Deck,[string]$MotionPlan,[string]$Destination)
Set-Location -LiteralPath $Destination
& $Helper -InputPptx $Deck -Plan $MotionPlan -OutputPptx 'relative.pptx' -DryRun
''', encoding="utf-8")
        for shell in SHELLS:
            with self.subTest(shell=shell):
                result = self.run_process([shell, "-NoProfile", "-File", str(probe),
                                           "-Helper", str(SCRIPTS / "apply_motion.ps1"),
                                           "-Deck", str(self.deck), "-MotionPlan", str(self.plan),
                                           "-Destination", str(nested)])
                self.assert_success(result)
                self.assertFalse(json.loads(result.stdout)["powerpointStarted"])
                self.assertEqual(sentinel.read_bytes(), b"must remain untouched")
                self.assertFalse((nested / "relative.pptx").exists())

    @unittest.skipUnless(SHELLS, "PowerShell is unavailable; no Office COM is required")
    def test_motion_rejects_nested_targets_and_existing_timing(self):
        for options in ({"grouped": True}, {"timing": True}):
            make_package(self.deck, **options)
            for shell in SHELLS:
                with self.subTest(shell=shell, options=options):
                    result = self.motion(shell)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertFalse((self.work / "animated.pptx").exists())

    @unittest.skipUnless(SHELLS, "PowerShell is unavailable; no Office COM is required")
    def test_motion_rejects_nonfinite_and_out_of_range_duration(self):
        for value in ("NaN", "Infinity", -0.1, 6):
            self.write_plan(duration=value)
            for shell in SHELLS:
                with self.subTest(shell=shell, duration=value):
                    result = self.motion(shell)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertFalse((self.work / "animated.pptx").exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
