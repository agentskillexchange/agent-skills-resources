#!/usr/bin/env python3
"""Lightweight link checker for resources.json."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from link_utils import check_url

ROOT = Path(__file__).resolve().parents[1]


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
            result = check_url(url, args.timeout)
            ok = bool(result["ok"])
            status = str(result["status"] or result["error"])
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
