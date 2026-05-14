#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-05-03
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import json

from os_compiler import (
    compile_state,
    local_hygiene_preview_from_summary,
    render_local_hygiene_preview_markdown,
    repo_root,
    write_json,
)


def main() -> int:
    root = repo_root()
    state = compile_state(root)
    summary = state.get("local_hygiene") or {
        "status": "missing",
        "warnings": ["local hygiene summary unavailable"],
        "details": {},
    }
    preview = local_hygiene_preview_from_summary(summary)
    write_json(root / "logs" / "local-hygiene-preview.json", preview)
    (root / "logs" / "local-hygiene-preview.md").write_text(
        render_local_hygiene_preview_markdown(preview),
        encoding="utf-8",
    )
    print(json.dumps({"tool": "local-hygiene-dry-run", **preview}, indent=2, sort_keys=True))
    print("local-hygiene-dry-run: wrote logs/local-hygiene-preview.json and logs/local-hygiene-preview.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
