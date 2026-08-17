import unittest

from economic_calendar_fred import normalize


class EconomicCalendarFredTests(unittest.TestCase):
    def test_emits_event_for_matching_employment_situation_date(self):
        release_dates = {50: ["2026-08-07"], 10: [], 46: [], 192: []}
        result = normalize(release_dates, "2026-08-07")
        self.assertEqual(len(result["events"]), 1)
        event = result["events"][0]
        self.assertEqual(event["name"], "Employment Situation")
        self.assertEqual(event["country"], "USD")
        self.assertEqual(event["importance"], "high")
        self.assertTrue(event["official"])
        self.assertEqual(event["time_jst"], "21:30")

    def test_no_events_when_target_date_not_in_any_release(self):
        release_dates = {50: ["2026-09-04"], 10: ["2026-09-11"], 46: [], 192: []}
        result = normalize(release_dates, "2026-08-07")
        self.assertEqual(result["events"], [])

    def test_converts_jolts_standard_release_time(self):
        release_dates = {50: [], 10: [], 46: [], 192: ["2026-08-04"]}
        result = normalize(release_dates, "2026-08-04")
        self.assertEqual(len(result["events"]), 1)
        self.assertEqual(result["events"][0]["time_jst"], "23:00")

    def test_multiple_matching_releases_on_same_date(self):
        release_dates = {50: ["2026-08-07"], 10: ["2026-08-07"], 46: [], 192: []}
        result = normalize(release_dates, "2026-08-07")
        names = sorted(event["name"] for event in result["events"])
        self.assertEqual(names, ["Consumer Price Index", "Employment Situation"])


if __name__ == "__main__":
    unittest.main()
