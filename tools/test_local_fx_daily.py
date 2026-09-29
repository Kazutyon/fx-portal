"""keep: deterministic daily-report gates; no network or model calls."""
import json
import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch

import local_fx_daily as daily


class DailyTests(unittest.TestCase):
    def test_editorial_pool_keeps_accepted_fact_not_selected_for_news(self):
        import local_fx_grounding as grounding
        facts = [{"fact_id": "N0-0", "claim_gate_accepted": True, "event_scope": "previous"},
                 {"fact_id": "N0-1", "claim_gate_accepted": True, "event_scope": "previous"},
                 {"fact_id": "N0-2", "claim_gate_accepted": False, "event_scope": "previous"},
                 {"fact_id": "N0-3", "claim_gate_accepted": True, "event_scope": "unknown"}]
        result = grounding.editorial_facts({"events": [], "day_themes": ""}, {"rankings": []},
                                           facts, [{"claim_ids": ["N0-0"]}])
        self.assertEqual([x["fact_id"] for x in result], ["N0-0", "N0-1"])

    def test_shared_selection_scans_every_batch_and_loads_originals_by_id(self):
        import local_fx_grounding as grounding
        facts = [{"fact_id": f"N{i}", "fact": "材料" * 800, "record_type": "actual",
                  "event_scope": "previous", "quote": "原文", "source_context": {"full": "文脈"}}
                 for i in range(4)]
        def choose(out, label, task, data, schema):
            self.assertNotIn("quote", data["facts"][0])
            return {"fact_ids": [data["facts"][-1]["fact_id"]]}
        with tempfile.TemporaryDirectory() as folder, patch.object(daily, "infer_cached", side_effect=choose) as infer:
            selected = grounding.shared_role_evidence(daily, Path(folder), "market", facts, date(2026, 9, 29))
            self.assertGreater(infer.call_count, 1)
            self.assertIn(facts[-1], selected)
            self.assertTrue(all("source_context" in x for x in selected))

    def test_shared_selection_rejects_invalid_ids(self):
        import local_fx_grounding as grounding
        with tempfile.TemporaryDirectory() as folder, patch.object(daily, "infer_cached", return_value={"fact_ids": ["invalid"]}):
            with self.assertRaisesRegex(ValueError, "invalid fact ID"):
                grounding.shared_role_evidence(daily, Path(folder), "market",
                    [{"fact_id": "N0", "fact": "金利", "record_type": "actual"}], date(2026, 9, 29))

    def test_editorial_quality_failure_is_not_source_pass(self):
        import local_fx_grounding as grounding
        draft = {"title": "引継ぎ", "body": "13時半にRBA。", "review": {"verdict": "PASS"}}
        with tempfile.TemporaryDirectory() as folder, patch.object(daily, "infer_cached",
                return_value={"verdict": "FAIL", "reason": "予定のみで判断条件がない"}):
            result = grounding.review_editorial_quality(daily, Path(folder), "handover", draft, [], {}, date(2026, 9, 29))
            self.assertEqual(result["verdict"], "FAIL")
            self.assertEqual(draft["review"]["verdict"], "PASS")

    def test_material_coverage_failure_keeps_unused_evidence(self):
        import local_fx_grounding as grounding
        with tempfile.TemporaryDirectory() as folder, patch.object(daily, "infer_cached",
                return_value={"verdict": "FAIL", "reason": "主要金利材料が未使用"}):
            result = grounding.material_coverage(daily, Path(folder),
                [{"fact_id": "N0", "fact": "米金利上昇", "event_scope": "previous"}], [], {}, date(2026, 9, 29))
            self.assertEqual(result["verdict"], "FAIL")
            self.assertEqual(result["unused_fact_ids"], ["N0"])

    def test_supplement_preserves_ids_and_excludes_today_afternoon(self):
        import hashlib
        adapter = daily.claude_sources
        sources = [{"source_id": 0, "source_url": "https://fx.minkabu.jp/news/1", "sha256": "original"}]
        index = '<a href="/news/2">米金利</a><a href="/news/3">東京市場</a>'
        def article(url, body):
            return {"source_url": url, "published_at": "2026-09-29T05:00:00+09:00" if url.endswith("2")
                    else "2026-09-29T12:00:00+09:00", "sha256": hashlib.sha256(url.encode()).hexdigest()}
        with tempfile.TemporaryDirectory() as folder, patch.object(adapter, "INDEXES", [adapter.INDEXES[1]]), \
                patch.object(adapter, "article", side_effect=article):
            out = Path(folder)
            daily.news.save(out / "source-bundle.json", {"sources": sources, "date_jst": "2026-09-29"})
            result = adapter.supplement_previous(date(2026, 9, 29), out,
                lambda out, label, url: index if url.endswith("/news") else "body", sources)
            self.assertEqual([x["source_id"] for x in result], [0, 1])
            self.assertTrue(result[1]["source_url"].endswith("2"))

    def test_large_evidence_is_split_without_loss(self):
        records = [{"source_id": i, "fact": "材料" * 90, "quote": "根拠" * 70} for i in range(40)]
        batches = daily.evidence_batches(records)
        self.assertGreater(len(batches), 1)
        self.assertEqual([item for group in batches for item in group], records)
        self.assertTrue(all(len(json.dumps(group, ensure_ascii=False).encode()) <= 12000 for group in batches))

    def test_quote_context_keeps_tokyo_opening_after_selection(self):
        import local_fx_grounding as grounding
        source = {"source_id": 0, "title": "東京市場", "source_url": "https://test.example/0",
                  "published_at": "2026-09-29T12:59:00+09:00",
                  "text": "29日午前の東京市場でドル・円は反落。米長期金利と原油相場の下げ渋りによるドルの買戻しで一時157円58銭まで上昇。"}
        claim = {"kind": "cause", "fact": "金利と原油が下げ渋りドル買戻し。",
                 "quote": "米長期金利と原油相場の下げ渋りによるドルの買戻しで一時157円58銭まで上昇。",
                 "event_scope": "previous", "market_session": "NY", "pairs": ["USD/JPY"], "record_type": "actual"}
        bound = grounding.bind_claim(source, claim, 0, date(2026, 9, 29))
        self.assertEqual(bound["event_scope"], "current")
        self.assertEqual(bound["market_session"], "Tokyo")
        self.assertIn("29日午前の東京市場", bound["source_context"]["article_opening"])
        self.assertEqual(bound["event_date"], "2026-09-29")

    def test_tokyo_only_statement_cannot_claim_ny(self):
        import local_fx_grounding as grounding
        facts = [{"fact_id": "N0-0", "market_session": "Tokyo", "record_type": "actual"}]
        copy = {"title": "値動き", "statements": [{"text": "NY時間に157.58円へ上昇。",
                "fact_ids": ["N0-0"], "mode": "fact"}]}
        self.assertIn("Tokyo-only facts assigned to NY", grounding.copy_errors(copy, facts, date(2026, 9, 29)))

    def test_last_week_is_not_previous_day(self):
        import local_fx_grounding as grounding
        quote = "先週前半、メキシコペソ円は原油高騰や高金利魅力を受け、9.40円台で推移していた。"
        source = {"source_id": 5, "title": "週のまとめ", "source_url": "https://test.example/5",
                  "published_at": "2026-09-29T13:05:00+09:00", "text": quote}
        claim = {"kind": "price", "fact": quote, "quote": quote,
                 "event_scope": "previous", "market_session": "unspecified", "pairs": ["MXN/JPY"], "record_type": "actual"}
        self.assertEqual(grounding.bind_claim(source, claim, 0, date(2026, 9, 29))["event_scope"], "historical")

    def test_last_week_theme_prefix_overrides_stale_heading(self):
        import local_fx_grounding as grounding
        quote = "トランプ大統領の懸念表明により、ドル円の160円ラインが市場に強烈に意識された。"
        source = {"source_id": 5, "title": "メキシコペソ円", "source_url": "https://test.example/5",
                  "published_at": "2026-09-29T13:05:00+09:00",
                  "text": "■ 値動き（9月28日〜足元） 日本・米国側：先週最大のテーマは円安牽制である。" + quote}
        claim = {"kind": "event", "fact": quote, "quote": quote, "event_scope": "previous",
                 "market_session": "unspecified", "pairs": ["USD/JPY"], "record_type": "actual"}
        self.assertEqual(grounding.bind_claim(source, claim, 0, date(2026, 9, 29))["event_scope"], "historical")

    def test_opening_cannot_be_reextracted_as_chunk_quote(self):
        import local_fx_grounding as grounding
        quote = "ロンドン時間には三村財務官の発言に敏感に反応し、円高が強まった。"
        chunk = "一方で、英国では初の予算発表が消費者心理を冷やすとアナリストが指摘した。"
        source = {"source_id": 4, "title": "NY概況", "source_url": "https://test.example/4",
                  "published_at": "2026-09-29T05:50:00+09:00", "text": quote + chunk}
        claim = {"kind": "event", "fact": quote, "quote": quote,
                 "event_scope": "previous", "market_session": "London", "pairs": ["USD/JPY"], "record_type": "actual"}
        with tempfile.TemporaryDirectory() as folder, patch.object(daily, "source_chunks", return_value=[chunk]), patch.object(daily, "infer_cached", return_value={"claims": [claim]}) as infer:
            with self.assertRaisesRegex(ValueError, "previous-session facts insufficient"):
                grounding.extract(daily, [source], date(2026, 9, 29), Path(folder))
            self.assertEqual(infer.call_count, 1)

    def test_us_country_cannot_be_added_to_unlabelled_mexican_release(self):
        import local_fx_grounding as grounding
        quote = "今週の主な指標 09/28 21:00 貿易収支 （8月） 結果 6.054億ドル 予想 15.3億ドル 前回 -8.475億ドル"
        source = {"source_id": 5, "title": "メキシコペソ円のまとめ", "source_url": "https://test.example/5",
                  "published_at": "2026-09-29T13:05:00+09:00", "text": "メキシコペソ円は下落。" + quote}
        claim = {"kind": "event", "fact": "米国の8月貿易収支は6.054億ドルとなった。", "quote": quote,
                 "event_scope": "previous", "market_session": "unspecified", "pairs": [], "record_type": "actual"}
        with self.assertRaisesRegex(ValueError, "country.*not grounded"):
            grounding.bind_claim(source, claim, 0, date(2026, 9, 29))

    def test_invalid_fact_id_is_rejected_before_model_review(self):
        import local_fx_grounding as grounding
        copy = {"title": "test", "statements": [{"text": "test", "fact_ids": ["nonexistent"], "mode": "fact"}]}
        with tempfile.TemporaryDirectory() as folder, patch.object(daily, "infer_cached", side_effect=AssertionError("must not call model")):
            qc = grounding.review_copy(daily, Path(folder), "review", copy, [], date(2026, 9, 29))
            self.assertEqual(qc["verdict"], "FAIL")

    def test_forecast_cannot_be_reported_as_realized_fact(self):
        import local_fx_grounding as grounding
        facts = [{"fact_id": "C0", "record_type": "forecast"}]
        copy = {"title": "RBA", "statements": [{"text": "RBAが利上げした。",
                "fact_ids": ["C0"], "mode": "fact"}]}
        self.assertIn("forecast/outlook written as realized fact", grounding.copy_errors(copy, facts, date(2026, 9, 29)))
        copy["statements"][0]["text"] = "13:30にRBA政策金利発表予定。予想は25bp利上げ。"
        self.assertEqual(grounding.copy_errors(copy, facts, date(2026, 9, 29)), [])

    def test_month_end_day_error_is_rejected(self):
        import local_fx_grounding as grounding
        facts = [{"fact_id": "D0", "fact": "明日9月30日が最後の営業日", "record_type": "outlook"}]
        copy = {"title": "本日", "statements": [{"text": "本日は最終営業日翌日。",
                "fact_ids": ["D0"], "mode": "conditional"}]}
        self.assertIn("today contradicts source month-end date", grounding.copy_errors(copy, facts, date(2026, 9, 29)))

    def test_forecast_mode_normalization_does_not_change_text(self):
        import local_fx_grounding as grounding
        text = "本日13:30にRBA政策金利が25bp利上げされ4.60%になる見込み。"
        copy = {"title": "本日", "statements": [{"text": text, "fact_ids": ["C3"], "mode": "conditional"}]}
        normalized = grounding.normalize_modes(copy, [{"fact_id": "C3", "record_type": "forecast"}])
        self.assertEqual(normalized["statements"][0]["mode"], "reported_forecast")
        self.assertEqual(normalized["statements"][0]["text"], text)

    def test_short_ny_price_quote_keeps_context_and_previous_session(self):
        import local_fx_grounding as grounding
        quote = "ユーロドルは１．１３ドル台で振幅。"
        source = {"source_id": 4, "title": "ドル円＝ＮＹ為替概況", "source_url": "https://test.example/4",
                  "published_at": "2026-09-29T05:50:00+09:00",
                  "text": "きょうのＮＹ為替市場。" + quote + "下げ止まってはいるものの買い戻す気配はない。"}
        claim = {"kind": "price", "fact": quote, "quote": quote, "event_scope": "current",
                 "market_session": "NY", "pairs": ["EUR/USD"], "record_type": "actual"}
        bound = grounding.bind_claim(source, claim, 0, date(2026, 9, 29))
        self.assertEqual(bound["event_date"], "2026-09-28")
        self.assertGreaterEqual(len(bound["quote"]), 20)
        self.assertIn(bound["quote"], source["text"])
        self.assertEqual(bound["fact"], quote)

    def test_rounding_compatibility_is_not_a_blanket_tolerance(self):
        self.assertEqual(daily.numeric_agreement("7228千件", "7.23M"), "rounding-compatible")
        self.assertEqual(daily.numeric_agreement("7271千件", "7.27M"), "rounding-compatible")
        self.assertEqual(daily.numeric_agreement("56.1千件", "56K"), "rounding-compatible")
        self.assertEqual(daily.numeric_agreement("89.1", "89.2"), "conflict")
        self.assertEqual(daily.numeric_agreement("7.23M", "7.24M"), "conflict")

    def test_weekly_schedule_keeps_dates_not_navigation(self):
        text = "▼ 9月28日(月) 昨日の予定 ▼ 9月29日(火) RBA ▼ 9月30日(水) ADP雇用統計 ▼ 10月1日(木) ISM製造業 ▼ 10月2日(金) 雇用統計 通知機能付きアプリ ★ 今週の為替相場の焦点 リンク広告"
        weekly = daily.weekly_schedule(text, date(2026, 9, 29))
        self.assertIn("9月30日(水) ADP", weekly)
        self.assertIn("10月1日(木) ISM", weekly)
        self.assertNotIn("9月28日", weekly)
        self.assertNotIn("アプリ", weekly)
        self.assertNotIn("広告", weekly)

    def test_reviewer_receives_original_context_not_only_generated_fact(self):
        import local_fx_grounding as grounding
        fact = {"fact_id": "N4-0", "record_type": "actual", "market_session": "London",
                "quote": "ロンドン時間には三村財務官の発言に敏感に反応し、円高が強まった。",
                "source_context": {"article_opening": "きょうのNY、ロンドンの下げを取り戻した"}}
        copy = {"title": "三村発言", "statements": [{"text": "ロンドンで発言に反応。",
                "fact_ids": ["N4-0"], "mode": "fact"}]}
        with tempfile.TemporaryDirectory() as folder, patch.object(daily, "infer_cached", return_value={"verdict": "PASS", "reason": "mock"}) as infer:
            grounding.review_copy(daily, Path(folder), "review", copy, [fact], date(2026, 9, 29))
            data = infer.call_args.args[3]
            self.assertEqual(data["original_evidence"][0]["source_context"], fact["source_context"])
            self.assertEqual(data["date_facts"]["previous_session_date"], "2026-09-28")
            self.assertNotIn("mode", data["draft"]["statements"][0])

    def test_author_does_not_accept_failed_repair(self):
        import local_fx_grounding as grounding
        fact = {"fact_id": "N4-0", "record_type": "actual"}
        copy = {"title": "test", "statements": [{"text": "test", "fact_ids": ["N4-0"], "mode": "fact"}]}
        values = [copy, {"verdict": "FAIL", "reason": "bad"}, copy, {"verdict": "FAIL", "reason": "still bad"}]
        with tempfile.TemporaryDirectory() as folder, patch.object(daily, "infer_cached", side_effect=values):
            with self.assertRaisesRegex(ValueError, "after one repair"):
                grounding.author(daily, Path(folder), "topic", "test", [fact], date(2026, 9, 29), "10")

    def test_case_shiller_year_and_month_are_not_merged(self):
        self.assertEqual(daily.event_code("S&P/CS Composite-20 HPI y/y"), "case-shiller-yy")
        self.assertEqual(daily.event_code("S＆P/ケース・シラー住宅価格指数 [前年比]"), "case-shiller-yy")
        self.assertNotEqual(daily.event_code("GDP [前月比]"), daily.event_code("GDP [前年比]"))

    def test_rowspans_preserve_second_measure_and_next_day(self):
        page = '''<table><tr><td rowspan="2">22:00</td>
        <td class="title" rowspan="2">米)ケース・シラー住宅価格指数 [前月比/前年比]</td>
        <td class="rank" rowspan="2"><div class="icon-bb"></div></td><td>+0.20%</td><td>+0.24%</td></tr>
        <tr><td>+2.20%</td><td>+2.10%</td></tr>
        <tr><td>28:00</td><td class="bg-yellow title">米)ウォラーFRB理事の発言</td><td class="rank"></td></tr></table>'''
        events = daily.parse_kiss(page, date(2026, 9, 29))
        self.assertEqual(len(events), 3)
        self.assertEqual(events[0]["forecast"], "+0.20%")
        self.assertEqual(events[1]["forecast"], "+2.20%")
        self.assertIn("前年比", events[1]["name"])
        self.assertEqual(events[2]["datetime_jst"], "2026-09-30T04:00:00+09:00")

    def test_completed_collection_cache_does_not_access_web(self):
        with tempfile.TemporaryDirectory() as folder:
            out = Path(folder)
            import hashlib
            sources = [{"source_id": i, "source_url": f"https://test.example/{i}", "title": "test",
                        "published_at": "2026-09-29T06:00:00+09:00", "text": "test",
                        "sha256": hashlib.sha256(b"test").hexdigest()} for i in range(5)]
            daily.news.save(out / "source-bundle.json", {"date_jst": "2026-09-29", "sources": sources})
            with patch.object(daily, "fetch", side_effect=AssertionError("unexpected network")):
                self.assertEqual(daily.collect_news(date(2026, 9, 29), out), sources)

    def test_units_are_normalized_without_float_rounding(self):
        self.assertEqual(daily.numeric_value("7228千件"), daily.numeric_value("7.228M"))
        self.assertEqual(daily.numeric_value("25bp 利上げ 4.60%"), daily.numeric_value("4.6%"))
        self.assertEqual(daily.numeric_value("±0.0%"), daily.numeric_value("0.0%"))

    def test_chunks_keep_all_source_spelling(self):
        text = ("重要な取引時間帯と価格の記述。" * 90) + "末尾の重要な中銀発言。"
        chunks = daily.source_chunks(text)
        self.assertEqual("".join(chunks), text)
        self.assertGreater(len(chunks), 1)

    def test_unapproved_automatic_sources_fail_without_request(self):
        with patch.object(daily, "mirror_enabled", return_value=False), patch.object(daily.urllib.request, "urlopen", side_effect=AssertionError("network forbidden")):
            for url in ["https://fx.minkabu.jp/news", "https://kissfx.com/article/test.html"]:
                with self.assertRaisesRegex(ValueError, "not approved"):
                    daily.fetch(url)

    def test_policy_inheritance_preserves_original_date_and_ignores_stance(self):
        with tempfile.TemporaryDirectory() as folder:
            out = Path(folder)
            currencies = ["USD", "GBP", "JPY", "EUR", "AUD", "NZD", "CAD", "CHF"]
            rows = ''.join(f'<tr><td>{c} bank</td><td>{c}</td><td><strong>1.25%</strong></td><td>要確認</td></tr>' for c in currencies)
            page = '<h3>主要中銀 政策金利</h3><span>2026-09-25 現在</span><table>' + rows + '</table>'
            daily.claude_sources.inherit_policy(date(2026, 9, 29), out, lambda *args: page)
            policy = daily.load(out / "policy.json")
            self.assertEqual(policy["source_as_of_jst"], "2026-09-25")
            self.assertEqual(len(policy["rates"]), 8)
            self.assertNotIn("要確認", json.dumps(policy))

    def test_monday_does_not_fake_inherited_policy_refresh(self):
        with self.assertRaisesRegex(ValueError, "Monday"):
            daily.claude_sources.inherit_policy(date(2026, 10, 5), Path("unused"), lambda *args: self.fail("unexpected request"))

    def test_cache_is_invalidated_when_prompt_changes(self):
        with tempfile.TemporaryDirectory() as folder:
            out = Path(folder)
            with patch.object(daily.news, "infer", side_effect=[{"body": "a"}, {"body": "b"}]) as infer:
                s = daily.news.schema({"body": daily.news.STRING})
                self.assertEqual(daily.infer_cached(out, "one", "first", {}, s)["body"], "a")
                self.assertEqual(daily.infer_cached(out, "one", "first", {}, s)["body"], "a")
                self.assertEqual(daily.infer_cached(out, "one", "changed", {}, s)["body"], "b")
                self.assertEqual(infer.call_count, 2)


if __name__ == "__main__":
    unittest.main()
