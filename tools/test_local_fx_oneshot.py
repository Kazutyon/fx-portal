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
        ids = [f["id"] for f in data["facts"] if f["id"].startswith("N") and f["type"] != "outlook" and not f["fact"].startswith("・")]
        return {"topics": [{"title": f"話題{i}", "fact_ids": ids[2 * i:2 * i + 2]} for i in range(4)], "market_view_ids": []}
    if label.endswith("today"):
        return {"focus_pair": data["ranking_top5"][0]["pair"], "focus_view_id": "", "risk_view_ids": [],
                "point_ids": ["e1", "e2", "e3"], "key_event_nos": [2, 1, 2, 9999]}
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

    def test_handover_is_built_from_the_calendar_not_the_model(self):
        events = [{"time_jst": "21:30", "country": "CAD", "name": "失業率", "forecast": "6.5%", "previous": "6.4%"},
                  {"time_jst": "08:30", "country": "JPY", "name": "家計支出", "forecast": "-3.5%", "previous": "-3.6%"},
                  {"time_jst": "29:00", "country": "USD", "name": "コリンズ連銀総裁の発言", "forecast": "—", "previous": "—"},
                  {"time_jst": "23:00", "country": "USD", "name": "ミシガン大 速報", "forecast": "47.5", "previous": "47.8"},
                  {"time_jst": "23:00", "country": "USD", "name": "ミシガン大 速報", "forecast": "47.6", "previous": "48.1"}]
        text = oneshot.handover_text(events)
        self.assertIn("アジア時間帯: 08:30 日本家計支出（予想-3.5%／前回-3.6%）。", text)
        self.assertIn("29:00 米国コリンズ連銀総裁の発言", text)
        self.assertNotIn("コリンズ連銀総裁の発言（", text)  # blank forecast/previous are not printed
        self.assertIn("予想47.5／前回47.8", text)  # conflicting sources are both shown, never merged
        self.assertIn("予想47.6／前回48.1", text)
        self.assertLess(text.index("08:30"), text.index("21:30"))
        self.assertEqual(oneshot.handover_text([]), "本日の主要予定は予定表にない。")

    def test_focus_ranking_sentence_carries_its_computation_time(self):
        ranking = {"generated_at_jst": "2026-10-08T08:39+09:00",
                   "rankings": [{"pair": "EUR/USD", "rank": 1, "score": 97, "verdict": "最適", "direction": "下降", "adx_h4": 35.8}]}
        self.assertEqual(oneshot.ranking_sentence(ranking, "EUR/USD"),
                         "デイトレ適性ランキング（10月8日08:39時点の算出）で1位のEUR/USD（スコア97、最適、方向下降、ADX 35.8）。")

    def test_story_and_topics_never_receive_the_ranking(self):
        material, calendar, ranking = self.inputs()
        seen = {}

        def calls(out, label, task, data, schema, *rest):
            seen[label] = "ranking_top5" in data
            return canned(out, label, task, data, schema)

        with tempfile.TemporaryDirectory() as folder, patch.object(oneshot, "call", side_effect=calls):
            out = Path(folder) / "oneshot"
            out.mkdir()
            (out / "policy.json").write_text((RUN / "policy.json").read_text(encoding="utf-8"), encoding="utf-8")
            oneshot.generate(out, date(2026, 9, 30), material, calendar, ranking, json.loads((out / "policy.json").read_text(encoding="utf-8")))
            sections = json.loads((out / "sections.json").read_text(encoding="utf-8"))
        self.assertEqual((seen["oneshot-1-story"], seen["oneshot-2-topics"], seen["oneshot-3-today"]), (False, False, True))
        self.assertIn("時点の算出）で", sections["focus_body"])

    def test_interpretive_sections_are_assembled_from_chosen_ids_only(self):
        material, calendar, ranking = self.inputs()
        views = [f for f in material if oneshot.is_view(f)]
        themes = [f for f in material if oneshot.is_theme(f)]
        self.assertTrue(views and themes)
        view, theme = views[0], themes[0]

        def calls(out, label, task, data, schema, *rest):
            if label.endswith("today"):
                pair = data["ranking_top5"][0]["pair"]
                enum = schema["properties"]["point_ids"]["items"]["enum"]
                self.assertIn(view["fact_id"], enum)
                self.assertIn("e1", enum)
                return {"focus_pair": pair, "focus_view_id": view["fact_id"], "risk_view_ids": [view["fact_id"], "N999"],
                        "point_ids": [theme["fact_id"], "e1", "e99999", view["fact_id"]], "key_event_nos": [1, 2]}
            return canned(out, label, task, data, schema)

        with tempfile.TemporaryDirectory() as folder, patch.object(oneshot, "call", side_effect=calls):
            out = Path(folder)
            (out / "policy.json").write_text((RUN / "policy.json").read_text(encoding="utf-8"), encoding="utf-8")
            oneshot.generate(out, date(2026, 9, 30), material, calendar, ranking, json.loads((out / "policy.json").read_text(encoding="utf-8")))
            sections = json.loads((out / "sections.json").read_text(encoding="utf-8"))
        self.assertEqual(sections["risk_body"], oneshot.sentence(view))  # unknown id dropped, text is the extracted fact
        self.assertEqual(sections["points"][0]["body"], oneshot.sentence(theme))
        self.assertEqual(sections["points"][1]["body"], "本日の予定: " + oneshot.event_label(calendar["events"][0]) + "。")
        self.assertEqual(len(sections["points"]), 3)  # out-of-range id dropped, then filled from today's key schedule
        self.assertEqual(len({p["body"] for p in sections["points"]}), 3)
        self.assertRegex(sections["risk_level"], r"^高重要度予定 \d+件$")
        pair_ok = sections["focus_pair"] in (view.get("pairs") or [])
        self.assertEqual(oneshot.sentence(view) in sections["focus_body"], pair_ok)  # a view about other pairs is not attached

    def test_join_facts_drops_a_repeated_lead_in_but_keeps_the_first(self):
        a = {"fact": "2026年10月8日のニューヨーク外国為替市場で、ドル円は157.88円で終えた。"}
        b = {"fact": "2026年10月8日のニューヨーク外国為替市場で、ユーロ円は177.01円で終えた。"}
        c = {"fact": "2026年10月8日、トランプ氏が発言した。"}
        d = {"fact": "米・先週分新規失業保険申請件数は19.7万件となった。"}
        self.assertEqual(oneshot.join_facts([a, b, c, d]),
                         "2026年10月8日のニューヨーク外国為替市場で、ドル円は157.88円で終えた。ユーロ円は177.01円で終えた。"
                         "2026年10月8日、トランプ氏が発言した。米・先週分新規失業保険申請件数は19.7万件となった。")

    def test_join_facts_treats_spelling_variants_as_one_lead_in_but_not_another_market(self):
        a = {"fact": "2026年10月8日のNY外為市場で、原油は93.20ドルまで上昇した。"}
        b = {"fact": "2026年10月8日のニューヨーク外国為替市場で、原油は90.21ドルまで反落した。"}
        c = {"fact": "2026年10月8日の欧州市場で、ユーロは売られた。"}
        self.assertEqual(oneshot.join_facts([a, b, c]),
                         "2026年10月8日のNY外為市場で、原油は93.20ドルまで上昇した。原油は90.21ドルまで反落した。"
                         "2026年10月8日の欧州市場で、ユーロは売られた。")

    def test_join_sourced_names_a_run_from_one_article_once(self):
        f = lambda t, s: {"fact": t, "source_title": s}
        self.assertEqual(oneshot.join_sourced([f("甲。", "A"), f("乙。", "A"), f("丙。", "B")]), "甲。 乙。（出典: A） 丙。（出典: B）")

    def test_topics_are_built_from_chosen_facts_without_reuse_across_topics(self):
        material, calendar, ranking = self.inputs()
        events = [f for f in material if f["fact_id"].startswith("N") and not oneshot.is_view(f) and not oneshot.is_theme(f)]
        views = [f for f in material if oneshot.is_view(f)]
        a, b, c = events[0], events[1], events[2]

        def calls(out, label, task, data, schema, *rest):
            if label.endswith("topics"):
                self.assertIn(a["fact_id"], schema["properties"]["topics"]["items"]["properties"]["fact_ids"]["items"]["enum"])
                self.assertNotIn(views[0]["fact_id"], schema["properties"]["topics"]["items"]["properties"]["fact_ids"]["items"]["enum"])
                return {"topics": [{"title": "甲", "fact_ids": [a["fact_id"], b["fact_id"], "NOPE"]},
                                   {"title": "乙", "fact_ids": [b["fact_id"], c["fact_id"]]},
                                   {"title": "丙", "fact_ids": [b["fact_id"]]}],
                        "market_view_ids": [views[0]["fact_id"], "X"]}
            return canned(out, label, task, data, schema)

        with tempfile.TemporaryDirectory() as folder, patch.object(oneshot, "call", side_effect=calls):
            out = Path(folder)
            (out / "policy.json").write_text((RUN / "policy.json").read_text(encoding="utf-8"), encoding="utf-8")
            oneshot.generate(out, date(2026, 9, 30), material, calendar, ranking, json.loads((out / "policy.json").read_text(encoding="utf-8")))
            sections = json.loads((out / "sections.json").read_text(encoding="utf-8"))
        self.assertEqual([t["title"] for t in sections["topics"]], ["甲", "乙"])  # "丙" had only an already-used fact
        self.assertEqual(sections["topics"][0]["body"], oneshot.join_facts([a, b]))
        self.assertEqual(sections["topics"][1]["body"], oneshot.join_facts([c]))
        self.assertEqual(sections["market"], oneshot.sentence(views[0]))

    def test_assembled_sections_are_never_sent_to_repair(self):
        material, calendar, ranking = self.inputs()
        issue = {"status": "ok", "issues": [{"section": "risk", "excerpt": "x", "kind": "取り違え", "reason": "x"},
                                            {"section": "point0", "excerpt": "x", "kind": "取り違え", "reason": "x"}]}

        def calls(out, label, task, data, schema, *rest):
            self.assertFalse(label.endswith("repair"))
            return canned(out, label, task, data, schema)

        with tempfile.TemporaryDirectory() as folder, patch.object(oneshot, "call", side_effect=calls), patch.object(
                oneshot.external_review, "review", return_value=issue):
            out = Path(folder)
            (out / "policy.json").write_text((RUN / "policy.json").read_text(encoding="utf-8"), encoding="utf-8")
            checks = oneshot.generate(out, date(2026, 9, 30), material, calendar, ranking, json.loads((out / "policy.json").read_text(encoding="utf-8")))
        self.assertNotIn("repaired_sections", checks)

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
                return {"fixes": [{"section": "summary", "text": "直した要約。"}]}
            return canned(out, label, task, data, schema)

        reviews = []

        def reviewer(out, data, texts):
            reviews.append(dict(texts))
            return {"status": "ok", "issues": [{"section": "summary", "excerpt": "要約。", "kind": "取り違え", "reason": "指標名が違う"}]}

        with tempfile.TemporaryDirectory() as folder, patch.object(oneshot, "call", side_effect=calls), patch.object(
                oneshot.external_review, "review", side_effect=reviewer):
            out = Path(folder)
            (out / "policy.json").write_text((RUN / "policy.json").read_text(encoding="utf-8"), encoding="utf-8")
            checks = oneshot.generate(out, date(2026, 9, 30), material, calendar, ranking,
                                      json.loads((out / "policy.json").read_text(encoding="utf-8")))
        self.assertTrue(any("指標名が違う" in p["reason"] and p["sections"] == ["summary"] for p in seen["problems"]))
        self.assertEqual(checks["repaired_sections"], ["summary"])
        self.assertEqual(reviews[0]["summary"], "要約。")      # first review sees the draft
        self.assertEqual(reviews[1]["summary"], "直した要約。")  # second review sees the repaired text
        self.assertIn("external_review_after", checks)

    def test_cut_off_repair_keeps_the_draft_and_the_report(self):
        material, calendar, ranking = self.inputs()

        def calls(out, label, task, data, schema, *rest):
            if label.endswith("repair"):
                self.assertEqual(rest, (30000,))  # thinking alone used 12000 on 2026-10-06
                raise ValueError("oneshot-5-repair: wrong model or incomplete response (length)")
            return canned(out, label, task, data, schema)

        issue = {"status": "ok", "issues": [{"section": "summary", "excerpt": "要約。", "kind": "取り違え", "reason": "x"}]}
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
