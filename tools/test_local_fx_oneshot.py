"""keep: one-shot comparison report wiring; no network or model calls (call() is mocked)."""
import json
import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch

import local_fx_daily as daily
import local_fx_grounding as grounding
import local_fx_oneshot as oneshot

RUN = daily.ROOT / "shadow-output" / "2026-09-30-observation-trial-02"


def canned(out, label, task, data, schema):
    if label.endswith("story"):
        return {"main_driver": "x", "hero": "冒頭。", "headline": "見出し", "summary": "要約。", "market": "市場。"}
    if label.endswith("topics"):
        return {"topics": [{"title": f"話題{i}", "body": "本文。"} for i in range(4)], "points": ["一。", "二。", "三。"]}
    if label.endswith("today"):
        return {"handover": "引継ぎ。", "focus_pair": data["ranking_top5"][0]["pair"], "focus_body": "注目。",
                "risk_level": "HIGH", "risk_body": "リスク。", "key_event_nos": [2, 1, 2, 9999]}
    return {"issues": []}


@unittest.skipUnless(RUN.exists(), "saved 2026-09-30 evidence run not present")
class OneshotTests(unittest.TestCase):
    def setUp(self):  # never call the real external reviewer from these tests
        patcher = patch.object(oneshot.external_review, "review", return_value={"status": "disabled"})
        patcher.start()
        self.addCleanup(patcher.stop)

    def inputs(self):
        return (json.loads((RUN / "shared-material.json").read_text(encoding="utf-8"))["facts"],
                json.loads((RUN / "calendar.json").read_text(encoding="utf-8")),
                json.loads((RUN / "market.json").read_text(encoding="utf-8"))["ranking"])

    def test_input_keeps_low_importance_events_and_original_passages(self):
        material, calendar, ranking = self.inputs()
        self.assertTrue(any("5.2911" in p for p in oneshot.passages(material)))
        self.assertGreaterEqual(len(oneshot.compact(material)), len([x for x in material if x.get("fact")]) - 1)

    def test_generate_writes_report_without_model(self):
        material, calendar, ranking = self.inputs()
        with tempfile.TemporaryDirectory() as folder, patch.object(oneshot, "call", side_effect=canned):
            out = Path(folder) / "oneshot"
            out.mkdir()
            (out / "policy.json").write_text((RUN / "policy.json").read_text(encoding="utf-8"), encoding="utf-8")
            checks = oneshot.generate(out, date(2026, 9, 30), material, calendar, ranking,
                                      json.loads((out / "policy.json").read_text(encoding="utf-8")))
            self.assertTrue((out / "report.html").exists())
            self.assertFalse(checks["publish_ready"])

    def test_external_reviewer_findings_go_to_the_repair_step(self):
        material, calendar, ranking = self.inputs()
        seen = {}

        def calls(out, label, task, data, schema, *rest):
            if label.endswith("repair"):
                seen["problems"] = data["problems"]
                return {"fixes": [{"section": "focus", "text": "直した注目。"}]}
            return canned(out, label, task, data, schema)

        reviews = []

        def reviewer(out, data, texts):
            reviews.append(dict(texts))
            return {"status": "ok", "issues": [{"section": "focus", "excerpt": "注目。", "kind": "取り違え", "reason": "指標名が違う"}]}

        with tempfile.TemporaryDirectory() as folder, patch.object(oneshot, "call", side_effect=calls), patch.object(
                oneshot.external_review, "review", side_effect=reviewer):
            out = Path(folder)
            (out / "policy.json").write_text((RUN / "policy.json").read_text(encoding="utf-8"), encoding="utf-8")
            checks = oneshot.generate(out, date(2026, 9, 30), material, calendar, ranking,
                                      json.loads((out / "policy.json").read_text(encoding="utf-8")))
        self.assertTrue(any("指標名が違う" in p["reason"] and p["sections"] == ["focus"] for p in seen["problems"]))
        self.assertEqual(checks["repaired_sections"], ["focus"])
        self.assertEqual(reviews[0]["focus"], "注目。")      # first review sees the draft
        self.assertEqual(reviews[1]["focus"], "直した注目。")  # second review sees the repaired text
        self.assertIn("external_review_after", checks)

    def test_cut_off_repair_keeps_the_draft_and_the_report(self):
        material, calendar, ranking = self.inputs()

        def calls(out, label, task, data, schema, *rest):
            if label.endswith("repair"):
                self.assertEqual(rest, (30000,))  # thinking alone used 12000 on 2026-10-06
                raise ValueError("oneshot-5-repair: wrong model or incomplete response (length)")
            return canned(out, label, task, data, schema)

        issue = {"status": "ok", "issues": [{"section": "focus", "excerpt": "注目。", "kind": "取り違え", "reason": "x"}]}
        with tempfile.TemporaryDirectory() as folder, patch.object(oneshot, "call", side_effect=calls), patch.object(
                oneshot.external_review, "review", return_value=issue):
            out = Path(folder)
            (out / "policy.json").write_text((RUN / "policy.json").read_text(encoding="utf-8"), encoding="utf-8")
            checks = oneshot.generate(out, date(2026, 9, 30), material, calendar, ranking,
                                      json.loads((out / "policy.json").read_text(encoding="utf-8")))
            self.assertTrue((out / "report.html").exists())
        self.assertIn("incomplete response", checks["repair_error"])
        self.assertNotIn("repaired_sections", checks)
        self.assertEqual(checks["external_review_after"]["status"], "skipped")

    def test_key_events_follow_model_selection_in_time_order_and_ignore_invalid_numbers(self):
        material, calendar, ranking = self.inputs()
        first, second = calendar["events"][0], calendar["events"][1]
        with tempfile.TemporaryDirectory() as folder, patch.object(oneshot, "call", side_effect=canned), patch.object(
                daily, "render") as render:
            out = Path(folder)
            (out / "policy.json").write_text((RUN / "policy.json").read_text(encoding="utf-8"), encoding="utf-8")
            oneshot.generate(out, date(2026, 9, 30), material, calendar, ranking,
                             json.loads((out / "policy.json").read_text(encoding="utf-8")))
            shown = render.call_args.args[2]
            self.assertEqual(shown["key_events"], [first, second])

    def test_failure_is_recorded_and_does_not_raise(self):
        material, calendar, ranking = self.inputs()
        with tempfile.TemporaryDirectory() as folder, patch.object(oneshot, "call", side_effect=ValueError("boom")):
            out = Path(folder)
            (out / "policy.json").write_text((RUN / "policy.json").read_text(encoding="utf-8"), encoding="utf-8")
            grounding.run_oneshot(out, date(2026, 9, 30), material, calendar, ranking)
            self.assertIn("boom", json.loads((out / "oneshot" / "error.json").read_text(encoding="utf-8"))["error"])


if __name__ == "__main__":
    unittest.main()
