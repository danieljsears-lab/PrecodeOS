# PrecodeOS — Claude Adapter

> AUTHORITY: Claude-specific startup notes, slash-command mapping, and local spend/status guidance.
> NOT_AUTHORITY: Shared operating model, feature requirements, route structure, schema definitions, or business policy.
> LOAD_WHEN: Using Claude Code as the active coding agent for this repo.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.3
Last updated: 2026-06-06

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
- `python3 scripts/next-step.py [--json]`
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
- `python3 scripts/run-contract-check.py`
- `python3 scripts/workflow-check.py`
- `python3 scripts/goal-frame-check.py`
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

## Routing Mapping

Use `tasks/reference/AGENT-ROUTING-PROTOCOL.md` for shared routing rules before choosing Claude-specific controls.

- `fast` maps to Haiku or low-effort Sonnet when available and the task is low-risk.
- `default` maps to Sonnet for ordinary scoped coding, synthesis, and repo exploration.
- `deep` maps to Opus or `opusplan` for planning, architecture, ambiguous debugging, and high-stakes review.
- `long-horizon` may use an extended context option only when the active bead is approved, bounded, and checkpointed.

`CLAUDE_CODE_SUBAGENT_MODEL` may set the model used for Claude subagents, but subagents still follow Precode delegation boundaries: no bead activation, no scope widening, no approval bypass, and no independent escalation when the task was undersized.

## Context Budget

Treat about 80% context usage as the point to prepare a checkpoint, compact, restart, or handoff.

For Claude sessions, a local or team preference may set:

```bash
CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=80
```

This is optional guidance, not a Precode invariant. Lower values can make sense for very long sessions or volatile tool output. After compaction, reload active memory, the active bead, and the primary authority before continuing.

## Spend Notes

If Claude Code exposes live usage telemetry such as the status line or built-in cost/stats commands, treat it as advisory only.
Prefer importing reliable exports with `python3 scripts/import-agent-spend.py`.
Record fallback durable cross-tool spend entries with:

```bash
bash scripts/log-agent-spend.sh --tool claude-code --task "current bead"
```
