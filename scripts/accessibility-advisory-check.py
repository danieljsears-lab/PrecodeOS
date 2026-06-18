#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-06-18
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import json

from os_compiler import compile_state, repo_root


def main() -> int:
    payload = compile_state(repo_root()).get("accessibility_advisory_gate") or {
        "status": "not_invoked",
        "warnings": [],
        "details": {
            "advisory_only": True,
            "invoked": False,
            "reason": "accessibility advisory analysis unavailable",
        },
    }
    print(json.dumps({"tool": "accessibility-advisory-check", **payload}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
