#!/usr/bin/env python3
# Version: v0.1.1
# Last updated: 2026-05-06
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
import json

from os_compiler import compile_state, repo_root


def main() -> int:
    parser = argparse.ArgumentParser(description="Show advisory files-in-play and command mutation guardrails.")
    parser.add_argument("--command", default="", help="optional command summary to classify before running")
    parser.add_argument("--edit-lock", action="store_true", help="show advisory edit-lock guidance for this bead")
    args = parser.parse_args()

    payload = compile_state(repo_root(), command=args.command, edit_lock=args.edit_lock).get("files_in_play_guardrail") or {
        "status": "missing",
        "warnings": ["files-in-play guardrail analysis unavailable"],
        "details": {},
    }
    print(json.dumps({"tool": "files-in-play-check", **payload}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
