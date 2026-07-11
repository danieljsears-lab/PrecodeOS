# PrecodeOS — Codex Adapter

> AUTHORITY: Codex-specific startup notes, shared-script entrypoints, and manual validation reminders.
> NOT_AUTHORITY: Shared operating model, feature requirements, route structure, or schema definitions.
> LOAD_WHEN: Using Codex as the active coding agent for this repo.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.4
Last updated: 2026-07-11

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

Codex does not rely on another tool's slash-command surface.
When markdown files change, run `bash scripts/validate-memory.sh [changed-path]` before closing the loop.

## Routing Mapping

Use `tasks/reference/AGENT-ROUTING-PROTOCOL.md` for shared routing rules before choosing Codex-specific controls.

- `fast` maps to a smaller available model or lower reasoning effort when the task is mechanical, low-risk, and easy to verify.
- `default` maps to the inherited/default Codex model and medium reasoning for ordinary scoped implementation, synthesis, and repo exploration.
- `deep` maps to a stronger Codex/OpenAI coding model or higher reasoning effort for architecture, ambiguous debugging, security-sensitive review, and high-blast-radius decisions.
- `long-horizon` maps to Codex cloud/background delegation only when the active bead is approved, files in play and checks are clear, and review remains human-gated.

If Codex does not expose a native compaction threshold, treat about 80% context pressure as a checkpoint, Context Pack, handoff, or fresh-session trigger. Reload active memory, the active bead, and the primary authority after any restart or handoff.

Codex subagents or delegated workers may be used only when the work is bounded, materially useful, and not a hidden bead transition. If a delegated task needs broader scope, stronger reasoning, or new approval, it reports back instead of escalating independently.

If you have tool-native spend telemetry, treat it as advisory only and record durable session totals with:

```bash
python3 scripts/import-agent-spend.py
bash scripts/log-agent-spend.sh --tool codex --task "current bead"
```
