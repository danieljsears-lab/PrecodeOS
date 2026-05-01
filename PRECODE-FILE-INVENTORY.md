# Precode OS File Inventory
<!-- ANCHOR: file-inventory -->

> AUTHORITY: Canonical technical inventory of Precode OS-owned files, file families, purposes, relationships, and maintenance expectations.
> NOT_AUTHORITY: Active memory, product decisions, task selection, feature requirements, implementation status, target-project architecture, generated evidence truth, or bead transition approval.
> LOAD_WHEN: Orienting a technical user or coding agent before changing Precode OS files, auditing file ownership, or tracing relationships between Precode OS surfaces.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.2
Last updated: 2026-04-27

## Purpose

This inventory is the technical dictionary for Precode OS files.

Use it to answer:

- why a file exists
- what it owns
- what it must not own
- when it should be loaded
- what reads it, writes it, or generates it
- how it relates to nearby files

This document is curated. Generated support lives in `logs/file-inventory.json` and is evidence only.

## Reading Rules

- Start here when you need a technical map of Precode OS.
- Use `PRECODE-MANIFESTO.md` for Precode's philosophical anchor, values, principles, and anti-drift stance.
- Use `PRECODE-OS-README.md` for beginner-facing explanation.
- Use `HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md` for the beginner bridge from software-building lifecycle concepts to Precode and AI-agent workflow.
- Use `PRECODE-ARCHITECTURE-OVERVIEW.md` for architecture, principles, and maintainer framing.
- Use `CODEBASE-GUIDE.md` for target-project layout guidance, not Precode OS internals.
- Do not treat generated outputs or inventory warnings as task selection.

## Quick Navigation

