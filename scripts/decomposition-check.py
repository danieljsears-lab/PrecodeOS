#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-04-26
# Owner: Precode OS
from __future__ import annotations

import json

from os_compiler import compile_state, repo_root


def main() -> int:
    state = compile_state(repo_root())
    payload = state.get("decomposition_quality") or {"status": "missing", "warnings": ["decomposition quality unavailable"], "details": {}}
    print(json.dumps({"tool": "decomposition-check", **payload}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
