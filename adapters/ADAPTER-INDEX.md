# PrecodeOS — Adapter Index

> AUTHORITY: Tool-adapter index, adapter ownership boundaries, and where to look for tool-specific notes.
> NOT_AUTHORITY: Shared operating model, feature requirements, route structure, schema definitions, or business policy.
> LOAD_WHEN: Selecting or switching the active AI coding tool for a session.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.8
Last updated: 2026-06-18

## Purpose

Use `AGENT.md` for the shared operating system.
Use the files in this folder only for tool-specific notes that do not belong in the shared core.
Use `modes/*.md` and `tasks/beads/*.md` for shared execution behavior.
Use `tasks/reference/AGENT-ROUTING-PROTOCOL.md` for shared model tier, context-budget, delegation, and tool-routing guidance before applying adapter-specific settings.
Use the Context Layer Matrix in `docs/PRECODE-PACKAGE-FILE-INVENTORY.md` when a tool-specific instruction, shim, generated report, memory result, or source artifact could be mistaken for Precode authority.

## Available Adapters

- `adapters/CLAUDE.md` — Claude Code-specific notes
- `adapters/CODEX.md` — Codex-specific notes
- `adapters/COPILOT.md` — GitHub Copilot-specific notes
- `adapters/GEMINI.md` — Gemini-specific notes
- `adapters/ANTIGRAVITY.md` — Antigravity-specific notes
- `adapters/CURSOR.md` — Cursor-specific notes

## Compatibility Shim Matrix

Official tool documentation and in-product controls remain authoritative for exact model availability, pricing, quotas, preview flags, MCP behavior, and file-discovery behavior. This matrix names the Precode-owned compatibility surface only; it is not a promise that every host behaves identically.

Status values:
- `shipped` - Precode ships a shim or adapter for this host family.
- `advisory` - Precode has a thin adapter note or likely root-shim path, but no broader support promise.
- `deferred` - Keep in roadmap/watchlist notes until repeated evidence justifies a shipped surface.

| Host family | Status | Precode-owned surface | Expected load contract | Boundary |
|---|---|---|---|---|
| Codex and AGENTS-compatible agents | shipped | `AGENTS.md`, `adapters/CODEX.md` | Auto-load `AGENTS.md`, then follow `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`. | No Precode-native scoped rule tree; use shared routing, checkpoint, handoff, and review discipline. |
| Claude Code and Claude-style project instructions | shipped | `CLAUDE.md`, `adapters/CLAUDE.md` | Auto-load `CLAUDE.md`, then follow the shared active-memory files and Claude adapter notes. | Claude-specific controls stay in the adapter; the shim must not become a second operating model. |
| Gemini-style project memory | shipped | `GEMINI.md`, `adapters/GEMINI.md` | Auto-load `GEMINI.md`, then follow the shared active-memory files and Gemini adapter notes. | Gemini-specific controls stay advisory and cannot approve work, commands, reviews, or transitions. |
| GitHub Copilot repository instructions | shipped | `.github/copilot-instructions.md`, `adapters/COPILOT.md` | Load repository instructions when the active Copilot surface supports them, then follow the shared active-memory files. | Copilot code review, PR review, issues, checks, and comments are evidence, not acceptance or task authority. |
| Cursor / VS Code-adjacent agents | advisory | `adapters/CURSOR.md`; `AGENTS.md` when supported by the host | Use the shipped adapter note and root shim behavior when the host supports it. | Do not add `.cursor/rules` or VS Code rule directories until repeated evidence shows a root-shim gap. |
| Antigravity | advisory | `adapters/ANTIGRAVITY.md` | Use the adapter note plus the host's documented instruction behavior. | Host-specific behavior remains tool-dependent; no broad compatibility promise. |
| Windsurf/Cascade, JetBrains/Junie, Kiro, Zed, Cline/Roo, Replit/Devin, and similar hosted or IDE agents | deferred | none beyond any host support for `AGENTS.md` or shared repo files | Treat as watchlist surfaces until official instruction behavior and repeated Precode usage justify a shipped adapter or shim. | Do not create native rule-directory shims, detailed host capability tables, package-manager semantics, optional packs, or support promises from speculation. |

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

## Switching Rule

Use one coding agent at a time.
Before switching tools, run `bash scripts/handoff.sh [next-agent]`.

## Spend Telemetry

Prefer `python3 scripts/import-agent-spend.py` when the active tool exposes a reliable usage export.
Use `bash scripts/log-agent-spend.sh --tool <tool> --task "current bead"` as the fallback manual ledger entry.

## Routing Discipline

Adapters translate the shared `fast`, `default`, `deep`, and `long-horizon` routing tiers into tool-native model, effort, delegation, and compaction controls when those controls exist.

`python3 scripts/next-step.py` owns the generated Router Decision. Adapters may display or explain its `user_decision`, `single_next_protocol`, `load_plan`, and `context_footprint`, but they must not treat those fields as approval or active memory.

If a tool does not expose a native control, fall back to Precode checkpoint, Context Pack, handoff, and review discipline. Adapter-specific routing notes must not expand active memory, activate beads, override files in play, or bypass human approval gates.

Adapters and shims are compatibility guidance only. They translate Precode into a host tool's discovery and routing habits, but they must not create alternate active memory, host-specific authority trees, generated instruction sources, task approval, review acceptance, or package-manager behavior.
