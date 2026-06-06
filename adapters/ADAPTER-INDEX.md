# PrecodeOS — Adapter Index

> AUTHORITY: Tool-adapter index, adapter ownership boundaries, and where to look for tool-specific notes.
> NOT_AUTHORITY: Shared operating model, feature requirements, route structure, schema definitions, or business policy.
> LOAD_WHEN: Selecting or switching the active AI coding tool for a session.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.6
Last updated: 2026-06-06

## Purpose

Use `AGENT.md` for the shared operating system.
Use the files in this folder only for tool-specific notes that do not belong in the shared core.
Use `modes/*.md` and `tasks/beads/*.md` for shared execution behavior.
Use `tasks/reference/AGENT-ROUTING-PROTOCOL.md` for shared model tier, context-budget, delegation, and tool-routing guidance before applying adapter-specific settings.

## Available Adapters

- `adapters/CLAUDE.md` — Claude Code-specific notes
- `adapters/CODEX.md` — Codex-specific notes
- `adapters/COPILOT.md` — GitHub Copilot-specific notes
- `adapters/GEMINI.md` — Gemini-specific notes
- `adapters/ANTIGRAVITY.md` — Antigravity-specific notes
- `adapters/CURSOR.md` — Cursor-specific notes

## Capability Matrix

Official tool documentation and in-product model selectors remain authoritative for exact model availability, pricing, quotas, preview flags, and file-discovery behavior. This matrix is a maintainer-facing compatibility summary, not a promise that every surface behaves identically.

Status values:
- `supported` — Precode ships an adapter or shim and expects normal repo use.
- `shim-supported` — Precode's root shims should be enough unless a repeated tool-specific gap appears.
- `candidate` — Watch for official instruction behavior plus credible adoption evidence.
- `roadmap` — Keep in `_maintainer/PRECODE-ROADMAP.md` until there is a stronger need.

| Environment | Status | Auto-load instructions | Scoped rules | CLI | IDE/editor | Cloud PR agent | Model selector | Delegation | Telemetry | Checkpoints | MCP/tools | Review behavior |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Claude Code | supported | `CLAUDE.md` | Tool-native hooks/settings, if configured | yes | optional integrations | no | yes | subagents when available | advisory | Precode checkpoint/compact/handoff | tool-dependent | manual review plus `/review`-style surfaces when available |
| Codex | supported | `AGENTS.md` | no Precode-native scoped shim | yes | available when tool exposes it | background/cloud when available | yes | bounded workers when available | advisory | Precode checkpoint/handoff | tool-dependent | human-gated review |
| GitHub Copilot | supported | `.github/copilot-instructions.md`, `AGENTS.md` when supported | `.github/instructions/*.instructions.md` when needed | yes | yes | yes | yes | coding agent / partner agents when enabled | advisory | Precode checkpoint/handoff | tool-dependent | Copilot code review and PR review are evidence, not acceptance |
| Gemini | supported | `GEMINI.md` | no Precode-native scoped shim | Gemini CLI when available | Code Assist when available | no | yes | agent mode when available | advisory | Precode checkpoint/handoff | MCP/tools when available | human-gated review |
| Cursor | supported | `AGENTS.md` or Cursor rules | `.cursor/rules` when needed | no | yes | no | yes | agent controls when available | advisory | Precode checkpoint/handoff | MCP/tools when available | human-gated review |
| Antigravity | supported | tool-dependent | tool-dependent | tool-dependent | yes | tool-dependent | tool-dependent | tool-dependent | advisory | Precode checkpoint/handoff | tool-dependent | human-gated review |
| Windsurf/Cascade | shim-supported | `AGENTS.md` | `.windsurf/rules` if future evidence warrants | no | yes | no | yes | Cascade planning/features | advisory | tool checkpoints plus Precode checkpoint/handoff | MCP/tools when available | human-gated review |
| JetBrains/Junie | candidate | tool-dependent | steering/instructions depend on surface | tool-dependent | yes | tool-dependent | yes | tool-dependent | advisory | Precode checkpoint/handoff | tool-dependent | human-gated review |
| Kiro | candidate | steering files | `.kiro/steering` | yes | yes | web/agent surfaces | yes | autonomous/session modes | advisory | Precode checkpoint/handoff | tool-dependent | human-gated review |
| Zed | candidate | `.rules` / supported instruction files | rules library/settings | no | yes | no | yes | agent panel | advisory | Precode checkpoint/handoff | tool-dependent | human-gated review |
| Cline/Roo and similar VS Code agents | roadmap | extension-dependent | extension-dependent | no | yes | no | yes | extension-dependent | advisory | Precode checkpoint/handoff | MCP/tools often available | human-gated review |
| Replit/Devin and similar hosted agents | roadmap | platform-dependent | platform-dependent | platform-dependent | hosted editor | yes | yes | platform agent | advisory | Precode checkpoint/handoff | platform-dependent | human-gated review |

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
