#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-04-26
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import json
import sys
from pathlib import Path

from os_compiler import read_todo_state, repo_root
from os_parser import MarkdownDocument, bullet_items


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else repo_root()
    todo = read_todo_state(root)

    bead_sections: dict[str, str] = {}
    bead_bullets: dict[str, list[str]] = {}
    bead_frontmatter: dict[str, object] = {}
    bead_path = root / str(todo["current_bead"]) if todo["current_bead"] else None
    bead_exists = bool(bead_path and bead_path.is_file())

    if bead_exists and bead_path is not None:
        bead_doc = MarkdownDocument.load(bead_path)
        bead_sections = bead_doc.sections
        bead_bullets = {key: bullet_items(value) for key, value in bead_doc.sections.items()}
        bead_frontmatter = bead_doc.frontmatter

    payload = {
        "todo_path": "tasks/todo.md",
        "current_bead": todo["current_bead"],
        "current_bead_exists": bead_exists,
        "todo_sections": todo["sections"],
        "todo_bullets": {key: bullet_items(value) for key, value in todo["sections"].items()},
        "todo_frontmatter": todo["frontmatter"],
        "bead_sections": bead_sections,
        "bead_bullets": bead_bullets,
        "bead_frontmatter": bead_frontmatter,
    }

    print(json.dumps(payload, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
