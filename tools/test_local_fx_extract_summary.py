"""keep: deterministic ID-only compression/provenance tests, not model quality."""
import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch

import local_fx_daily as daily
import local_fx_extract_summary as selection
import local_fx_hierarchy as hierarchy


class ExtractiveTests(unittest.TestCase):
    def facts(self, count=3):
        return [{"fact_id": f"F{i}", "fact": f"2026-09-30に米国とイランの会合{i}が予定される。",
                 "event_date": "2026-09-30", "event_scope": "future", "record_type": "forecast",
                 "pairs": ["USD/JPY"], "market_session": "NY"} for i in range(count)]

    def inference(self, out, label, task, data, schema):
        if "review" in label:
            return {"verdict": "PASS", "reason": "fixture only"}
        facts = data["facts"]
        cap = len(facts) if "leaf" in label else min(selection.CAP, len(facts))
        return {"groups": [{"fact_ids": [x["fact_id"] for x in facts[:cap]]}]}

    def test_dates_names_numbers_and_types_are_copied_not_written(self):
        pool = self.facts()
        raw = {"groups": [{"fact_ids": ["F2", "F0"]}, {"fact_ids": ["F1"]}]}
        value = selection.assemble(raw, pool, True)
        self.assertEqual(value["retained_facts"], [pool[2], pool[0], pool[1]])
        self.assertIn("イラン", value["units"][0]["text"])
        self.assertNotIn("米伊", value["units"][0]["text"])
        self.assertIn("forecast", value["units"][0]["text"])
        self.assertEqual(value["units"][0]["refs"], ["F2", "F0"])

    def test_generated_prose_unknown_duplicate_and_leaf_omission_fail(self):
        wrong = [{"groups": [{"fact_ids": ["F0"], "text": "説明"}]},
                 {"groups": [{"fact_ids": ["UNKNOWN"]}]},
                 {"groups": [{"fact_ids": ["F0"]}, {"fact_ids": ["F0"]}]},
                 {"groups": [{"fact_ids": ["F0"]}]},
                 {"groups": [], "text": "説明"}]
        for raw in wrong:
            with self.assertRaises(ValueError):
                selection.assemble(raw, self.facts(), True)

    def test_budget_failure_does_not_slice_original(self):
        pool = self.facts(1)
        pool[0]["fact"] = "原文" * selection.BUDGET
        before = pool[0]["fact"]
        with self.assertRaisesRegex(ValueError, "byte budget"):
            selection.assemble({"groups": [{"fact_ids": ["F0"]}]}, pool, True)
        self.assertEqual(pool[0]["fact"], before)

    def test_parent_omission_is_explicit_not_false_coverage(self):
        value = selection.assemble({"groups": [{"fact_ids": ["F1"]}]}, self.facts(), False)
        self.assertEqual(value["omitted_fact_ids"], ["F0", "F2"])

    def test_failed_selection_qc_stops_after_one_repair(self):
        def fail(out, label, task, data, schema):
            if "review" in label:
                return {"verdict": "FAIL", "reason": "major opposite material lost"}
            return self.inference(out, label, task, data, schema)
        with tempfile.TemporaryDirectory() as folder, patch.object(daily, "infer_cached", side_effect=fail) as infer:
            with self.assertRaisesRegex(ValueError, "major opposite"):
                selection.summarize(daily, Path(folder), "leaf", self.facts(), {}, True)
            self.assertEqual(sum(c.args[1].endswith("-repair") for c in infer.call_args_list), 1)

    def test_no_prose_can_pass_even_when_self_review_would_pass(self):
        def prose(out, label, task, data, schema):
            return {"groups": [{"fact_ids": ["F0"], "text": "米伊交渉"}]}
        with tempfile.TemporaryDirectory() as folder, patch.object(daily, "infer_cached", side_effect=prose):
            with self.assertRaisesRegex(ValueError, "fact_ids only"):
                selection.summarize(daily, Path(folder), "leaf", self.facts(1), {}, True)

    def test_complete_tree_keeps_original_lineage_and_bounded_payload(self):
        pool = self.facts(90)
        with tempfile.TemporaryDirectory() as folder, patch.object(daily, "infer_cached", side_effect=self.inference) as infer:
            tree = hierarchy.build(daily, Path(folder), pool, date(2026, 9, 29), {}, extractive=True)
            self.assertEqual(set(tree["root"]["covered_fact_ids"]), {x["fact_id"] for x in pool})
            self.assertEqual(tree["method"], selection.METHOD)
            self.assertLessEqual(len(tree["root"]["retained_facts"]), selection.CAP)
            by_id = {x["fact_id"]: x for x in pool}
            for node in tree["nodes"]:
                self.assertLessEqual(selection.size(node["retained_facts"]), selection.BUDGET)
                for fact in node["retained_facts"]:
                    self.assertEqual(fact, by_id[fact["fact_id"]])
            for call in infer.call_args_list:
                self.assertLess(len(__import__("json").dumps(call.args[3], ensure_ascii=False).encode()), 17000)


if __name__ == "__main__":
    unittest.main()
