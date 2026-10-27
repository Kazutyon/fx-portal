"""keep: the published-report check flags a close stated at an intraday high, and stays quiet on a correct close."""
import json
import tempfile
import unittest
from datetime import date
from pathlib import Path

import local_fx_published_check as pc


class PublishedCheckTests(unittest.TestCase):
    def run_check(self, sentence):
        with tempfile.TemporaryDirectory() as tmp:
            run = Path(tmp) / "run"
            (run / "sources").mkdir(parents=True)
            facts = [{"fact_id": "N0-0", "fact": "10/23のNYでドル円は終値は156.87円となった。", "kind": "event",
                      "event_scope": "previous", "pairs": ["USD/JPY"], "quote": "終値は156.87円", "source_context": {}, "published_at": ""},
                     {"fact_id": "N0-1", "fact": "ドル円は157.08円まで上昇した。", "kind": "event", "event_scope": "previous",
                      "pairs": ["USD/JPY"], "quote": "157.08円まで上昇", "source_context": {}, "published_at": ""}]
            (run / "shared-material.json").write_text(json.dumps({"facts": facts}, ensure_ascii=False), encoding="utf-8")
            page = Path(tmp) / "report.html"
            page.write_text(f"<html><body><p>{sentence}</p></body></html>", encoding="utf-8")
            return pc.check(page, run, date(2026, 10, 26))

    def test_intraday_high_reported_as_the_close_is_flagged(self):
        result = self.run_check("前営業日10/23（金）のドル円は156.30円まで下げた後、157.08円まで戻して引けた。")
        self.assertEqual(result["sentences_flagged"], 1)
        self.assertTrue(result["flagged"][0]["close_mismatch"])

    def test_close_value_reads_both_wordings(self):
        self.assertEqual(pc.close_value("ドル円は終値は156.87円となった。"), 156.87)
        self.assertEqual(pc.close_value("USD/JPYは157.50円で終値を付け、63銭高かった。"), 157.5)
        self.assertIsNone(pc.close_value("ドル円は157.08円まで上昇した。"))
        self.assertEqual(pc.close_value("ドル円は終値157.95円となり、前営業日NY終値157.50円から45銭高かった。"), 157.95)
        self.assertEqual(pc.close_value("前営業日NY終値157.50円と比べて高い。"), None)

    def test_sen_notation_equals_decimal_yen(self):
        import local_fx_grounding as grounding
        evidence = [{"quote": "ドル円は157円67銭から157円96銭まで上昇した。", "fact": "", "source_context": {}, "published_at": ""}]
        self.assertEqual(grounding.number_errors("ドル円は157.67円〜157.96円で推移した。", evidence, date(2026, 10, 28)), [])
        self.assertTrue(grounding.number_errors("ドル円は157.12円まで下げた。", evidence, date(2026, 10, 28)))

    def test_the_stated_close_is_not_flagged(self):
        result = self.run_check("前営業日10/23（金）のドル円は157.08円まで戻したが、引けは156.87円だった。")
        self.assertFalse(any(f["close_mismatch"] for f in result["flagged"]))


if __name__ == "__main__":
    unittest.main()
