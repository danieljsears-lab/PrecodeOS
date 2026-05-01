#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-04-26
# Owner: Precode OS
from __future__ import annotations

import json
from typing import Any

from os_compiler import compile_state, repo_root


def main() -> int:
    root = repo_root()
    state = compile_state(root)
    quality = state.get("verification_quality") or {}
    print(json.dumps({"tool": "verification-check", **quality}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
