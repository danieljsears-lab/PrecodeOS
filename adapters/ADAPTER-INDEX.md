# Precode OS — Adapter Index

> AUTHORITY: Tool-adapter index, adapter ownership boundaries, and where to look for tool-specific notes.
> NOT_AUTHORITY: Shared operating model, feature requirements, route structure, schema definitions, or business policy.
> LOAD_WHEN: Selecting or switching the active AI coding tool for a session.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.2
Last updated: 2026-05-08

## Purpose

Use `AGENT.md` for the shared operating system.
Use the files in this folder only for tool-specific notes that do not belong in the shared core.
Use `modes/*.md` and `tasks/beads/*.md` for shared execution behavior.

## Available Adapters

- `adapters/CLAUDE.md` — Claude Code-specific notes
- `adapters/CODEX.md` — Codex-specific notes
- `adapters/GEMINI.md` — Gemini-specific notes
- `adapters/ANTIGRAVITY.md` — Antigravity-specific notes
- `adapters/CURSOR.md` — Cursor-specific notes

## Shared Command Surface

Every adapter should point back to the same repo-level commands:
- `bash scripts/install-git-hooks.sh`
- `bash scripts/session-start.sh`
- `bash scripts/checkpoint.sh`
- `bash scripts/session-close.sh`
- `bash scripts/handoff.sh [next-agent]`
- `bash scripts/validate-memory.sh`
- `bash scripts/write-guard.sh --post <changed-file>`
- `bash scripts/record-check.sh -- <command>`
- `bash scripts/log-tool-run.sh --tool <tool> --class <class> --status <pass|fail|blocked> --command "<summary>"`
- `python3 scripts/bead-transition.py`
- `python3 scripts/os-health.py`
- `python3 scripts/import-agent-spend.py`
- `python3 scripts/github-audit.py`
- `python3 scripts/import-github-sources.py`
- `python3 scripts/extension-check.py`
- `python3 scripts/verification-check.py`
- `python3 scripts/decomposition-check.py`
- `python3 scripts/state-check.py`
- `python3 scripts/context-check.py`
- `python3 scripts/orchestration-check.py`
- `python3 scripts/tool-execution-check.py`
- `python3 scripts/workflow-check.py`
- `python3 scripts/goal-frame-check.py`
- `python3 scripts/long-horizon-check.py`
- `python3 scripts/completion-check.py`
- `python3 scripts/pattern-check.py`
- `python3 scripts/version-check.py`
- `bash scripts/log-agent-spend.sh --tool <tool> --task "current bead"`
- `bash scripts/scheduled-audit.sh`

## Switching Rule

Use one coding agent at a time.
Before switching tools, run `bash scripts/handoff.sh [next-agent]`.

## Spend Telemetry

Prefer `python3 scripts/import-agent-spend.py` when the active tool exposes a reliable usage export.
Use `bash scripts/log-agent-spend.sh --tool <tool> --task "current bead"` as the fallback manual ledger entry.
