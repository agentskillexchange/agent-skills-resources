#!/usr/bin/env python3
"""Lightweight link checker for resources.json."""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def check(url: str, timeout: int) -> tuple[bool, str]:
    req = urllib.request.Request(url, headers={"User-Agent": "agent-skills-resources-link-check/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            status = getattr(resp, "status", 0)
            return 200 <= status < 400, str(status)
    except urllib.error.HTTPError as exc:
        return 300 <= exc.code < 400, str(exc.code)
    except Exception as exc:  # noqa: BLE001 - report concise network failures
        return False, type(exc).__name__


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--timeout", type=int, default=12)
    parser.add_argument("--skip-http", action="store_true", help="Validate URL shape only; do not fetch.")
    args = parser.parse_args()

    rows = json.loads((ROOT / "data" / "resources.json").read_text())
    urls: list[str] = []
    for row in rows:
        urls.append(row["url"])
        if row.get("repo"):
            urls.append(row["repo"])

    failures: list[tuple[str, str]] = []
    for url in sorted(set(urls)):
        if args.skip_http:
            ok = url.startswith("https://")
            status = "shape"
        else:
            ok, status = check(url, args.timeout)
        print(f"{'PASS' if ok else 'FAIL'} {status} {url}")
        if not ok:
            failures.append((url, status))

    if failures:
        print(f"FAIL: {len(failures)} links failed")
        return 1
    print(f"PASS: {len(set(urls))} links checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())

