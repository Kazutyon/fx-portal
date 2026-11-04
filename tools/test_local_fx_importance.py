"""keep: importance signals, labels and the weight fit; no network or model calls."""
import json
import subprocess
import tempfile
import unittest
from datetime import date
from pathlib import Path

import local_fx_importance as imp


def fact(fact_id, text, source_id, **extra):
    return {"fact_id": fact_id, "fact": text, "source_id": source_id, "event_scope": "previous", "pairs": ["USD/JPY"],
            "record_type": "actual", "kind": "price", "source_url": "https://zai.diamond.jp/articles/-/1", **extra}


class ImportanceTests(unittest.TestCase):
    def test_articles_counts_the_other_articles_that_state_the_same_figure(self):
        material = [fact("N0-0", "ドル円の終値は158.69円だった。", 0),
                    fact("N1-0", "ドル円は続伸し158.69円で引けた。", 1),
                    fact("N2-3", "ドル円は158.69円で終えた。", 2, source_context={"also_stated_in": ["別記事"]}),
                    fact("N3-0", "ユーロドルは1.1193ドルだった。", 3)]
        sig = imp.signals(material)
        self.assertEqual(sig["N0-0"]["repeat"], 2)
        self.assertEqual(sig["N0-0"]["articles"], 3)
        self.assertEqual(sig["N2-3"]["outlets"], 2)  # a merged duplicate counts as another outlet
        self.assertEqual(sig["N3-0"]["articles"], 1)

    def test_surprise_needs_both_actual_and_forecast_in_the_sentence(self):
        self.assertAlmostEqual(imp.surprise("米9月JOLTS求人件数は752.3万件と予想716.4万件を上回った。"), 0.05, places=2)
        self.assertEqual(imp.surprise("ドル円は158円台まで上昇した。"), 0.0)

    def test_label_is_decided_by_the_figures_and_unknown_without_any(self):
        page = imp.norm("ドル円は158.69円で引け、ユーロ円は177.62円だった。")
        self.assertTrue(imp.in_text(fact("N0-0", "ドル円の終値は158.69円。", 0), page))
        self.assertFalse(imp.in_text(fact("N0-1", "ポンド円は213.05円まで上昇。", 0), page))
        self.assertIsNone(imp.in_text(fact("N0-2", "市場は様子見だった。", 0), page))

    def test_build_day_writes_rows_with_features_and_labels(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            run = root / "run"
            (run / "oneshot").mkdir(parents=True)
            material = [fact("N0-0", "ドル円の終値は158.69円だった。", 0), fact("N0-1", "ポンド円は213.05円まで上昇した。", 0),
                        {"fact_id": "C1", "fact": "予定", "source_id": 9}]
            (run / "shared-material.json").write_text(json.dumps({"facts": material}), encoding="utf-8")
            (run / "oneshot" / "report.html").write_text("<p>ドル円は158.69円</p>", encoding="utf-8")
            published = root / "pub.html"
            published.write_text("<p>ドル円は158.69円で引けた</p>", encoding="utf-8")
            path = imp.build_day(run, date(2026, 11, 4), published, root)
            day = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual([r["id"] for r in day["rows"]], ["N0-0", "N0-1"])  # news facts only
        self.assertEqual([r["published"] for r in day["rows"]], [True, False])
        self.assertEqual([r["shadow"] for r in day["rows"]], [True, False])
        self.assertIn("log_articles", day["rows"][0]["f"])

    def test_fit_recovers_a_feature_that_drives_the_label(self):
        names = sorted(imp.features(fact("N0-0", "x158.69", 0), {"articles": 1, "outlets": 1, "repeat": 0}))
        days = []
        for d in range(10):
            rows = []
            for i in range(60):
                articles = 1 + (i % 5)
                f = imp.features(fact(f"N{i}-0", f"事実{i}は{150 + i}.5円", i), {"articles": articles, "outlets": 1, "repeat": articles - 1})
                rows.append({"id": f"N{i}-0", "articles": articles, "f": f, "published": articles >= 4, "shadow": None})
            days.append({"date": f"2026-10-{d + 1:02d}", "rows": rows})
        result = imp.fit(days)
        self.assertGreater(result["auc_test"], 0.9)
        self.assertEqual(next(iter(result["weights"])), "log_articles")
        self.assertIn("preview", result["status"])  # 10 days are too few to trust
        self.assertEqual(imp.fit(days[:2])["status"], "not enough days")
        self.assertTrue(names)

    def test_the_dataset_is_committed_and_pushed_without_touching_other_work(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            remote, work = base / "remote.git", base / "work"
            run = lambda *a, cwd=work: subprocess.run(["git", *a], cwd=cwd, check=True, capture_output=True, text=True)
            subprocess.run(["git", "init", "--bare", "-b", "main", str(remote)], check=True, capture_output=True)
            subprocess.run(["git", "clone", str(remote), str(work)], check=True, capture_output=True)
            run("config", "user.email", "t@example.com")
            run("config", "user.name", "t")
            (work / "other.txt").write_text("1", encoding="utf-8")
            run("add", "other.txt")
            run("commit", "-m", "base")
            run("push", "-u", "origin", "HEAD:main")
            self.assertEqual(imp.commit_and_push(work), "nothing new")
            (work / "data" / "importance").mkdir(parents=True)
            (work / "data" / "importance" / "2026-11-05.json").write_text("{}", encoding="utf-8")
            (work / "other.txt").write_text("changed by someone else", encoding="utf-8")  # unrelated work in progress
            self.assertEqual(imp.commit_and_push(work), "committed and pushed")
            files = run("show", "--name-only", "--format=", "HEAD").stdout.split()
            self.assertEqual(files, ["data/importance/2026-11-05.json"])  # only the dataset is in the commit
            self.assertEqual((work / "other.txt").read_text(encoding="utf-8"), "changed by someone else")
            self.assertIn("2026-11-05.json", run("ls-tree", "-r", "--name-only", "origin/main").stdout)
            (work / "data" / "importance" / "2026-11-06.json").write_text("{}", encoding="utf-8")
            run("remote", "set-url", "origin", str(base / "missing.git"))
            self.assertIn("push failed", imp.commit_and_push(work))  # offline: kept for the next time

    def test_auc_of_a_perfect_and_a_tied_ranking(self):
        self.assertEqual(imp.auc([0.1, 0.2, 0.8, 0.9], [0, 0, 1, 1]), 1.0)
        self.assertEqual(imp.auc([0.5, 0.5, 0.5, 0.5], [0, 1, 0, 1]), 0.5)


if __name__ == "__main__":
    unittest.main()
