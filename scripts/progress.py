#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-05-18
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from os_compiler import compile_state, progress_payload, render_progress_markdown, repo_root, write_json


def main() -> int:
    root = repo_root()
    payload = compile_state(root)
    write_json(root / "logs" / "progress.json", progress_payload(payload))
    (root / "PROGRESS.md").write_text(render_progress_markdown(payload), encoding="utf-8")
    print("progress: wrote PROGRESS.md and logs/progress.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
