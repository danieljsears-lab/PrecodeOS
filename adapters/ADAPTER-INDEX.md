# PrecodeOS — Adapter Index

> AUTHORITY: Tool-adapter index, adapter ownership boundaries, and where to look for tool-specific notes.
> NOT_AUTHORITY: Shared operating model, feature requirements, route structure, schema definitions, or business policy.
> LOAD_WHEN: Selecting or switching the active AI coding tool for a session.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.2.0
Last updated: 2026-09-06

## Purpose

Use `AGENT.md` for the shared operating system.
Use the files in this folder only for tool-specific notes that do not belong in the shared core.
Use `modes/*.md` and `tasks/beads/*.md` for shared execution behavior.
Use `tasks/reference/AGENT-ROUTING-PROTOCOL.md` for shared model tier, context-budget, delegation, and tool-routing guidance before applying adapter-specific settings.
Use `tasks/reference/TOOL-EXECUTION-PROTOCOL.md` for the shared access ladder before translating risk into host-specific prompts. Adapters may explain `inspect`, `verify`, `local-change`, `sensitive`, `external-change`, and `destructive`, but they must not redefine those labels as provider settings, sandbox policy, command approval, schema metadata, or host permissions.
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
- `certified-for-launch` - the host has a deterministic Precode conformance result for the bounded macOS setup-and-orientation journey.
- `shipped` - Precode ships a shim or adapter for this host family without the bounded v1 certification claim.
- `advisory` - Precode has a thin adapter note or likely root-shim path, but no broader support promise.
- `deferred` - Keep in roadmap/watchlist notes until repeated evidence justifies a shipped surface.

| Host family | Status | Precode-owned surface | Expected load contract | Boundary |
|---|---|---|---|---|
| Codex and AGENTS-compatible agents | certified-for-launch | `AGENTS.md`, `adapters/CODEX.md` | Auto-load `AGENTS.md`, then follow `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`. | Conformance-certified; external no-help session result pending. No Precode-native scoped rule tree. |
| Claude Code and Claude-style project instructions | certified-for-launch | `CLAUDE.md`, `adapters/CLAUDE.md` | Auto-load `CLAUDE.md`, then follow the shared active-memory files and Claude adapter notes. | Conformance-certified; external no-help session result pending. The shim must not become a second operating model. |
| Gemini-style project memory | certified-for-launch | `GEMINI.md`, `adapters/GEMINI.md` | Auto-load `GEMINI.md`, then follow the shared active-memory files and Gemini adapter notes. | Conformance-certified; external usability evidence pending. Gemini-specific controls cannot approve work or transitions. |
| GitHub Copilot repository instructions | shipped | `.github/copilot-instructions.md`, `adapters/COPILOT.md` | Load repository instructions when the active Copilot surface supports them, then follow the shared active-memory files. | Copilot code review, PR review, issues, checks, and comments are evidence, not acceptance or task authority. |
| Cursor | certified-for-launch | `AGENTS.md`, `adapters/CURSOR.md` | Auto-load the root `AGENTS.md`, then follow the shared active-memory files. | Conformance-certified; external usability evidence pending. Do not add a competing `.cursor/rules` authority tree. |
| Antigravity | advisory | `adapters/ANTIGRAVITY.md` | Use the adapter note plus the host's documented instruction behavior. | Host-specific behavior remains tool-dependent; no broad compatibility promise. |
| Windsurf/Cascade, JetBrains/Junie, Kiro, Zed, Cline/Roo, Replit/Devin, and similar hosted or IDE agents | deferred | none beyond any host support for `AGENTS.md` or shared repo files | Treat as watchlist surfaces until official instruction behavior and repeated Precode usage justify a shipped adapter or shim. | Do not create native rule-directory shims, detailed host capability tables, package-manager semantics, optional packs, or support promises from speculation. |

Certification describes Precode contract conformance, not equal usability evidence. Codex and Claude Code are the hosts used in the six external no-help sessions. Cursor and Gemini are certified for launch through deterministic conformance plus maintainer smoke tests; external usability evidence remains pending and must be stated as such.

## V1 Agent-Operated Setup Contract

For the bounded macOS self-serve journey, the active certified agent should:

1. Identify the intended project folder; the user should not need to construct a path or interpret shell syntax.
2. Run `npx @precodeos/precodeos fast-setup-preview --target <target-project-root>`.
3. Explain package version, support status, prerequisites, target classification, proposed actions, approval IDs, validation requirements, recovery route, next safe action, and stop reason in plain English.
4. Ask for explicit approval of named current actions before running `fast-setup-apply`.
5. Adapt project-specific owner facts only through a separate approval.
6. Validate, route to the First Session Card or Daily Cockpit, and stop before product work.

The contract covers installation, validation, orientation, and next-safe-action identification. It does not certify the full idea-to-production journey, guarantee deployment or operations, or turn generated `ready_for_orientation` evidence into approval for product work.

## Shared Command Surface

Every adapter should point back to the same repo-level commands:
- `npx @precodeos/precodeos fast-setup-preview --target <target-project-root>`
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
If an adapter or root shim uses access wording that conflicts with Tool Execution, treat the adapter wording as stale and reconcile to Tool Execution before continuing.
