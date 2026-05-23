# PrecodeOS File Inventory
<!-- ANCHOR: file-inventory -->

> AUTHORITY: Canonical technical inventory of PrecodeOS-owned files, file families, purposes, relationships, and maintenance expectations.
> NOT_AUTHORITY: Active memory, product decisions, task selection, feature requirements, implementation status, target-project architecture, generated evidence truth, or bead transition approval.
> LOAD_WHEN: Orienting a technical user or coding agent before changing PrecodeOS files, auditing file ownership, or tracing relationships between PrecodeOS surfaces.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.39
Last updated: 2026-05-22

## Purpose

This inventory is the technical dictionary for PrecodeOS files.

Use it to answer:

- why a file exists
- what it owns
- what it must not own
- when it should be loaded
- what reads it, writes it, or generates it
- how it relates to nearby files

This document is curated. Generated support lives in `logs/file-inventory.json` and is evidence only.

## License And Provenance

`LICENSE` holds the Apache-2.0 terms for open-source use. `NOTICE` preserves creator attribution, copyright ownership, the canonical site, and the PrecodeOS trademark notice. `TRADEMARK.md` owns brand-use guidance. Core source files use lightweight provenance and SPDX headers so adopters can reuse PrecodeOS while keeping license and origin visible.

## Reading Rules

- Start here when you need a technical map of PrecodeOS.
- Use `README.md` when you need the public document compass.
- Use `CODEBASE-GUIDE.md` for target-project layout guidance, not PrecodeOS internals.
- Do not treat generated outputs or inventory warnings as task selection.

## Quick Navigation

