"""Regression checks for the observed silent-success and hindsight failures."""
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import local_fx_news as pilot


class PilotRegressionTests(unittest.TestCase):
    def result(self, content, **overrides):
        return {"model": pilot.MODEL, "done": True, "done_reason": "stop",
                "message": {"content": content}, **overrides}

    def infer_result(self, value, out):
        response = io.BytesIO(json.dumps(value).encode("utf-8"))
        with patch.object(pilot.urllib.request, "urlopen", return_value=response):
            return pilot.infer("test-extract", "test", {}, pilot.QC_SCHEMA, out)

    def test_no_reply_and_empty_are_failures(self):
        for text in ["NO_REPLY", "", "   "]:
            with self.subTest(text=text), tempfile.TemporaryDirectory() as folder:
                with self.assertRaisesRegex(ValueError, "empty/NO_REPLY"):
                    self.infer_result(self.result(text), Path(folder))

    def test_truncated_output_and_wrong_model_are_failures(self):
        text = '{"verdict":"PASS","reason":"test"}'
        for overrides in [{"done_reason": "length"}, {"model": "other"}]:
            with self.subTest(overrides=overrides), tempfile.TemporaryDirectory() as folder:
                with self.assertRaisesRegex(ValueError, "wrong model or incomplete"):
                    self.infer_result(self.result(text, **overrides), Path(folder))

    def test_request_has_fresh_messages_explicit_64k_and_no_tools(self):
        with tempfile.TemporaryDirectory() as folder:
            out = Path(folder)
            value = self.infer_result(self.result('{"verdict":"PASS","reason":"test"}'), out)
            request = json.loads((out / "test-extract.request.json").read_text(encoding="utf-8"))
            self.assertEqual(value["verdict"], "PASS")
            self.assertEqual(len(request["messages"]), 2)
            self.assertEqual(request["options"]["num_ctx"], 65536)
            self.assertNotIn("tools", request)

    def test_think_off_trial_preserves_model_context_and_output_limit(self):
        for think_off in [False, True]:
            with self.subTest(think_off=think_off), tempfile.TemporaryDirectory() as folder:
                out = Path(folder)
                response = io.BytesIO(json.dumps(self.result('{"verdict":"PASS","reason":"test"}')).encode())
                with patch.object(pilot, "FORCE_THINK_OFF", think_off), patch.object(pilot.urllib.request, "urlopen", return_value=response):
                    pilot.infer("test-write", "test", {}, pilot.QC_SCHEMA, out)
                request = json.loads((out / "test-write.request.json").read_text(encoding="utf-8"))
                self.assertEqual(request["model"], pilot.MODEL)
                self.assertEqual(request["options"]["num_ctx"], 65536)
                self.assertEqual(request["options"]["num_predict"], 6144)
                self.assertEqual(request["think"], not think_off)

    def test_writer_length_retries_once_with_same_model_thinking_and_preserves_first(self):
        first = self.result('{"verdict":', done_reason="length")
        second = self.result('{"verdict":"PASS","reason":"supported"}')
        with tempfile.TemporaryDirectory() as folder:
            out = Path(folder)
            responses = [io.BytesIO(json.dumps(value).encode()) for value in [first, second]]
            with patch.object(pilot.urllib.request, "urlopen", side_effect=responses) as urlopen:
                value = pilot.infer("topic-write", "test", {}, pilot.QC_SCHEMA, out)
            self.assertEqual(value["verdict"], "PASS")
            self.assertEqual(urlopen.call_count, 2)
            first_request = json.loads((out / "topic-write-output-limit-first.request.json").read_text(encoding="utf-8"))
            second_request = json.loads((out / "topic-write.request.json").read_text(encoding="utf-8"))
            self.assertEqual(first_request["options"]["num_predict"], 6144)
            self.assertEqual(second_request["options"]["num_predict"], 8192)
            self.assertEqual(first_request["messages"], second_request["messages"])
            self.assertEqual(first_request["model"], second_request["model"])
            self.assertTrue(second_request["think"])
            self.assertTrue((out / "topic-write-output-limit-first.response.json").exists())

    def test_writer_second_length_still_fails_closed(self):
        truncated = self.result('{"verdict":', done_reason="length")
        with tempfile.TemporaryDirectory() as folder:
            responses = [io.BytesIO(json.dumps(truncated).encode()) for _ in range(2)]
            with patch.object(pilot.urllib.request, "urlopen", side_effect=responses) as urlopen:
                with self.assertRaisesRegex(ValueError, "incomplete response"):
                    pilot.infer("topic-write", "test", {}, pilot.QC_SCHEMA, Path(folder))
            self.assertEqual(urlopen.call_count, 2)

    def test_visible_publication_time_controls_cutoff(self):
        page = '''<script type="application/ld+json">{
        "@type":"NewsArticle","headline":"test", "datePublished":"2026-09-29T06:55:00+09:00"
        }</script><time>2026/09/29(火) 07:17</time><p class="news__text">''' + ("試験資料。" * 50) + "</p>"
        source = pilot.article("https://fx.minkabu.jp/news/1", page)
        self.assertEqual(source["published_at"], "2026-09-29T07:17:00+09:00")
        self.assertNotEqual(source["published_at"], source["metadata_published_at"])

    def test_short_news_is_not_discarded_for_missing_length(self):
        page = '''<script type="application/ld+json">{
        "@type":"NewsArticle","headline":"test", "datePublished":"2026-09-29T01:40:00+09:00"
        }</script><time>2026/09/29(火) 01:45</time><p class="news__text">''' + ("試験資料。" * 25) + "</p>"
        source = pilot.article("https://fx.minkabu.jp/news/1", page)
        self.assertEqual(len(source["text"]), 125)


if __name__ == "__main__":
    unittest.main()
