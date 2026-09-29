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
