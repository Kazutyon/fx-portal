"""keep: observation-mode regression tests; no live model, network or cron run."""
import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch

import local_fx_daily as daily
import local_fx_grounding as grounding
import local_fx_hierarchy as hierarchy
import local_fx_summary_observation as observation


class ObservationTests(unittest.TestCase):
    def inference(self, out, label, task, data, schema):
        if label.endswith("review-plan"):
            return {"verdict": "FAIL", "reason": "fixture missing opposite condition"}
        key = "fact_id" if "fact_id" in data["inputs"][0] else "node_id"
        return {"units": [{"text": "入力から判断した要約。", "refs": [data["inputs"][0][key]]}]}

    def test_review_failure_is_recorded_without_content_repair_or_false_pass(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(daily, "infer_cached", side_effect=self.inference) as infer:
            out = Path(folder)
            value = observation.summarize(daily, out, "leaf", [{"fact_id": "F0", "fact": "原材料"}], {}, True)
            self.assertEqual(len(infer.call_args_list), 2)
            self.assertEqual(value["units"][0]["text"], "入力から判断した要約。")
            saved = daily.load(out / "hierarchy" / "leaf.json")
            self.assertTrue(saved["review_is_advisory"])
            self.assertEqual(saved["review"]["verdict"], "FAIL")

    def test_unknown_reference_and_oversized_output_still_stop(self):
        for unit in [{"text": "文", "refs": ["UNKNOWN"]},
                     {"text": "長文" * observation.BUDGET, "refs": ["F0"]}]:
            with tempfile.TemporaryDirectory() as folder, patch.object(daily, "infer_cached", return_value={"units": [unit]}) as infer:
                with self.assertRaises(ValueError):
                    observation.summarize(daily, Path(folder), "leaf", [{"fact_id": "F0"}], {}, True)
                self.assertEqual(infer.call_count, 2)

    def test_whole_tree_visits_all_facts_but_does_not_claim_retention_or_quality(self):
        material = [{"fact_id": f"F{i}", "fact": f"原材料{i}"} for i in range(25)]
        with tempfile.TemporaryDirectory() as folder, patch.object(daily, "infer_cached", side_effect=self.inference):
            tree = hierarchy.build(daily, Path(folder), material, date(2026, 9, 30), {}, observational=True)
            self.assertEqual(set(tree["root"]["covered_fact_ids"]), {x["fact_id"] for x in material})
            self.assertEqual(tree["method"], observation.METHOD)
            self.assertTrue(tree["content_reviews_advisory"])
            self.assertNotIn("retained_facts", tree["root"])

    def test_quality_review_does_not_rewrite_observed_draft(self):
        draft = {"title": "見出し", "body": "本文", "review": {"verdict": "PASS"}}
        with patch.object(grounding, "author", return_value=draft) as author, patch.object(
                grounding, "review_editorial_quality", return_value={"verdict": "FAIL", "reason": "thin"}):
            result = grounding.improve_editorial(daily, Path("unused"), "market", "市場環境", [], {},
                date(2026, 9, 30), "300", observational=True)
            self.assertEqual(author.call_count, 1)
            self.assertEqual(result["body"], "本文")
            self.assertEqual(result["quality_review"]["verdict"], "FAIL")

    def test_initial_source_failure_remains_fatal(self):
        with patch.object(grounding, "author", side_effect=ValueError("source failure")):
            with self.assertRaisesRegex(ValueError, "source failure"):
                grounding.improve_editorial(daily, Path("unused"), "market", "市場環境", [], {},
                    date(2026, 9, 30), "300", observational=True)

    def test_ff_refusal_does_not_fabricate_confirmation(self):
        def source(out, label, url):
            if label == "forexfactory":
                raise ValueError("HTTP 403")
            return "KissFX 本文"
        event = {"name": "住宅指標", "country": "USD", "time_jst": "22:00",
                 "importance": "medium",
                 "datetime_jst": "2026-09-30T22:00:00+09:00", "forecast": "—", "previous": "—"}
        with tempfile.TemporaryDirectory() as folder, patch.object(daily, "snapshot", side_effect=source), patch.object(
                daily, "parse_kiss", return_value=[event]), patch.object(daily, "mirror_enabled", return_value=True):
            out = Path(folder)
            result = daily.collect_calendar(date(2026, 9, 30), out, allow_single_source=True)
            self.assertFalse(result["events"][0]["confirmed"])
            self.assertEqual(len(result["events"][0]["sources"]), 1)
            self.assertTrue((out / "calendar-source-error.json").exists())
            with self.assertRaisesRegex(ValueError, "403"):
                daily.collect_calendar(date(2026, 9, 30), Path(folder) / "strict")

    def test_observation_writer_receives_only_topic_facts_not_global_overview(self):
        fact = {"fact_id": "N1-6", "fact": "住宅価格指数は予想を上回った。",
                "quote": "住宅価格指数：+0.3（予想+0.1）", "record_type": "actual"}
        draft = {"title": "住宅指標", "statements": [
            {"text": "住宅価格指数は予想を上回った。", "fact_ids": ["N1-6"], "mode": "fact"}]}
        calls = []

        def infer(out, label, task, data, schema):
            calls.append((label, task, data))
            return draft

        with tempfile.TemporaryDirectory() as folder, patch.object(daily, "infer_cached", side_effect=infer), patch.object(
                grounding, "review_copy", return_value={"verdict": "PASS", "reason": "supported"}):
            grounding.author(daily, Path(folder), "topic", "指標の振り返り", [fact],
                             date(2026, 9, 30), "250", overview={"synopsis": ["別記事のFRB観測"]},
                             observational=True)
        self.assertEqual(len(calls), 1)
        self.assertNotIn("global_overview", calls[0][2])
        self.assertEqual([x["fact_id"] for x in calls[0][2]["facts"]], ["N1-6"])
        self.assertIn("値動きや理由の根拠がなければ無理に書かず", calls[0][1])

    def test_observation_repair_rebuilds_from_same_facts_and_still_fails_closed(self):
        fact = {"fact_id": "N1-6", "fact": "住宅価格指数は予想を上回った。",
                "quote": "住宅価格指数：+0.3（予想+0.1）", "record_type": "actual"}
        draft = {"title": "誤った解釈", "statements": [
            {"text": "FRBが追加利上げした。", "fact_ids": ["N1-6"], "mode": "fact"}]}
        calls = []

        def infer(out, label, task, data, schema):
            calls.append((label, task, data))
            return draft

        with tempfile.TemporaryDirectory() as folder, patch.object(daily, "infer_cached", side_effect=infer), patch.object(
                grounding, "review_copy", return_value={"verdict": "FAIL", "reason": "unsupported"}):
            with self.assertRaisesRegex(ValueError, "original-context review failed"):
                grounding.author(daily, Path(folder), "topic", "指標の振り返り", [fact],
                                 date(2026, 9, 30), "250", overview={"synopsis": ["別記事のFRB観測"]},
                                 observational=True)
        self.assertEqual([x[0] for x in calls], ["topic-write", "topic-repair"])
        self.assertNotIn("global_overview", calls[1][2])
        self.assertIn("根拠のない文や句は削除", calls[1][1])

    def test_below_forecast_is_not_downward_revision(self):
        fact = {"fact_id": "N1-8", "record_type": "actual", "quote": "指数81.9（予想89.0、前回88.6←89.4）"}
        wrong = {"title": "指標", "statements": [{"text": "景気指標は下方修正となり、予想を下回った。",
                 "fact_ids": ["N1-8"], "mode": "fact"}]}
        errors = grounding.copy_errors(wrong, [fact], date(2026, 9, 30))
        self.assertIn("below-forecast result described as a downward revision", errors)
        wrong["statements"][0]["text"] = "景気指標は予想を下回った。"
        self.assertNotIn("below-forecast result described as a downward revision",
                         grounding.copy_errors(wrong, [fact], date(2026, 9, 30)))


if __name__ == "__main__":
    unittest.main()
