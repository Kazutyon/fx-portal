import json
import tempfile
import unittest
from datetime import date, datetime, timezone
from pathlib import Path

import local_fx_quotes as quotes


def chart(days_closes, offset=-14400):
    return {"meta": {"gmtoffset": offset},
            "timestamp": [int(datetime(2026, 10, d, 16, tzinfo=timezone.utc).timestamp()) for d, _ in days_closes],
            "indicators": {"quote": [{"close": [c for _, c in days_closes]}]}}


class QuoteTests(unittest.TestCase):
    def test_uses_last_session_before_the_report_date_with_change(self):
        bars = quotes.daily_bars(chart([(22, 52867.98), (23, 52215.16), (26, 52361.6), (27, 52500.0)]))
        fact = quotes.quote_fact("NYダウ", "ドル", 2, bars, date(2026, 10, 27), "^DJI", 0)
        self.assertIn("2026-10-26", fact["fact"])
        self.assertIn("52,361.60ドル", fact["fact"])
        self.assertIn("146.44ドル(+0.28％)上昇", fact["fact"])
        self.assertEqual(fact["fact_id"], "Q0")

    def test_falling_close_and_missing_values(self):
        bars = quotes.daily_bars(chart([(22, 4060.4), (23, None), (26, 4007.9)]))
        fact = quotes.quote_fact("金先物(1オンス)", "ドル", 1, bars, date(2026, 10, 27), "GC=F", 4)
        self.assertIn("52.5ドル(-1.29％)下落", fact["fact"])

    def test_one_failing_symbol_does_not_drop_the_others(self):
        def fetch(symbol):
            if symbol == "GC=F":
                raise OSError("down")
            return chart([(22, 100.0), (23, 101.0), (26, 102.0)])
        facts = quotes.build(date(2026, 10, 27), fetch)
        self.assertEqual(len(facts), len(quotes.INSTRUMENTS) - 1)

    def test_saved_file_is_reused(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            first = quotes.load(out, date(2026, 10, 27), lambda s: chart([(22, 1.0), (23, 2.0), (26, 3.0)]))
            again = quotes.load(out, date(2026, 10, 27), lambda s: (_ for _ in ()).throw(OSError("no network")))
            self.assertEqual(first, again)
            self.assertTrue(json.loads((out / "quotes.json").read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main()
