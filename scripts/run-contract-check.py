#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-05-11
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import json

from os_compiler import compile_state, repo_root


def main() -> int:
    root = repo_root()
    state = compile_state(root)
    run_contract = state.get("run_contract") or {}
    print(json.dumps({"tool": "run-contract-check", **run_contract}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
