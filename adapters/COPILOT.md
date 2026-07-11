# PrecodeOS — GitHub Copilot Adapter

> AUTHORITY: GitHub Copilot-specific startup notes, repository-instruction shim guidance, shared-script entrypoints, and manual validation reminders.
> NOT_AUTHORITY: Shared operating model, feature requirements, route structure, schema definitions, provider pricing, model availability, or business policy.
> LOAD_WHEN: Using GitHub Copilot, Copilot CLI, Copilot coding agent, or Copilot code review as the active coding agent surface for this repo.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.1
Last updated: 2026-07-11

Read `AGENT.md`, then `DECISIONS.md`, then `tasks/todo.md`.

## Copilot Surfaces

- `.github/copilot-instructions.md` is the repository-wide Copilot shim.
- Copilot may also read `AGENTS.md` or path-specific `.github/instructions/*.instructions.md` files when the active Copilot surface supports them.
- Do not add path-specific Copilot instruction files unless a repeated, tool-specific gap proves the root shim and shared adapter matrix are insufficient.
- Copilot Chat in IDEs, Copilot CLI, Copilot coding agent, and Copilot code review have different execution and review boundaries. Treat them as separate surfaces even when they share repository instructions.
- Shared repo scripts remain the canonical command surface.

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
- `python3 scripts/external-status.py`
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

## Routing Mapping

Use `tasks/reference/AGENT-ROUTING-PROTOCOL.md` for shared routing rules before choosing Copilot-specific controls.

Map `fast`, `default`, `deep`, and `long-horizon` to Copilot's available model selector, agent mode, CLI mode, coding agent, or code review controls only when the active surface exposes them. GitHub's current model list, base model, LTS model, billing, quotas, and preview flags are tool-native facts; do not freeze them in Precode.

Use Copilot cloud or PR-agent surfaces only when the active bead is approved, files in play and checks are clear, and review remains human-gated. If Copilot cannot run the shared scripts directly, require equivalent recorded evidence before accepting work.

If Copilot exposes usage or cost telemetry, treat it as advisory only and record durable session totals with:

```bash
python3 scripts/import-agent-spend.py
bash scripts/log-agent-spend.sh --tool github-copilot --task "current bead"
```
