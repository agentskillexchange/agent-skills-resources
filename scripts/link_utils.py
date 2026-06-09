"""Shared link-checking helpers for validation scripts."""

from __future__ import annotations

import urllib.error
import urllib.request

USER_AGENT = "agent-skills-resources-link-check/1.0"
TEMPORARY_HTTP_STATUSES = {403, 408, 425, 429, 500, 502, 503, 504}


def check_url(url: str, timeout: int) -> dict[str, object]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            status = int(getattr(resp, "status", 0))
            return {
                "url": url,
                "ok": 200 <= status < 400,
                "status": status,
                "temporary": False,
                "error": "",
            }
    except urllib.error.HTTPError as exc:
        status = int(exc.code)
        return {
            "url": url,
            "ok": 300 <= status < 400,
            "status": status,
            "temporary": status in TEMPORARY_HTTP_STATUSES,
            "error": "HTTPError",
        }
    except Exception as exc:  # noqa: BLE001 - report concise network failures
        return {
            "url": url,
            "ok": False,
            "status": None,
            "temporary": False,
            "error": type(exc).__name__,
        }

