# PrecodeOS — Antigravity Adapter

> AUTHORITY: Antigravity-specific startup notes, shared-script entrypoints, and manual validation reminders.
> NOT_AUTHORITY: Shared operating model, feature requirements, route structure, or schema definitions.
> LOAD_WHEN: Using Antigravity as the active coding agent for this repo.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.2
Last updated: 2026-05-10

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
- `python3 scripts/goal-frame-check.py`
- `python3 scripts/long-horizon-check.py`
- `python3 scripts/completion-check.py`
- `python3 scripts/pattern-check.py`
- `python3 scripts/version-check.py`
- `bash scripts/log-agent-spend.sh --tool <tool> --task "current bead"`
- `bash scripts/scheduled-audit.sh`

Antigravity should follow the same execution contract and shared verification steps as any other agent.
After markdown edits, run `bash scripts/validate-memory.sh [changed-path]` before ending the session.

## Routing Mapping

Use `tasks/reference/AGENT-ROUTING-PROTOCOL.md` for shared routing rules before choosing Antigravity-specific controls.

Map `fast`, `default`, `deep`, and `long-horizon` to Antigravity's available model, effort, context, or delegation controls only when the active tool exposes them. If Antigravity does not expose a native compaction threshold or delegation control, fall back to Precode checkpoint, Context Pack, handoff, and fresh-context review discipline.

If you have tool-native spend telemetry, treat it as advisory only and record durable session totals with:

```bash
python3 scripts/import-agent-spend.py
bash scripts/log-agent-spend.sh --tool antigravity --task "current bead"
```
