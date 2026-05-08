#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-05-08
# Owner: Precode OS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import json

from os_compiler import compile_state, repo_root


def main() -> int:
    state = compile_state(repo_root())
    payload = state.get("goal_frame") or {
        "status": "missing",
        "warnings": ["Goal Frame summary unavailable"],
        "details": {},
    }
    print(json.dumps({"tool": "goal-frame-check", **payload}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