| Area | Files or families | Purpose |
|---|---|---|
| Active memory | `AGENT.md`, `DECISIONS.md`, `tasks/todo.md` | Always-loaded operating state. |
| Root explainers | `README.md`, `PRECODE-MANIFESTO.md`, `PRECODE-OS-README.md`, `HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md`, `PRECODE-USER-GUIDE.md`, `PRECODE-ARCHITECTURE-OVERVIEW.md`, `PRECODE-FILE-INVENTORY.md` | Orientation for different audiences. |
| Project authority templates | `PROJECT-CONTEXT.md`, `FEATURES.md`, `ACCEPTANCE.md`, `ARCHITECTURE.md`, `API.md`, `DATA-MODELS.md`, `SECURITY.md`, `CODEBASE-GUIDE.md` | Target-project owner files and reference templates. |
| Protocols | `tasks/reference/*.md` | Durable Precode rules and playbooks outside active memory. |
| Execution docs | `tasks/todo.md`, `tasks/beads/*.md`, `tasks/prds/*.md` | Current work, bead contracts, and PRD shards. |
| Modes | `modes/*.md` | Navigator, builder, and review role guidance. |
| Adapters and shims | `adapters/*.md`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md` | Thin compatibility surfaces for AI coding tools. |
| Scripts | `scripts/*.py`, `scripts/*.sh` | Validation, state compilation, evidence recording, auditing, and generated reports. |
| Reviewed memory | `memory/`, `memory/cards/*.md` | Reviewed memory cards and templates; evidence only. |
| Generated reports | `OS-HEALTH.md`, `PROGRESS.md`, `logs/*.md` | Human-readable generated evidence; not authority. |
| Generated sidecars | `logs/*.json`, `logs/*.jsonl` | Machine-readable generated evidence and ledgers. |
| Generated output families | `logs/check-output/*`, `logs/scheduled-audit-output/*` | Timestamped command output and audit snapshots. |
| Workflows | `.github/workflows/*.yml` | Repository validation automation. |

## Core Relationship Map

### Active Memory To Execution

```text
AGENT.md + DECISIONS.md + tasks/todo.md
  -> active bead in tasks/beads/
  -> bead primary authority file
  -> files in play
  -> recorded checks
  -> closeout evidence
  -> review decision
  -> user-approved transition
```

`AGENT.md` owns the shared command surface. `tasks/todo.md` points to the active bead. The active bead names the primary authority and the files allowed for the current unit of work.

### Product Definition To Evidence

```text
local source or idea
  -> Local Source Intake
  -> PRD shard in tasks/prds/
  -> FEATURES.md compiled inventory
  -> bead proposal
  -> active bead
  -> logs/check-results.jsonl
  -> Closeout Evidence
```

PRDs own product intent. Beads own executable work. Logs prove what happened.

### Diary To Reviewed Memory

```text
session evidence
  -> logs/learning-diary.md
  -> memory candidate
  -> reviewed memory card in memory/cards/
  -> logs/memory-index.md/json
  -> optional promotion to DECISIONS.md, PRD, or authority doc
```

The diary is generated learning. Memory cards are reviewed evidence. Owner files hold authority.

### Scripts To Generated Sidecars

```text
scripts/os_compiler.py
  -> logs/authority-map.json
  -> logs/readiness.json
  -> logs/workflow-map.json
  -> logs/long-horizon-map.json
  -> logs/handoff-packet.json/md
  -> logs/memory-index.json/md
  -> logs/file-inventory.json
```

Generated sidecars summarize current state but do not replace source files.

### Adapters To Shared Commands

```text
AGENT.md
  -> adapters/README.md shared command surface
  -> adapters/*.md tool-specific notes
  -> AGENTS.md / CLAUDE.md / GEMINI.md / .github/copilot-instructions.md shims
```

Adapters and shims point back to the shared operating model. They must not become alternate Precode systems.

## Root File Dictionary

| File | Class | What it owns | How it relates |
|---|---|---|---|
| `AGENT.md` | active-memory | Shared AI coding agent operating model, command surface, active-memory contract, and verification gate. | Loaded every session; points to scripts, adapters, and the active-memory set. |
| `DECISIONS.md` | active-memory | Hard decisions, open questions, superseded decision context. | Consulted when product, architecture, or OS decisions are made or revisited. |
| `tasks/todo.md` | active-memory | Current bead pointer and current execution view. | Must match the one `in_progress` bead. |
| `README.md` | reference | Short scaffold navigation and adaptation start points. | Links to major protocols and first adaptation steps. |
| `PRECODE-MANIFESTO.md` | reference | Philosophical anchor for why Precode exists, who it serves, core values, and principles. | Guides positioning and fit for future OS changes without becoming operational authority. |
| `PRECODE-OS-README.md` | reference | Beginner-first canonical explainer for what Precode is and why it exists. | Points technical readers to the architecture overview and this inventory. |
| `HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md` | reference | Beginner-facing bridge from traditional software-building stages to Precode and AI coding agent workflows. | Teaches non-technical users how ideas become planned, built, verified, deployed, and learned from without replacing the user guide. |
| `PRECODE-USER-GUIDE.md` | reference | Hands-on user playbook for operating Precode. | Prescriptive guide for non-technical users. |
| `PRECODE-ARCHITECTURE-OVERVIEW.md` | reference | Reviewer-facing architecture, principles, layer model, trust boundaries, and limitations. | Deep companion to the README and this inventory. |
| `PRECODE-FILE-INVENTORY.md` | reference | Canonical technical file dictionary and relationship map. | Supported by `logs/file-inventory.json`. |
| `PROJECT-CONTEXT.md` | reference | Target-project constitution and integration boundaries. | Loaded when project context, integrations, or environment assumptions matter. |
| `OPERATING-CONSTRAINTS.md` | reference | Shared edit discipline, scope control, generated-output demotion, and reference-loading rules. | Always-loaded by `AGENT.md` as shared constraints. |
| `FEATURES.md` | reference | Compiled feature inventory and approved requirements. | Fed by approved PRD shards. |
| `ACCEPTANCE.md` | reference | Done checks and acceptance criteria. | Used when defining or reviewing verification gates. |
| `ARCHITECTURE.md` | reference | Route structure, flow shape, module placement, and auth boundaries. | Primary authority for architecture-affecting beads. |
| `API.md` | reference | API route rules, server-side boundaries, webhooks, and handler conventions. | Primary authority for API-affecting beads. |
| `DATA-MODELS.md` | reference | Schema fields, entities, data relationships, and semantic meaning. | Primary authority for schema-affecting beads. |
| `SECURITY.md` | reference | Security, privacy, auth, and sensitive-surface rules. | Primary authority for security-affecting beads. |
| `CODEBASE-GUIDE.md` | reference | Target-project repository layout and file placement conventions. | Not the Precode OS inventory; use this for app layout decisions. |
| `PROGRESS.md` | generated | Generated progress snapshot. | Evidence only; not active memory. |
| `OS-HEALTH.md` | generated | Generated OS health, warnings, loop metrics, and sidecar summary. | Evidence only; refreshed by `scripts/os-health.py`. |

## Task And Reference Dictionary

| File or family | Class | What it owns | How it relates |
|---|---|---|---|
| `tasks/reference/*.md` | reference | Protocols and playbooks for specific Precode behaviors. | Loaded conditionally by active bead or workflow need. |
| `tasks/reference/PRD-PROTOCOL.md` | reference | Product Definition Gate and PRD shard requirements. | Governs PRD creation and approval before feature implementation. |
| `tasks/reference/LOCAL-SOURCE-INTAKE-PROTOCOL.md` | reference | Intake of local notes, docs, screenshots, and research as evidence. | Feeds PRD-ready summaries without creating authority. |
| `tasks/reference/DECOMPOSITION-PROTOCOL.md` | reference | Bead slicing, dependencies, and not-a-bead-yet criteria. | Used before activating candidate beads. |
| `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md` | reference | Evidence tiers, sensitive gates, and false-done warnings. | Informs checks, closeout, and OS Health warnings. |
| `tasks/reference/MEMORY-PROTOCOL.md` | reference | Reviewed filesystem memory rules and promotion path. | Governs `memory/cards/` and generated memory indexes. |
| `tasks/reference/PROMPT-PATTERNS.md` | reference | Copyable prompts for common Precode work. | Teaching aid; not authority over active memory or beads. |
| `tasks/beads/README.md` | reference | Bead schema, templates, closeout guidance, and review rules. | Defines shape for `tasks/beads/*.md`. |
| `tasks/beads/*.md` | execution contract | One durable unit of work, files in play, checks, stop conditions, and closeout. | One bead may be `in_progress`; active bead is pointed to by `tasks/todo.md`. |
| `tasks/prds/README.md` | reference | PRD directory rules and shard guidance. | Supports `tasks/prds/*.md`. |
| `tasks/prds/*.md` | reference | Product definition shards. | Feed `FEATURES.md` and candidate beads. |

## Script Dictionary

| File | Purpose | Inputs | Outputs or side effects |
|---|---|---|---|
| `scripts/os_parser.py` | Shared markdown/frontmatter parsing helpers. | Markdown files. | Parser utilities for other scripts. |
| `scripts/os_compiler.py` | Compiles Precode state and sidecars. | Active memory, beads, logs, docs. | `logs/*.json`, generated handoff/memory/file inventory surfaces. |
| `scripts/os-health.py` | Renders OS Health. | Compiled state. | `OS-HEALTH.md`, `logs/os-health.json`. |
| `scripts/validate-memory.sh` | Validates core Precode document invariants. | Required docs, todo, beads. | Pass/fail validation output. |
| `scripts/record-check.sh` | Runs a verification command and records evidence. | Command, active bead. | `logs/check-results.jsonl`, `logs/check-output/*`, closeout refresh. |
| `scripts/session-start.sh` | Starts a session and prints active context. | Active memory and bead state. | Loop event and human-readable context. |
| `scripts/checkpoint.sh` | Records checkpoint context. | Active bead and current state. | `logs/loop-runs.jsonl`. |
| `scripts/session-close.sh` | Closes a session and refreshes reports. | Active bead, checks, closeout. | Session close event, diary/health refresh, transition proposal when eligible. |
| `scripts/handoff.sh` | Produces handoff context. | Active state and optional next-agent name. | `logs/handoffs.jsonl`, handoff packet refresh. |
| `scripts/bead-transition.py` | Evaluates or approves bead transition. | Active bead closeout and next bead. | Transition report or approved active-bead update. |
| `scripts/update-bead-closeout.py` | Refreshes closeout evidence markers. | Check logs and active bead. | Updates active bead closeout fields. |
| `scripts/log-loop-event.sh` | Appends loop events. | Event type and bead context. | `logs/loop-runs.jsonl`. |
| `scripts/execution-state.py` | Prints execution state. | Active memory and bead state. | Human-readable or machine-readable state. |
| `scripts/write-guard.sh` | Guards writes against scope rules. | Paths and active bead context. | Pass/fail write-scope signal. |
| `scripts/install-git-hooks.sh` | Installs local git hooks when available. | Repo checkout. | Local hook files. |
| `scripts/pre-commit-validate.sh` | Runs validation before commit. | Working tree. | Pass/fail hook output. |
| `scripts/scheduled-audit.sh` | Shell wrapper for opt-in scheduled audits. | Local repo and optional external tools. | Audit output files and generated audit report. |
| `scripts/scheduled-audit.py` | Renders scheduled audit report. | Audit command results and compiled state. | `logs/scheduled-audit.md/json`. |
| `scripts/github-audit.py` | Read-only GitHub repository/CI audit. | Git and `gh` when configured. | JSON status output. |
| `scripts/import-github-sources.py` | Read-only GitHub issue/PR intake. | `gh` or sample source. | Generated GitHub source intake evidence. |
| `scripts/import-agent-spend.py` | Imports agent spend telemetry. | Supported usage exports or local sources. | Normalized spend rows or dry-run output. |
| `scripts/log-agent-spend.sh` | Manual spend logging fallback. | Tool/task/tokens/cost. | `logs/agent-spend.jsonl`. |
| `scripts/log-tool-run.sh` | Logs important non-check tool calls. | Tool command metadata. | `logs/tool-runs.jsonl`. |
| `scripts/update-learning-diary.py` | Renders generated learning diary. | Bead closeout, checks, spend, loop events. | `logs/learning-diary.md/jsonl`. |
| `scripts/update-memory-index.py` | Renders reviewed memory index. | `memory/cards/*.md`. | `logs/memory-index.md/json`. |
| `scripts/file-inventory.py` | Renders/checks file inventory metadata. | Repo files and authority contracts. | `logs/file-inventory.json` or advisory JSON. |
| `scripts/*-check.py` | Advisory quality checks. | Compiled state and logs. | JSON warnings; no state mutation. |
| `scripts/version-check.py` | Checks version metadata coverage. | Docs, scripts, workflows. | Advisory JSON. |

## Adapter, Mode, Memory, And Workflow Dictionary

| File or family | Class | What it owns | How it relates |
|---|---|---|---|
| `adapters/README.md` | reference | Shared adapter command surface and tool-neutral expectations. | Source of truth for adapter command parity. |
| `adapters/*.md` | reference | Tool-specific notes for Codex, Claude, Cursor, Gemini, Antigravity, and related agents. | Thin wrappers around `AGENT.md`. |
| `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md` | reference shims | Auto-discovery compatibility for specific tools. | Must point back to `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`. |
| `modes/NAVIGATOR.md` | reference | Planning/navigation role guidance. | Used when choosing work or shaping tasks. |
| `modes/BUILDER.md` | reference | Implementation role guidance. | Used during scoped code or doc changes. |
| `modes/REVIEW.md` | reference | Review role guidance. | Used for code review, closeout, and acceptance checks. |
| `memory/README.md` | reference | Reviewed memory directory guidance. | Points to memory protocol and card directory. |
| `memory/cards/README.md` | reference | Memory card format. | Defines reviewed memory card expectations. |
| `memory/cards/MEMORY-CARD-template.md` | reference template | Starter shape for reviewed memory cards. | Copied for approved memory cards. |
| `.github/workflows/precode-validate.yml` | workflow | GitHub Actions validation for Precode docs. | Runs read-only validation on pushes and pull requests. |

## Generated Evidence And Log Families

| File or family | Class | Purpose | Rule |
|---|---|---|---|
| `logs/README.md` | reference | Log taxonomy and generated-output rules. | Versioned reference doc. |
| `logs/check-results.jsonl` | generated evidence | Append-only check result ledger. | Evidence only. |
| `logs/check-output/*` | generated evidence family | Timestamped command output logs. | Document as a family, not individual files. |
| `logs/loop-runs.jsonl` | generated evidence | Session start, checkpoint, and close events. | Evidence only. |
| `logs/handoffs.jsonl` | generated evidence | Handoff events. | Evidence only. |
| `logs/agent-spend.jsonl` | generated evidence | Normalized agent spend rows. | Missing spend is unknown, not zero. |
| `logs/tool-runs.jsonl` | generated evidence | Non-check tool-run ledger. | Not verification unless also recorded as a check. |
| `logs/os-events.jsonl` | generated evidence | Compiled event stream. | Generated from logs. |
| `logs/os-health.json` | generated sidecar | Machine-readable OS Health payload. | Evidence only. |
| `logs/authority-map.json` | generated sidecar | Authority contract index. | Evidence only. |
| `logs/adapter-index.json` | generated sidecar | Adapter command-surface summary. | Evidence only. |
| `logs/shim-index.json` | generated sidecar | Shim summary. | Evidence only. |
| `logs/readiness.json` | generated sidecar | Bead readiness and promotion state. | Evidence only. |
| `logs/orchestration-map.json` | generated sidecar | Intent orchestration summary. | Evidence only. |
| `logs/workflow-map.json` | generated sidecar | Workflow selection summary. | Evidence only. |
| `logs/long-horizon-map.json` | generated sidecar | Future/blocked/deferred work summary. | Evidence only. |
| `logs/handoff-packet.md/json` | generated report | Handoff context pack. | Orientation only; not transition approval. |
| `logs/learning-diary.md/jsonl` | generated report | Session learning digest and entries. | Not active memory. |
| `logs/memory-index.md/json` | generated report | Reviewed memory card index. | Search aid only. |
| `logs/file-inventory.json` | generated sidecar | Generated inventory metadata. | Maintenance aid only. |
| `logs/pattern-guidance.json` | generated sidecar | System design pattern guidance. | Advisory only. |
| `logs/scheduled-audit.md/json` | generated report | Scheduled audit summary. | Evidence only. |
| `logs/scheduled-audit-output/*` | generated evidence family | Timestamped audit helper outputs. | Document as a family, not individual files. |

## Maintenance Rules

- Add new Precode OS-owned files here when they become durable surfaces.
- Add generated outputs by family when they are timestamped or high-churn.
- Keep `logs/file-inventory.json` regenerated with `python3 scripts/file-inventory.py`.
- Run `python3 scripts/file-inventory.py --check` before accepting inventory-sensitive changes.
- Keep `CODEBASE-GUIDE.md` focused on target-project code layout.
