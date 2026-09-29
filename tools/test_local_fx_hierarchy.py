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
        is_leaf = "fact_id" in data["inputs"][0]
        return {"units": [{"text": "前日の材料群。予想と実績は区別。"}],
                "routes": {ref: 0 if is_leaf else [0] for ref in ids}}

    def test_tree_visits_every_fact_and_preserves_original_without_mutation(self):
        facts = self.facts(60)
        with tempfile.TemporaryDirectory() as folder, patch.object(daily, "infer_cached", side_effect=self.inference) as infer:
            tree = hierarchy.build(daily, Path(folder), facts, date(2026, 9, 29), {})
            self.assertEqual(set(tree["root"]["covered_fact_ids"]), {x["fact_id"] for x in facts})
            self.assertGreater(len([n for n in tree["nodes"] if n["children"]]), 1)
            self.assertTrue(all(len(n["covered_fact_ids"]) <= 6 for n in tree["nodes"] if not n["children"]))
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
            return {"units": [{"text": "要約"}], "routes": {"UNKNOWN": 0}}
        with tempfile.TemporaryDirectory() as folder, patch.object(daily, "infer_cached", side_effect=missing) as infer:
            with self.assertRaisesRegex(ValueError, "summary review failed"):
                hierarchy.build(daily, Path(folder), self.facts(3), date(2026, 9, 29), {})
            self.assertEqual(sum("repair" in c.args[1] for c in infer.call_args_list), 1)
            repair = next(c for c in infer.call_args_list if c.args[1].endswith("-repair"))
            self.assertIn("N0", repair.args[3]["review"]["reason"])
            self.assertIn("UNKNOWN", repair.args[3]["review"]["reason"])
            self.assertNotIn("rejected", repair.args[3])
            self.assertIn("独自分析は最後の記事工程", repair.args[2])

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
            return {"units": [{"text": "米伊交渉"}], "routes": {"N0": 0}}
        with tempfile.TemporaryDirectory() as folder, patch.object(daily, "infer_cached", side_effect=wrong_country):
            with self.assertRaisesRegex(ValueError, "Iran replaced by Italy"):
                hierarchy.build(daily, Path(folder), [fact], date(2026, 9, 29), {})

    def test_entity_spelling_constraint_comes_from_input_not_fixed_theme(self):
        for fact, expected in [("米国とイランの交渉", True), ("本日の会合予定", False)]:
            with tempfile.TemporaryDirectory() as folder, patch.object(daily, "infer_cached", side_effect=self.inference) as infer:
                hierarchy.build(daily, Path(folder), [{"fact_id": "N0", "fact": fact}], date(2026, 9, 29), {})
                data = infer.call_args_list[0].args[3]
                self.assertEqual("entity_spelling_rules" in data, expected)
                if expected:
                    self.assertIn("米伊", data["entity_spelling_rules"]["イラン"])

    def test_one_child_summary_can_support_multiple_parent_units(self):
        children = [{"node_id": "child-a", "units": ["前日の円高。", "本日の会合予定。"]},
                    {"node_id": "child-b", "units": ["円の背景。"]}]
        def fanout(out, label, task, data, schema):
            if "review" in label:
                return {"verdict": "PASS", "reason": "fixture"}
            return {"units": [{"text": "前日の円高と背景。"}, {"text": "本日の会合予定。"}],
                    "routes": {"child-a": [0, 1], "child-b": [0]}}
        with tempfile.TemporaryDirectory() as folder, patch.object(daily, "infer_cached", side_effect=fanout):
            summary = hierarchy.summarize(daily, Path(folder), "merge", children, date(2026, 9, 29), {}, False)
            self.assertEqual(summary["units"][0]["refs"], ["child-a", "child-b"])
            self.assertEqual(summary["units"][1]["refs"], ["child-a"])

    def test_semantic_review_receives_reference_local_support(self):
        facts = self.facts(2)
        def two_units(out, label, task, data, schema):
            if "review" in label:
                self.assertIn("別unitの入力で補完しない", task)
                checks = data["reference_checks"]
                self.assertEqual(checks[0]["supporting_input_ids"], [facts[0]["fact_id"]])
                self.assertEqual(checks[1]["supporting_input_ids"], [facts[1]["fact_id"]])
                return {"verdict": "PASS", "reason": "fixture only"}
            return {"units": [{"text": "材料0"}, {"text": "材料1"}], "routes": {"N0": 0, "N1": 1}}
        with tempfile.TemporaryDirectory() as folder, patch.object(daily, "infer_cached", side_effect=two_units):
            hierarchy.build(daily, Path(folder), facts, date(2026, 9, 29), {})


if __name__ == "__main__":
    unittest.main()
