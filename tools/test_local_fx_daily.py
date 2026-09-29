"""keep: deterministic daily-report gates; no network or model calls."""
import json
import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch

import local_fx_daily as daily


class DailyTests(unittest.TestCase):
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
        with patch.object(daily.urllib.request, "urlopen", side_effect=AssertionError("network forbidden")):
            for url in ["https://fx.minkabu.jp/news", "https://kissfx.com/article/test.html"]:
                with self.assertRaisesRegex(ValueError, "not approved"):
                    daily.fetch(url)

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