| Area | Files or families | Purpose |
|---|---|---|
| Active memory | `AGENT.md`, `DECISIONS.md`, `tasks/todo.md` | Always-loaded operating state. |
| Reader-facing docs | `docs/*.md` | Long-form human guides for philosophy, guided setup, support assistance, troubleshooting, beginner orientation, day-to-day use, Claude Code students, architecture review, and file-level navigation. |
| Project authority templates | `PRODUCT.md`, `PROJECT-CONTEXT.md`, `FEATURES.md`, `ACCEPTANCE.md`, `ARCHITECTURE.md`, `API.md`, `DATA-MODELS.md`, `SECURITY.md`, `CODEBASE-GUIDE.md` | Target-project owner files and reference templates. |
| Protocols | `tasks/reference/*.md` | Durable Precode rules and playbooks outside active memory, including agent routing. |
| Reusable templates | `tasks/templates/*.md` | Copyable student and workflow templates that produce source evidence, completion evidence, and public-safe cohort snapshots, not authority. |
| Execution docs | `tasks/todo.md`, `tasks/beads/*.md`, `tasks/prds/*.md` | Current work, bead contracts, and PRD shards. |
| Modes | `modes/*.md` | Navigator, explorer, builder, and review role contracts. |
| Adapters and shims | `adapters/*.md`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md` | Thin compatibility surfaces for AI coding tools. |
| Scripts | `scripts/*.py`, `scripts/*.sh` | Validation, state compilation, evidence recording, auditing, local hygiene checks, and generated reports. |
| Reviewed memory | `memory/`, `memory/cards/*.md` | Reviewed memory cards and templates; evidence only. |
| Maintainer cockpit | `_maintainer/MAINTAINER-NOTES.md`, `_maintainer/CHANGELOG.md`, `_maintainer/PRECODE-ALPHA-BETA-EVIDENCE-PLAN.md`, `_maintainer/PRECODE-ROADMAP.md`, `_maintainer/PUBLIC-REPO-IGNORE-MANIFEST.md`, `_maintainer/scripts/roadmap-maintenance.py` | Private maintainer index, history, alpha/beta evidence planning, roadmap, publishing-boundary policy, strategy, and automation for Dan/Recode-driven PrecodeOS maintenance; not active memory or public package authority. |
| Generated reports | `OS-HEALTH.md`, `PROGRESS.md`, `logs/*.md` | Human-readable generated evidence; not authority. |
| Generated sidecars | `logs/*.json`, `logs/*.jsonl`, `logs/progress.json`, `logs/run-contract.yaml` | Machine-readable generated evidence, execution profiles, and ledgers. |
| Generated output families | `logs/check-output/*`, `logs/scheduled-audit-output/*` | Timestamped command output and audit snapshots; local hygiene may report old unprotected entries as future archive candidates. |
| Workflows | `.github/workflows/*.yml` | Repository validation automation. |

## Core Relationship Map

## Maintainer-Only Files

`_maintainer/` is Dan Sears / Recode's private local maintainer cockpit for deciding how to improve the PrecodeOS package. It is excluded from the public repository by `.gitignore`, with publishing-boundary policy listed in `_maintainer/PUBLIC-REPO-IGNORE-MANIFEST.md`.

`_maintainer/MAINTAINER-NOTES.md` is the maintainer index. When Dan asks to maintain, analyze, or plan changes to PrecodeOS itself, agents read this file first, then load only the relevant maintainer roadmap, strategy, or reference files for the request.

`_maintainer/CHANGELOG.md` is maintainer-local human-readable project and document history for PrecodeOS. It is not public package authority or normal user-facing navigation.

`_maintainer/PRECODE-ALPHA-BETA-EVIDENCE-PLAN.md` is the maintainer-owned alpha and beta operating plan for using early cohorts to drive PrecodeOS use, feedback, and evidence. It is not public package authority or normal user workflow guidance.

`_maintainer/PRECODE-ROADMAP.md` is the canonical detailed maintainer roadmap for PrecodeOS ranking, source-derived roadmap themes, and prioritization.

`_maintainer/PUBLIC-REPO-IGNORE-MANIFEST.md` is the maintainer-only master list of files and patterns excluded from the public PrecodeOS package.

`_maintainer/scripts/roadmap-maintenance.py` is maintainer-only automation for roadmap cleanup after candidates are marked implemented.

Maintainer cockpit files may guide direct edits to public package files when Dan asks for Precode maintenance, but they must not be loaded as active memory, used as normal user workflow authority, or treated as bead activation, transition approval, public package authority, or generated evidence.

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
  -> Product Discovery Validation when worth-building is uncertain
  -> PRODUCT.md fit check
  -> Local Source Intake
  -> Alignment / Grilling
  -> destination PRD shard in tasks/prds/
  -> FEATURES.md compiled inventory
  -> journey bead proposal
  -> active bead
  -> logs/check-results.jsonl
  -> Closeout Evidence
```

PRDs own the destination. Beads own executable journey units. Logs prove what happened.

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
  -> scripts/precode_routing.py
  -> logs/authority-map.json
  -> logs/readiness.json
  -> logs/workflow-map.json
  -> logs/goal-frame.json
  -> logs/long-horizon-map.json
  -> logs/handoff-packet.json/md
  -> logs/memory-index.json/md
  -> logs/file-inventory.json
```

Generated sidecars summarize current state but do not replace source files.

### Adapters To Shared Commands

```text
AGENT.md
  -> adapters/ADAPTER-INDEX.md shared command surface
  -> tasks/reference/AGENT-ROUTING-PROTOCOL.md shared routing tiers
  -> adapters/*.md tool-specific notes
  -> AGENTS.md / CLAUDE.md / GEMINI.md / .github/copilot-instructions.md shims
```

Adapters and shims point back to the shared operating model. They must not become alternate Precode systems.

## Root And Reader Doc Dictionary

| File | Class | What it owns | How it relates |
|---|---|---|---|
| `AGENT.md` | active-memory | Shared AI coding agent operating model, command surface, active-memory contract, and verification gate. | Loaded every session; points to scripts, adapters, and the active-memory set. |
| `DECISIONS.md` | active-memory | Hard decisions, open questions, superseded decision context. | Consulted when product, architecture, or OS decisions are made or revisited. |
| `tasks/todo.md` | active-memory | Current bead pointer and current execution view. | Must match the one `in_progress` bead. |
| `README.md` | reference | Public GitHub landing page, beginner-first orientation, quickstart, and curated navigation for PrecodeOS. | Points to the Builder OS map, practical guides, reviewer surfaces, contribution policy, governance, trademark guidance, and this inventory for exhaustive navigation. |
| `LICENSE` | reference | Apache License 2.0 terms for use, modification, and distribution. | Root legal/provenance file; not active memory or task authority. |
| `NOTICE` | reference | Creator attribution, copyright ownership, canonical site, trademark notice, and distribution notice text. | Complements `LICENSE`; preserves "Created by Dan Sears / Recode", `https://www.precodeos.org`, and PrecodeOS trademark attribution. |
| `GOVERNANCE.md` | reference | Benevolent founder-maintainer governance model and official project authority. | Explains contribution decision rights, roadmap authority, forks, and maintainer delegation. |
| `CONTRIBUTING.md` | reference | Contribution rules and inbound = Apache-2.0 policy. | Guides proposed changes while preserving provenance, active-memory limits, and beginner-safe behavior. |
| `TRADEMARK.md` | reference | PrecodeOS trademark ownership, brand-use, allowed descriptive references, fork naming, and official-project identity guidance. | Clarifies that Apache-2.0 does not grant confusing brand use, trademark rights, or official-project identity. |
| `docs/PRECODE-MANIFESTO.md` | reference | Philosophical anchor for why Precode exists, who it serves, core values, and principles. | Guides positioning and fit for future OS changes without becoming operational authority. |
| `docs/PRECODE-OS-README.md` | reference | Beginner-first canonical explainer for Precode's Builder OS model, six-room surface map, plain-English project-folder model, and idea-to-evidence workflow. | Points users to the how-to guide, user guide, architecture overview, file inventory, and manifesto. |
| `_maintainer/CHANGELOG.md` | private-reference | Maintainer-local project and document history, including moved public document-history sections. | Provides maintainer history only; does not approve work, select tasks, replace owner files, act as generated evidence, or belong to public package navigation. |
| `docs/PRECODE-GUIDED-SETUP.md` | reference | Beginner-safe guided setup for pulling PrecodeOS from GitHub and adopting it into a new or existing project. | Explains manual package adoption, copy groups, exclusions, validation, and support-engineer setup flow while deferring canonical file ownership to this inventory. |
| `docs/PRECODE-SUPPORT-RUNBOOK.md` | reference | Public-safe support-engineer field guide for guiding first-time PrecodeOS adoption, user-owned intent capture, setup, first safe session, and repair routing. | Companion to guided setup, user guide, troubleshooting, file inventory, and recovery protocol; does not create product truth, approve PRDs, accept work, or approve transitions. |
| `docs/PRECODE-TROUBLESHOOTING.md` | reference | Symptom-first troubleshooting reference for setup, validation, active state, current bead, generated-report, copy, and first-session confusion. | Routes users, support engineers, and agents back to owner files, advisory checks, guided setup, and recovery protocol without becoming auto-repair policy. |
| `docs/HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md` | reference | Beginner-facing bridge from traditional software-building stages to Precode and AI coding agent workflows. | Teaches non-technical users how ideas become aligned, named, planned, built, verified, deployed, and learned from without replacing the user guide. |
| `docs/PRECODE-USER-GUIDE.md` | reference | Hands-on user playbook for operating Precode. | Prescriptive guide for non-technical users, including alignment, shared-language, AFK-candidate, test-strategy, and review prompts. |
| `docs/CLAUDE-CODE-FIELD-GUIDE.md` | reference | Beginner-facing public field guide for using Claude Code with PrecodeOS safely and confidently. | Companion to the user guide and prompt catalog; commit-eligible public documentation, not maintainer-only material. |
| `docs/PRECODE-ARCHITECTURE-OVERVIEW.md` | reference | Reviewer-facing architecture, principles, layer model, trust boundaries, and limitations. | Deep companion to the README and this inventory, including destination/journey, glossary evidence, and stale-artifact trust boundaries. |
| `docs/PRECODE-FILE-INVENTORY.md` | reference | Canonical technical file dictionary and relationship map. | Supported by `logs/file-inventory.json`. |
| `PRODUCT.md` | reference | Builder-facing product constitution: product promise, users and jobs, strategy and non-goals, current bets, success signals, design or voice pointers, and optional product-level Goal Frame. | Loaded for product planning, PRD shaping, PRD approval review, product drift checks, durable-intent orientation, and builder onboarding; not active memory or task selection. |
| `PROJECT-CONTEXT.md` | reference | Technical project constitution and integration boundaries. | Loaded when project context, integrations, or environment assumptions matter. |
| `OPERATING-CONSTRAINTS.md` | reference | Shared edit discipline, scope control, generated-output demotion, and reference-loading rules. | Always-loaded by `AGENT.md` as shared constraints. |
| `FEATURES.md` | reference | Compiled feature inventory and approved requirements. | Fed by approved PRD shards. |
| `ACCEPTANCE.md` | reference | Done checks and acceptance criteria. | Used when defining or reviewing verification gates. |
| `ARCHITECTURE.md` | reference | Route structure, flow shape, module placement, and auth boundaries. | Primary authority for architecture-affecting beads. |
| `API.md` | reference | API route rules, server-side boundaries, webhooks, and handler conventions. | Primary authority for API-affecting beads. |
| `DATA-MODELS.md` | reference | Schema fields, entities, data relationships, and semantic meaning. | Primary authority for schema-affecting beads. |
| `SECURITY.md` | reference | Security, privacy, auth, and sensitive-surface rules. | Primary authority for security-affecting beads. |
| `CODEBASE-GUIDE.md` | reference | Target-project repository layout and file placement conventions. | Not the PrecodeOS inventory; use this for app layout decisions. |
| `PROGRESS.md` | generated | Short user-facing progress snapshot for current work, completion picture, proof status, and attention prompts. | Evidence only; not active memory, task authority, or roadmap authority. |
| `OS-HEALTH.md` | generated | Generated OS health, warnings, loop metrics, and sidecar summary. | Evidence only; refreshed by `scripts/os-health.py`. |
| `PRECODE-HELP.md` | generated | Generated next-step guidance, load plan, context footprint, adaptive-depth summary, and files-in-play warning snapshot. | Evidence only; refreshed by `scripts/os-health.py` and not active memory. |

## Task And Reference Dictionary

| File or family | Class | What it owns | How it relates |
|---|---|---|---|
| `tasks/reference/*.md` | reference | Protocols and playbooks for specific Precode behaviors, with standard license and copyright metadata. | Loaded conditionally by active bead or workflow need. |
| `tasks/reference/PRD-PROTOCOL.md` | reference | Product Definition Gate, alignment summary, destination PRD rules, and PRD-to-bead requirements. | Governs PRD creation and approval before feature implementation. |
| `tasks/reference/LOCAL-SOURCE-INTAKE-PROTOCOL.md` | reference | Intake of local notes, docs, screenshots, client handoff artifacts, existing codebases, and research as evidence. | Feeds PRD-ready summaries without creating authority. |
| `tasks/reference/CLIENT-ENGAGEMENT-INTAKE-PROTOCOL.md` | reference | Client-engagement intake for external PRDs, design files, backend handoff plans, sprint plans, repo topology choices, and existing codebases. | Normalizes client materials into Precode owner files, PRD shards, and candidate beads without making external artifacts authority. |
| `tasks/reference/PRODUCT-DISCOVERY-VALIDATION-PROTOCOL.md` | reference | Advisory product-discovery validation before PRD shaping, including evidence ladder, assumption categories, current-workaround analysis, Core Four methods, Discovery Summary format, and `proceed | pause | narrow | kill` recommendations. | Used when worth-building uncertainty is higher than what-to-build uncertainty; feeds Local Source Intake or Idea-to-PRD as evidence only. |
| `tasks/reference/AGENT-ROUTING-PROTOCOL.md` | reference | Cross-agent model tier selection, context-budget discipline, delegation boundaries, and tool-routing preferences. | Shared policy for adapters and context engineering; provider-specific controls stay in `adapters/*.md`. |
| `tasks/reference/DECOMPOSITION-PROTOCOL.md` | reference | Journey bead slicing, vertical slice guidance, dependencies, AFK-candidate language, and not-a-bead-yet criteria. | Used before activating candidate beads. |
| `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md` | reference | Evidence tiers, test strategy, sensitive gates, and false-done warnings. | Informs checks, closeout, and OS Health warnings. |
| `tasks/reference/MEMORY-PROTOCOL.md` | reference | Reviewed filesystem memory rules and promotion path. | Governs `memory/cards/` and generated memory indexes. |
| `tasks/reference/UBIQUITOUS-LANGUAGE-PROTOCOL.md` | reference | Shared domain-language workflow, project-glossary card expectations, terminology freshness, and PRD/bead naming guidance. | Used during alignment, PRD shaping, module/interface naming, review, and glossary memory creation. |
| `tasks/reference/LOCAL-HYGIENE-PROTOCOL.md` | reference | Advisory local cleanup boundaries for truth, evidence, generated reports, bulky logs, caches, dry-run previews, and protected files. | Governs `scripts/local-hygiene-check.py`, `scripts/local-hygiene-dry-run.py`, and generated preview manifests. |
| `tasks/reference/RECOVERY-PROTOCOL.md` | reference | Beginner-safe recovery workflow for file damage, generated-report confusion, stale reports, active-state drift, missing proof, context loss, scope expansion, and approval confusion. | Canonical "I think I broke something" guide; informs user docs and next-step recovery prompts without authorizing destructive repair. |
| `tasks/reference/GOAL-FRAME-PROTOCOL.md` | reference | Reviewed durable-intent orientation, allowed owner-file locations, required fields, lifecycle, reaffirmation, and forbidden uses. | Governs Goal Frame sections in `PRODUCT.md`, PRDs, beads, or `DECISIONS.md`, plus `logs/goal-frame.json` and `scripts/goal-frame-check.py`. |
| `tasks/reference/PROMPT-PATTERNS.md` | reference | Copyable prompts for alignment, shared language, PRDs, decomposition, implementation, review, stale artifacts, and common Precode work. | Teaching aid; not authority over active memory or beads. |
| `tasks/templates/PRODUCT-IDEATION-WORKBOOK.md` | reference template | Student-facing product ideation workbook for Claude/Codex-assisted research, ideation, challenge, refinement, and Precode ingestion packet creation. | Source evidence only; ingest through Local Source Intake before promoting anything into `PRODUCT.md`, PRDs, decisions, or beads. |
| `tasks/templates/*.md` | reference template family | Reusable worksheets and guided artifacts outside active memory. | Templates may help create source evidence or proposals, but they do not approve work or become authority. |
| `tasks/beads/BEAD-SCHEMA.md` | reference | Bead schema, delegation mode, test strategy, review context, adaptive-depth fields, templates, closeout guidance, and review rules. | Defines shape for `tasks/beads/*.md`. |
| `tasks/beads/*.md` | execution contract | One durable journey unit of work, files in play, checks, stop conditions, delegation/test/review/adaptive-depth posture, and closeout. | One bead may be `in_progress`; active bead is pointed to by `tasks/todo.md`. |
| `tasks/prds/PRD-SHARD-SCHEMA.md` | reference | PRD directory rules, destination-shard guidance, and expected domain-language sections. | Supports `tasks/prds/*.md`. |
| `tasks/prds/*.md` | reference | Product destination shards, including domain language when terms matter. | Feed `FEATURES.md` and candidate journey beads. |

## Script Dictionary

Maintained scripts should carry lightweight provenance headers: version, last updated date, `Owner: PrecodeOS`, `Created by Dan Sears / Recode.`, and `SPDX-License-Identifier: Apache-2.0`.

| File | Purpose | Inputs | Outputs or side effects |
|---|---|---|---|
| `scripts/os_parser.py` | Shared markdown/frontmatter parsing helpers. | Markdown files. | Parser utilities for other scripts. |
| `scripts/os_compiler.py` | Compiles Precode state and sidecars while delegating router decisions to internal service modules. | Active memory, beads, logs, docs, delegation/test/review metadata, Goal Frames, run contracts, optional command guardrail input. | `logs/*.json`, `logs/run-contract.yaml`, generated progress/handoff/memory/file inventory surfaces, beginner-facing decisions, and advisory warnings. |
| `scripts/precode_routing.py` | Internal router service for next-step decisions, load plans, recovery routing, and context-footprint fields. | Active state passed from `os_compiler.py`, active bead, guardrail states, run-contract state, Goal Frame state. | Advisory next-step payload fields such as `single_next_protocol`, `load_plan`, `context_footprint`, and `why_not_more_context`; no standalone public command. |
| `scripts/os-health.py` | Renders OS Health. | Compiled state. | `OS-HEALTH.md`, `logs/os-health.json`. |
| `scripts/progress.py` | Renders the generated user-facing progress snapshot. | Compiled state. | `PROGRESS.md`, `logs/progress.json`. |
| `scripts/next-step.py` | Prints canonical generated next-step routing guidance with a plain user decision. | Compiled state. | Human-readable stdout or advisory JSON including `single_next_protocol`, `load_plan`, and `context_footprint`; no state mutation. |
| `scripts/loop-health.py` | Prints advisory Build Loop Health for the current work loop. | Compiled state plus the active bead contract. | Compact stdout, verbose dimensions, or advisory JSON; no state mutation, scoring, task selection, or approval. |
| `scripts/bead-depth-check.py` | Prints adaptive bead-depth advisory findings. | Active bead metadata, risk hints, checks, stop conditions. | JSON warnings; no state mutation. |
| `scripts/files-in-play-check.py` | Prints active-bead file mutation guardrail findings and optional command/edit-lock guidance. | Git changed paths, active bead `files_in_play`, optional `--command`, optional `--edit-lock`. | JSON warnings and plain continue/approval/stop guidance; no state mutation or command approval. |
| `scripts/run-contract-check.py` | Prints advisory run-contract findings. | Active bead Run Contract, files in play, verification tiers, recorded checks, and closeout. | JSON warnings about allowed actions, proof needed, approvals, and recovery; no state mutation or command approval. |
| `scripts/goal-frame-check.py` | Prints advisory Goal Frame findings. | Goal Frame sections in allowed owner files and compiled state. | JSON warnings; no state mutation, task selection, or approval. |
| `scripts/clarity-scenario-check.py` | Runs deterministic beginner-decision fixtures. | In-memory bead scenarios, adaptive-depth scenarios, and command-risk examples. | Advisory JSON pass/fail result; exits nonzero if expected decisions regress. |
| `scripts/local-hygiene-check.py` | Prints advisory Local Hygiene findings. | Compiled local hygiene state. | JSON to stdout; no cleanup mutation. |
| `scripts/local-hygiene-dry-run.py` | Previews future archive/delete actions without performing them. | Compiled local hygiene state. | `logs/local-hygiene-preview.json`, `logs/local-hygiene-preview.md`, and stdout. |
| `scripts/public-repo-check.py` | Checks public repository hygiene against the private ignore manifest and git ignore rules. | `_maintainer/PUBLIC-REPO-IGNORE-MANIFEST.md` when present, `.gitignore`, and git-tracked/untracked paths. | Advisory JSON for missing ignore rules, tracked ignored files, and untracked public candidates; no state mutation. |
| `scripts/validate-memory.sh` | Validates core Precode document invariants. | Required docs, todo, beads. | Pass/fail validation output. |
| `scripts/record-check.sh` | Runs a verification command and records evidence. | Command, active bead. | `logs/check-results.jsonl`, `logs/check-output/*`, closeout refresh. |
| `scripts/session-start.sh` | Starts a session and prints active context plus the canonical next-step router decision. | Active memory, bead state, and `scripts/next-step.py`. | Loop event, human-readable Context Pack, generated Router Decision display, and OS health refresh. |
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
| `adapters/ADAPTER-INDEX.md` | reference | Shared adapter command surface, routing-protocol pointer, and tool-neutral expectations. | Source of truth for adapter command parity and shared routing discipline. |
| `adapters/*.md` | reference | Tool-specific notes for Codex, Claude, Cursor, Gemini, Antigravity, and related agents. | Thin wrappers around `AGENT.md` that translate shared routing tiers into provider-native controls when available. |
| `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md` | reference shims | Auto-discovery compatibility for specific tools. | Must point back to `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`. |
| `modes/NAVIGATOR.md` | reference | Planning/navigation role guidance. | Used when choosing work or shaping tasks. |
| `modes/EXPLORER.md` | reference | Explorer role contract for bounded read-only repo inspection and source summarization. | Used when a narrow question needs cited repo facts before navigator, builder, or review decisions. |
| `modes/BUILDER.md` | reference | Implementation role guidance. | Used during scoped code or doc changes. |
| `modes/REVIEW.md` | reference | Review role guidance. | Used for code review, closeout, and acceptance checks. |
| `memory/REVIEWED-MEMORY-GUIDE.md` | reference | Reviewed memory directory guidance. | Points to memory protocol and card directory. |
| `memory/cards/MEMORY-CARD-FORMAT.md` | reference | Memory card format. | Defines reviewed memory card expectations. |
| `memory/cards/MEMORY-CARD-template.md` | reference template | Starter shape for reviewed memory cards. | Copied for approved memory cards. |
| `.github/workflows/precode-validate.yml` | workflow | GitHub Actions validation for Precode docs. | Runs read-only validation on pushes and pull requests. |

## Generated Evidence And Log Families

| File or family | Class | Purpose | Rule |
|---|---|---|---|
| `logs/LOG-EVIDENCE-TAXONOMY.md` | reference | Log taxonomy and generated-output rules. | Versioned reference doc. |
| `logs/check-results.jsonl` | generated evidence | Append-only check result ledger. | Evidence only. |
| `logs/check-output/*` | generated evidence family | Timestamped command output logs. | Document as a family, not individual files. |
| `logs/loop-runs.jsonl` | generated evidence | Session start, checkpoint, and close events. | Evidence only. |
| `logs/handoffs.jsonl` | generated evidence | Handoff events. | Evidence only. |
| `logs/agent-spend.jsonl` | generated evidence | Normalized agent spend rows. | Missing spend is unknown, not zero. |
| `logs/tool-runs.jsonl` | generated evidence | Non-check tool-run ledger. | Not verification unless also recorded as a check. |
| `logs/os-events.jsonl` | generated evidence | Compiled event stream. | Generated from logs. |
| `logs/os-health.json` | generated sidecar | Machine-readable OS Health payload. | Evidence only. |
| `logs/next-step.json` | generated sidecar | Machine-readable next-step guidance, load plan, single next protocol, and context footprint. | Evidence only; not task selection, transition approval, command approval, or active memory. |
| `logs/run-contract.json` and `logs/run-contract.yaml` | generated sidecar | Active bead run-contract execution profile. | Evidence only; not authority, command approval, or host-specific ZYAL contract. |
| `logs/authority-map.json` | generated sidecar | Authority contract index. | Evidence only. |
| `logs/adapter-index.json` | generated sidecar | Adapter command-surface summary. | Evidence only. |
| `logs/shim-index.json` | generated sidecar | Shim summary. | Evidence only. |
| `logs/readiness.json` | generated sidecar | Bead readiness and promotion state. | Evidence only. |
| `logs/orchestration-map.json` | generated sidecar | Intent orchestration summary. | Evidence only. |
| `logs/workflow-map.json` | generated sidecar | Workflow selection summary. | Evidence only. |
| `logs/goal-frame.json` | generated sidecar | Goal Frame status, freshness, required-field, and boundary warnings. | Advisory orientation only; not task selection, PRD approval, or bead activation. |
| `logs/long-horizon-map.json` | generated sidecar | Future/blocked/deferred work summary. | Evidence only. |
| `logs/handoff-packet.md/json` | generated report | Handoff context pack. | Orientation only; not transition approval. |
| `logs/learning-diary.md/jsonl` | generated report | Session learning digest and entries. | Not active memory. |
| `logs/memory-index.md/json` | generated report | Reviewed memory card index. | Search aid only. |
| `logs/file-inventory.json` | generated sidecar | Generated inventory metadata. | Maintenance aid only. |
| `logs/pattern-guidance.json` | generated sidecar | System design pattern guidance. | Advisory only. |
| `logs/scheduled-audit.md/json` | generated report | Scheduled audit summary. | Evidence only. |
| `logs/scheduled-audit-output/*` | generated evidence family | Timestamped audit helper outputs. | Document as a family, not individual files. |

## Maintenance Rules

- Add new PrecodeOS-owned files here when they become durable surfaces.
- Add generated outputs by family when they are timestamped or high-churn.
- Keep `logs/file-inventory.json` regenerated with `python3 scripts/file-inventory.py`.
- Run `python3 scripts/file-inventory.py --check` before accepting inventory-sensitive changes.
- Keep `CODEBASE-GUIDE.md` focused on target-project code layout.
