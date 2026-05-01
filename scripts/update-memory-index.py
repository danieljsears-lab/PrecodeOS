#!/usr/bin/env python3
# Version: v0.1.0
# Last updated: 2026-04-27
# Owner: Precode OS
from __future__ import annotations

from os_compiler import compile_state, repo_root, render_memory_index_markdown, write_json


def main() -> int:
    root = repo_root()
    state = compile_state(root)
    memory = state.get("memory") or {}
    write_json(root / "logs" / "memory-index.json", memory)
    (root / "logs" / "memory-index.md").write_text(render_memory_index_markdown(memory), encoding="utf-8")
    print("memory-index: wrote logs/memory-index.md and logs/memory-index.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
