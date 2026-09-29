"""keep: configure only the existing GALLERIA FX cron, snapshot before/after."""
import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

import local_fx_news as news

JOB = "886af487-0b98-4068-a379-8868e804e29f"
CLI = [r"C:\Program Files\nodejs\node.exe", str(Path(os.environ["APPDATA"]) / "npm/node_modules/openclaw/openclaw.mjs")]


def command(*args):
    result = subprocess.run([*CLI, *args], capture_output=True, encoding="utf-8", check=True, timeout=45)
    return json.loads(result.stdout)


def job():
    return next(x for x in command("cron", "list", "--all", "--json")["jobs"] if x["id"] == JOB)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--record-runs", action="store_true")
    parser.add_argument("--evidence-dir", type=Path, required=True)
    args = parser.parse_args()
    if os.environ.get("COMPUTERNAME", "").upper() != "GALLERIA":
        raise ValueError("wrong host")
    out = args.evidence_dir.resolve()
    if not out.is_relative_to((news.ROOT / "shadow-output").resolve()):
        raise ValueError("evidence outside shadow-output")
    before = job()
    if args.record_runs:
        value = command("cron", "runs", "--id", JOB, "--limit", "10", "--json")
        news.save(out / "cron-run-history.json", value)
        print("saved FX-only cron execution history")
        return
    if before["name"] != "fx-portal-shadow-collect-0700":
        raise ValueError("unexpected job identity")
    backup = out / "cron-before.json"
    if not backup.exists():
        news.save(backup, before)
    if args.apply:
        argv = [sys.executable, "-u", str(news.ROOT / "tools/local_fx_daily.py")]
        command("cron", "edit", JOB, "--command-argv", json.dumps(argv),
                "--command-cwd", str(news.ROOT), "--timeout-seconds", "2400",
                "--no-output-timeout-seconds", "240", "--output-max-bytes", "65536",
                "--cron", "0 7 * * 1-5", "--tz", "Asia/Tokyo", "--exact", "--no-deliver",
                "--description", "GALLERIA full daily shadow; bounded fresh Qwen stages; no upload or fallback", "--json")
        after = job()
        news.save(out / "cron-after.json", after)
        if after["payload"]["kind"] != "command" or after["schedule"]["expr"] != "0 7 * * 1-5":
            raise ValueError("cron readback mismatch")
        print(json.dumps(after, ensure_ascii=True))
    else:
        print(json.dumps(before, ensure_ascii=True))


if __name__ == "__main__":
    main()
