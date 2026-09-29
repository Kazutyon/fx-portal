"""keep: offline summary-tree coverage, budget and fail-closed regressions."""
import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch

import local_fx_daily as daily
import local_fx_hierarchy as hierarchy


class HierarchyTests(unittest.TestCase):
    def facts(self, count):
        return [{"fact_id": f"N{i}", "fact": f"2026-09-28の別材料{i}。" + "背景" * 180,
                 "event_date": "2026-09-28", "event_scope": "previous", "record_type": "actual",
                 "quote": f"別材料{i}", "source_context": {"original": "原文"}} for i in range(count)]

    def inference(self, out, label, task, data, schema):
        if "review" in label:
            return {"verdict": "PASS", "reason": "offline fixture, not model quality"}
        ids = [x.get("fact_id", x.get("node_id")) for x in data["inputs"]]
        return {"units": [{"text": "前日の材料群。予想と実績は区別。", "refs": ids}]}

    def test_tree_visits_every_fact_and_preserves_original_without_mutation(self):
        facts = self.facts(60)
        with tempfile.TemporaryDirectory() as folder, patch.object(daily, "infer_cached", side_effect=self.inference) as infer:
            tree = hierarchy.build(daily, Path(folder), facts, date(2026, 9, 29), {})
            self.assertEqual(set(tree["root"]["covered_fact_ids"]), {x["fact_id"] for x in facts})
            self.assertGreater(len([n for n in tree["nodes"] if n["children"]]), 1)
            for call in infer.call_args_list:
                self.assertLess(len(__import__("json").dumps(call.args[3], ensure_ascii=False).encode()), 15000)
                if "merge" in call.args[1]:
                    self.assertLessEqual(len(call.args[3]["inputs"]), 3)
            self.assertIn("source_context", facts[0])
            self.assertNotIn("source_context", hierarchy.compact_fact(facts[0]))

    def test_missing_or_unknown_refs_fail_after_one_repair(self):
        def missing(out, label, task, data, schema):
            if "review" in label:
                return {"verdict": "PASS", "reason": "not enough to bypass refs"}
            return {"units": [{"text": "要約", "refs": ["UNKNOWN"]}]}
        with tempfile.TemporaryDirectory() as folder, patch.object(daily, "infer_cached", side_effect=missing) as infer:
            with self.assertRaisesRegex(ValueError, "summary review failed"):
                hierarchy.build(daily, Path(folder), self.facts(3), date(2026, 9, 29), {})
            self.assertEqual(sum("repair" in c.args[1] for c in infer.call_args_list), 1)
            repair = next(c for c in infer.call_args_list if c.args[1].endswith("-repair"))
            self.assertIn("N0", repair.args[3]["review"]["reason"])
            self.assertIn("UNKNOWN", repair.args[3]["review"]["reason"])
            self.assertNotIn("rejected", repair.args[3])

    def test_semantic_summary_failure_is_not_ignored(self):
        def fail(out, label, task, data, schema):
            if "review" in label:
                return {"verdict": "FAIL", "reason": "forecast became actual"}
            return self.inference(out, label, task, data, schema)
        with tempfile.TemporaryDirectory() as folder, patch.object(daily, "infer_cached", side_effect=fail):
            with self.assertRaisesRegex(ValueError, "forecast became actual"):
                hierarchy.build(daily, Path(folder), self.facts(3), date(2026, 9, 29), {})

    def test_allocator_retrieves_original_quote_not_summary_as_evidence(self):
        facts = self.facts(3)
        tree = {"root": {"units": [{"text": "全体の見取り図"}]}, "nodes": [
            {"node_id": "leaf", "units": [{"text": "短い要約"}], "children": [],
             "covered_fact_ids": [x["fact_id"] for x in facts]}]}
        def select(out, label, task, data, schema):
            if "branches" in data:
                return {"node_ids": ["leaf"]}
            return {"fact_ids": ["N1"]}
        with tempfile.TemporaryDirectory() as folder, patch.object(daily, "infer_cached", side_effect=select):
            result = hierarchy.allocate(daily, Path(folder), "market", facts, date(2026, 9, 29), {}, tree, "市場環境")
            self.assertEqual(result, [facts[1]])
            self.assertEqual(result[0]["quote"], "別材料1")

    def test_empty_or_duplicate_originals_rejected(self):
        for facts in [[], self.facts(1) * 2]:
            with self.assertRaisesRegex(ValueError, "unique original"):
                hierarchy.build(daily, Path("unused"), facts, date(2026, 9, 29), {})

    def test_country_corruption_is_rejected_before_merge_even_if_self_review_passes(self):
        fact = {"fact_id": "N0", "fact": "米国とイランの交渉", "record_type": "actual"}
        def wrong_country(out, label, task, data, schema):
            if "review" in label:
                return {"verdict": "PASS", "reason": "self review misses it"}
            return {"units": [{"text": "米伊交渉", "refs": ["N0"]}]}
        with tempfile.TemporaryDirectory() as folder, patch.object(daily, "infer_cached", side_effect=wrong_country):
            with self.assertRaisesRegex(ValueError, "Iran replaced by Italy"):
                hierarchy.build(daily, Path(folder), [fact], date(2026, 9, 29), {})


if __name__ == "__main__":
    unittest.main()
