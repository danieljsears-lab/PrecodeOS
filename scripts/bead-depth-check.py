#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-05-06
# Owner: Precode OS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import json

from os_compiler import compile_state, repo_root


def main() -> int:
    payload = compile_state(repo_root()).get("bead_depth") or {
        "status": "missing",
        "warnings": ["adaptive bead-depth analysis unavailable"],
        "details": {},
    }
    print(json.dumps({"tool": "bead-depth-check", **payload}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
