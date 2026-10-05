"""keep: external review wiring; no real codex call (subprocess.run is injected)."""
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

import local_fx_external_review as ext


class ExternalReviewTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.out = self.root / "run"
        self.out.mkdir()
        self.cfg = self.root / "cfg.json"
        self.cfg.write_text(json.dumps({"external_review": {"enabled": True, "model": "m", "timeout_seconds": 5}}), encoding="utf-8")
        base = self.root / "ext"
        for version in ["26.818.1-win32-x64", "26.930.2-win32-x64", "26.9.9-win32-x64"]:
            exe = base / f"openai.chatgpt-{version}" / ext.CODEX_RELATIVE
            exe.parent.mkdir(parents=True)
            exe.write_text("x")
        self.ext = base

    def tearDown(self):
        self.tmp.cleanup()

    def fake(self, text, code=0):
        def run(cmd, **kwargs):
            if "--output-last-message" in cmd:
                Path(cmd[cmd.index("--output-last-message") + 1]).write_text(text, encoding="utf-8")
            return subprocess.CompletedProcess(cmd, code, "", "err")
        return run

    def call(self, run, cfg=None):
        return ext.review(self.out, {"facts": []}, {"hero": "x"}, run=run, config_path=cfg or self.cfg, extensions=self.ext)

    def test_newest_version_is_numeric_not_lexical(self):
        self.assertIn("26.930.2", str(ext.newest_codex(self.ext)))

    def test_ok_returns_issues(self):
        issue = [{"section": "focus", "excerpt": "a", "kind": "取り違え", "reason": "r"}]
        result = self.call(self.fake("```json\n" + json.dumps(issue) + "\n```"))
        self.assertEqual((result["status"], result["issues"]), ("ok", issue))

    def test_empty_array_is_ok(self):
        self.assertEqual(self.call(self.fake("[]"))["issues"], [])

    def test_disabled_or_missing_config_never_runs(self):
        def boom(*a, **k):
            raise AssertionError("must not run")
        self.cfg.write_text(json.dumps({"external_review": {"enabled": False}}), encoding="utf-8")
        self.assertEqual(self.call(boom)["status"], "disabled")
        self.assertEqual(self.call(boom, cfg=self.root / "missing.json")["status"], "disabled")

    def test_failures_are_recorded_not_raised(self):
        self.assertEqual(self.call(self.fake("[]", code=1))["status"], "error")
        self.assertEqual(self.call(self.fake("not json"))["status"], "error")

        def timeout(cmd, **kwargs):
            raise subprocess.TimeoutExpired(cmd, 5)
        self.assertIn("TimeoutExpired", self.call(timeout)["error"])

    def test_no_codex_installed_is_an_error_record(self):
        result = ext.review(self.out, {}, {}, run=self.fake("[]"), config_path=self.cfg, extensions=self.root / "none")
        self.assertEqual(result["status"], "error")


if __name__ == "__main__":
    unittest.main()
