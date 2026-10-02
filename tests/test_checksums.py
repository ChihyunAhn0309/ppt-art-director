"""Regression checks for exact published bytes and manifest coverage; no Office."""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "verify_checksums.py"
SPEC = importlib.util.spec_from_file_location("verify_checksums", SCRIPT)
checksums = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checksums)


class ChecksumTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="ppt-checksums-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.directory = self.root / "example"
        self.directory.mkdir()
        self.manifest = self.directory / "checksums.json"
        self.payload = self.directory / "deck.pptx"
        self.payload.write_bytes(b"Exact file bytes\x00\xff\r\n")
        self.entries = {"deck.pptx": self.digest(self.payload.read_bytes())}
        self.write_manifest()

    @staticmethod
    def digest(data):
        return hashlib.sha256(data).hexdigest()

    def write_manifest(self, data=None):
        self.manifest.write_text(json.dumps(self.entries if data is None else data), encoding="utf-8")

    def cli(self):
        environment = dict(os.environ, PYTHONIOENCODING="ascii:strict", PYTHONUTF8="0")
        return subprocess.run([sys.executable, "-B", str(SCRIPT), str(self.manifest)],
                              env=environment, capture_output=True, timeout=30)

    def test_valid_binary_nested_unicode_and_uppercase_digest(self):
        nested = self.directory / "design" / "설명.txt"
        nested.parent.mkdir()
        nested.write_bytes("가상 값\n".encode("utf-8"))
        self.entries["design/설명.txt"] = self.digest(nested.read_bytes()).upper()
        self.write_manifest()
        report = checksums.verify(self.manifest)
        self.assertTrue(report["pass"])
        self.assertEqual(report["checked_files"], 2)
        result = self.cli()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(json.loads(result.stdout.decode("ascii"))["pass"])

    def test_line_ending_change_fails_exact_bytes(self):
        self.payload.write_bytes(self.payload.read_bytes().replace(b"\r\n", b"\n"))
        result = self.cli()
        self.assertEqual(result.returncode, 1, result.stderr)
        report = json.loads(result.stdout.decode("ascii"))
        self.assertFalse(report["pass"])
        self.assertIn("SHA-256 mismatch: deck.pptx", report["errors"][0])

    def test_deleted_and_unlisted_files_fail_coverage(self):
        self.payload.unlink()
        (self.directory / "new.png").write_bytes(b"unlisted")
        report = checksums.verify(self.manifest)
        self.assertFalse(report["pass"])
        self.assertIn("Missing regular file: deck.pptx", report["errors"])
        self.assertIn("Unlisted file: new.png", report["errors"])

    def test_invalid_manifest_shapes_and_hashes(self):
        for invalid in ({}, [], {"deck.pptx": "abc"}, {"deck.pptx": None},
                        {"deck.pptx": ["a" * 64]}):
            with self.subTest(invalid=invalid):
                self.write_manifest(invalid)
                with self.assertRaises(ValueError):
                    checksums.verify(self.manifest)

    def test_duplicate_json_keys_are_rejected(self):
        digest = self.entries["deck.pptx"]
        self.manifest.write_text('{"deck.pptx":"' + digest + '","deck.pptx":"' + digest + '"}', encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            checksums.verify(self.manifest)

    def test_path_escape_and_noncanonical_entries_are_rejected(self):
        for name in ("", ".", "../outside", "nested/../../outside", "/absolute",
                     "C:/absolute", "C:relative", "\\\\server\\file", "nested\\file",
                     "./deck.pptx", "nested//file", "nested/./file", "bad\0path"):
            with self.subTest(name=name):
                self.write_manifest({name: "0" * 64})
                with self.assertRaises(ValueError):
                    checksums.verify(self.manifest)

    def test_manifest_cannot_cover_itself(self):
        self.write_manifest({"checksums.json": "0" * 64})
        with self.assertRaisesRegex(ValueError, "itself"):
            checksums.verify(self.manifest)

    def test_invalid_input_cli_returns_two_without_traceback(self):
        self.manifest.write_text("invalid JSON", encoding="utf-8")
        result = self.cli()
        self.assertEqual(result.returncode, 2)
        self.assertIn("input_error", json.loads(result.stderr.decode("ascii")))
        self.assertNotIn(b"Traceback", result.stderr)

    def test_symlink_escape_is_rejected(self):
        outside = self.root / "outside.txt"
        outside.write_bytes(b"outside")
        link = self.directory / "linked.txt"
        try:
            link.symlink_to(outside)
        except (OSError, NotImplementedError) as exc:
            self.skipTest(f"Symlinks unavailable ({type(exc).__name__}, errno={getattr(exc, 'errno', None)})")
        self.entries["linked.txt"] = self.digest(outside.read_bytes())
        self.write_manifest()
        with self.assertRaisesRegex(ValueError, "Symlinks"):
            checksums.verify(self.manifest)

    def test_unlisted_symlink_directory_is_not_traversed(self):
        outside = self.root / "outside"
        outside.mkdir()
        (outside / "secret.txt").write_bytes(b"outside")
        link = self.directory / "linked"
        try:
            link.symlink_to(outside, target_is_directory=True)
        except (OSError, NotImplementedError) as exc:
            self.skipTest(f"Symlinks unavailable ({type(exc).__name__}, errno={getattr(exc, 'errno', None)})")
        report = checksums.verify(self.manifest)
        self.assertFalse(report["pass"])
        self.assertEqual(report["errors"], ["Unsupported symlink: linked"])

    @unittest.skipUnless(os.name == "nt", "Windows junction regression")
    def test_windows_junction_escape_is_not_traversed(self):
        outside = self.root / "outside"
        outside.mkdir()
        (outside / "not-in-scope.txt").write_bytes(b"outside")
        junction = self.directory / "linked"
        result = subprocess.run(["cmd", "/c", "mklink", "/J", str(junction), str(outside)],
                                capture_output=True, timeout=30)
        if result.returncode:
            self.skipTest("Junction creation unavailable")
        self.addCleanup(junction.rmdir)
        report = checksums.verify(self.manifest)
        self.assertFalse(report["pass"])
        self.assertEqual(report["errors"], ["Directory escapes manifest scope: linked"])
        self.entries["linked/not-in-scope.txt"] = self.digest(b"outside")
        self.write_manifest()
        with self.assertRaisesRegex(ValueError, "escapes"):
            checksums.verify(self.manifest)


if __name__ == "__main__":
    unittest.main(verbosity=2)
