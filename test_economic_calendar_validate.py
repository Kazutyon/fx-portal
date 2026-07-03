import unittest

from economic_calendar_forexfactory import normalize
from economic_calendar_validate import merge_feeds


class EconomicCalendarValidatorTests(unittest.TestCase):
    def test_normalizes_forex_factory_jst_events_for_target_date(self):
        result = normalize(
            [
                {
                    "title": "Employment Report",
                    "country": "USD",
                    "date": "2026-07-03T21:30:00+09:00",
                    "impact": "High",
                    "forecast": "100K",
                    "previous": "90K",
                },
                {
                    "title": "Other Day",
                    "country": "EUR",
                    "date": "2026-07-04T10:00:00+09:00",
                    "impact": "Low",
                    "forecast": "",
                    "previous": "",
                },
            ],
            "2026-07-03",
        )
        self.assertEqual(len(result["events"]), 1)
        self.assertEqual(result["events"][0]["time_jst"], "21:30")
        self.assertEqual(result["events"][0]["importance"], "high")

    def test_confirms_event_seen_by_two_sources(self):
        event = {
            "time_jst": "21:30",
            "country": "US",
            "name": "雇用統計",
            "importance": "high",
        }
        result = merge_feeds(
            [
                {"source": "source-a", "events": [event]},
                {"source": "source-b", "events": [dict(event)]},
            ],
            "2026-07-03",
        )
        self.assertTrue(result["publish_ready"])
        self.assertEqual(result["event_count"], 1)
        self.assertTrue(result["events"][0]["confirmed"])
        self.assertEqual(result["events"][0]["sources"], ["source-a", "source-b"])

    def test_warns_for_single_source(self):
        event = {
            "time_jst": "17:00",
            "country": "EU",
            "name": "ECB総裁発言",
            "importance": "medium",
        }
        result = merge_feeds([{"source": "source-a", "events": [event]}], "2026-07-03")
        self.assertFalse(result["publish_ready"])
        self.assertTrue(any("single source" in warning for warning in result["warnings"]))
        self.assertTrue(any("fewer than two" in warning for warning in result["warnings"]))

    def test_rejects_invalid_time(self):
        event = {
            "time_jst": "25:00",
            "country": "JP",
            "name": "テスト指標",
            "importance": "low",
        }
        result = merge_feeds(
            [
                {"source": "source-a", "events": [event]},
                {"source": "source-b", "events": []},
            ],
            "2026-07-03",
        )
        self.assertFalse(result["publish_ready"])
        self.assertTrue(any("invalid JST time" in error for error in result["errors"]))


if __name__ == "__main__":
    unittest.main()
