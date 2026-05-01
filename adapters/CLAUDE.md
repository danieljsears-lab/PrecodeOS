# Precode OS — Claude Adapter

> AUTHORITY: Claude-specific startup notes, slash-command mapping, and local spend/status guidance.
> NOT_AUTHORITY: Shared operating model, feature requirements, route structure, schema definitions, or business policy.
> LOAD_WHEN: Using Claude Code as the active coding agent for this repo.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-04-26

Read `AGENT.md`, then `DECISIONS.md`, then `tasks/todo.md`.

## Shared Command Surface

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
- `python3 scripts/long-horizon-check.py`
- `python3 scripts/completion-check.py`
- `python3 scripts/pattern-check.py`
- `python3 scripts/version-check.py`
- `bash scripts/log-agent-spend.sh --tool <tool> --task "current bead"`
- `bash scripts/scheduled-audit.sh`

## Claude Surfaces

- Optional Claude slash commands may wrap the shared scripts.
- Optional Claude-specific hooks or status lines must stay convenience-only and point back to the shared command surface.
- Shared repo scripts remain the canonical command surface whenever possible.

## Spend Notes

If Claude Code exposes live usage telemetry such as the status line or built-in cost/stats commands, treat it as advisory only.
Prefer importing reliable exports with `python3 scripts/import-agent-spend.py`.
Record fallback durable cross-tool spend entries with:

```bash
bash scripts/log-agent-spend.sh --tool claude-code --task "current bead"
```
