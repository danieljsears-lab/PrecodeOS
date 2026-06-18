# PrecodeOS Package File Inventory
<!-- ANCHOR: package-file-inventory -->

> AUTHORITY: User-facing technical inventory of public PrecodeOS package files, file families, purposes, relationships, and maintenance expectations.
> NOT_AUTHORITY: Private local file inventory, active memory, product decisions, task selection, feature requirements, implementation status, target-project architecture, generated evidence truth, or bead transition approval.
> LOAD_WHEN: Orienting a technical user, support helper, or coding agent before changing public PrecodeOS package files, auditing package file ownership, or tracing relationships between user-facing PrecodeOS surfaces.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.2.44
Last updated: 2026-06-18

## Purpose

This inventory is the technical dictionary for public PrecodeOS package files.

Use it to answer:

- why a file exists
- what it owns
- what it must not own
- when it should be loaded
- what reads it, writes it, or generates it
- how it relates to nearby files

This document is curated. Generated support lives in `logs/file-inventory.json` and is evidence only. Private local material is outside this user-facing package inventory and must not be inspected or required by public package tooling.

## License And Provenance

`LICENSE` holds the Apache-2.0 terms for open-source use. `NOTICE` preserves creator attribution, copyright ownership, the canonical site, and the PrecodeOS trademark notice. `TRADEMARK.md` owns brand-use guidance. `pyproject.toml` defines the optional local `precode` console entrypoint only; it does not publish, update, or install PrecodeOS into a target project. Core source files use lightweight provenance and SPDX headers so adopters can reuse PrecodeOS while keeping license and origin visible.

## Reading Rules

- Start here when you need a technical map of the public PrecodeOS package.
- Use `README.md` when you need the public document compass.
- Use `CODEBASE-GUIDE.md` for target-project layout guidance, not PrecodeOS internals.
- Do not use this document to inventory private local material.
- Do not treat generated outputs or inventory warnings as task selection.

## Quick Navigation

| Area | Files or families | Purpose |
|---|---|---|
| Active memory | `AGENT.md`, `DECISIONS.md`, `tasks/todo.md` | Always-loaded operating state. |
| Reader-facing docs | `docs/*.md` | Human guides for the Daily Cockpit, philosophy, guided setup, support assistance, troubleshooting, beginner orientation, day-to-day use, Claude Code students, architecture review, and file-level navigation. |
| Public generated docs site | `docs-html/*.html` | Committed HTML reading surface generated from `docs/*.md`; easier to navigate, but not authority. |
| Project authority templates | `PRODUCT.md`, `PROJECT-CONTEXT.md`, `FEATURES.md`, `ACCEPTANCE.md`, `ARCHITECTURE.md`, `API.md`, `DATA-MODELS.md`, `SECURITY.md`, `CODEBASE-GUIDE.md` | Target-project owner files and reference templates. |
| Protocols | `tasks/reference/*.md` | Durable Precode rules and playbooks outside active memory, including agent routing, skill playbooks, and copyable prompt patterns. |
| Reusable templates | `tasks/templates/*.md` | Copyable student and workflow templates that produce source evidence, completion evidence, and public-safe cohort snapshots, not authority. |
| Execution docs | `tasks/todo.md`, `tasks/beads/*.md`, `tasks/prds/*.md` | Current work, bead contracts, and PRD shards. |
| Generated PRD review surface | `tasks/prds-html/*.html` | Committed static HTML review pages generated from non-template PRD shards, including export-only Acceptance Oracle Matrix proposal controls; easier to inspect, but not authority. |
| Modes | `modes/*.md` | Navigator, explorer, builder, and review role contracts. |
| Adapters and shims | `adapters/*.md`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md` | Thin compatibility surfaces for AI coding tools; `adapters/ADAPTER-INDEX.md` owns the narrow compatibility shim matrix. |
| Project evidence guide | `project-evidence/PROJECT-EVIDENCE-GUIDE.md` | Marker and user guidance for target-project raw evidence such as notes, documents, screenshots, research, and links. |
| Scripts and local CLI | `scripts/*.py`, `scripts/*.sh`, `pyproject.toml` | Validation, state compilation, evidence recording, bounded Ralph attempts, auditing, local hygiene checks, generated reports, and the optional local `precode` command facade. |
| Reviewed memory | `memory/`, `memory/cards/*.md` | Reviewed memory cards and templates; evidence only. |
| Generated reports | `OS-HEALTH.md`, `PROGRESS.md`, `logs/*.md` | Human-readable generated evidence, including the Work Graph Report; not authority. |
| Generated sidecars | `logs/*.json`, `logs/*.jsonl`, `logs/progress.json`, `logs/run-contract.yaml` | Machine-readable generated evidence, execution profiles, and ledgers. |
| Generated output families | `logs/check-output/*`, `logs/scheduled-audit-output/*`, `logs/os-checkpoints/*` | Timestamped command output, audit snapshots, and explicit scoped OS checkpoints; local hygiene may report old unprotected entries as future archive candidates. |
| GitHub support surfaces | `.github/workflows/*.yml`, `.github/PULL_REQUEST_TEMPLATE.md` | Repository validation automation and pull-request evidence prompts. |

## Context Layer Matrix

Use this matrix when an agent, adapter, skill playbook, generated report, memory search, source-intake artifact, or maintainer-local note could be confused with current authority.

| Layer | Authority level | Load trigger | Allowed use | Forbidden use | Promotion path |
|---|---|---|---|---|---|
| Active memory | Current operating state | Always load at session start for normal Precode work. | Orient the agent to the shared operating model, current decisions, and active bead pointer. | Do not expand through adapters, skill playbooks, generated reports, reviewed memory, raw evidence, or maintainer notes. | Active-memory changes require explicit package-maintenance review and the relevant owner-file/protocol follow-through. |
| Owner/reference files | Durable domain authority | Load when the task affects the file's domain. | Govern product, project, acceptance, architecture, API, data, security, codebase, public docs, and protocol decisions. | Do not use them as active task selection unless the active bead or workflow calls for them. | Amend the owning file after user or maintainer review; requirements also flow through PRDs and compiled `FEATURES.md` when applicable. |
| Execution contracts | Current approved work authority | Load when planning, building, reviewing, closing, or transitioning work. | Bound one active bead, its primary authority, files in play, checks, stop conditions, PRD links, and proof. | Do not use old, proposed, closed, or generated handoff material to activate work. | Proposed work becomes an approved bead only through the normal human-gated transition path. |
| Protocols | Durable process authority | Load when a workflow, risk, or prompt invokes the protocol. | Define repeatable Precode rules for intake, planning, execution, verification, recovery, release, setup, collaboration, and extension behavior. | Do not load every protocol by default or let protocol text override active bead scope. | Repeated process lessons may be promoted through a reviewed protocol update. |
| Adapters and shims | Host-tool compatibility guidance | Load when the coding tool auto-discovers a shim or when switching tools. | Translate shared Precode rules into tool-specific startup, command, routing, handoff guidance, and the narrow compatibility shim matrix. | Do not create alternate active memory, host-specific authority trees, task approval, broad host support promises, native rule-directory proliferation, or tool-owned operating models. | Repeated tool gaps may be promoted into `adapters/*.md`, `ADAPTER-INDEX.md`, or an extension review. |
| Skill playbooks | Read-only invocation contract | Load when the user names a skill-style Precode workflow or review. | Tell a host agent what owner protocols/files to inspect, what output to return, and what gates to preserve. | Do not edit files, approve work, activate beads, run mutating commands, install skills, or become a second operating model. | Stable repeated invocation patterns may be promoted through `SKILL-PLAYBOOK-PROTOCOL.md` and the owner protocol. |
| Generated reports and sidecars | Generated evidence | Load when inspecting state, health, routing hints, reports, or compiled sidecars. | Summarize source Markdown, logs, checks, warnings, and next-step evidence for human review. | Do not treat generated output as active memory, authority, task approval, command approval, or transition approval. | Repair source state and regenerate; gaps may become follow-up beads, validator improvements, or protocol/docs updates. |
| Reviewed memory | Reviewed evidence and citation source | Load when the user asks, when a protocol says memory may help, or when durable lessons are relevant. | Orient future sessions with reviewed lessons, preferences, vocabulary, risks, and source pointers. | Do not store decisions, choose work, override active memory, replace PRDs, or treat generated indexes as authority. | Decisions go to `DECISIONS.md`; requirements to PRDs/`FEATURES.md`; domain facts to owner files; process lessons to protocols. |
| Raw/source evidence | Unreviewed or intake evidence | Load only when the user names source material or an intake workflow applies. | Inspect read-only, summarize stable facts, assumptions, conflicts, privacy concerns, candidate requirements, and likely owner files. | Do not treat notes, screenshots, research, external issues, PRs, transcripts, or generated summaries as product truth or permission to code. | Promote reviewed conclusions through Local Source Intake, PRDs, `DECISIONS.md`, owner files, or candidate beads. |
| Maintainer-local context | Private package-maintenance planning context | Load only for Dan's PrecodeOS package-maintenance work. | Guide roadmap, strategy, public/private boundary review, changelog follow-through, and package-maintainer planning. | Do not make `_maintainer/` public package authority, normal user-session input, generated evidence, or setup dependency. | Record maintainer history in `_maintainer/`; public package changes still require public owner-file/protocol/docs follow-through. |

Manual promotion is the rule: decisions go to `DECISIONS.md`, product requirements to PRDs and compiled `FEATURES.md`, architecture/API/data/security facts to their owner files, execution work to approved beads, repeated process lessons to protocols, adapters, or skill playbooks, and maintainer roadmap history to `_maintainer/` only.

## Core Relationship Map

## Private Local Material

Private local planning, strategy, and review material is intentionally outside the public package inventory. Public package docs and scripts must remain complete and functional when that material is absent.

### Package Surface Authority Map

```text
Markdown authority contracts
  -> scripts/os_compiler.py
  -> logs/authority-map.json
  -> surface_classes and docs_by_surface
```

`logs/authority-map.json` is a generated orientation sidecar. It groups parsed authority contracts by package surface class and names class-level boundaries for active memory, owner/reference docs, protocols, PRDs, beads, templates, adapters, shims, generated public HTML, generated reports and sidecars, scripts, workflows, and maintainer-private surfaces.

The map helps contributors and agents distinguish authority, evidence, compatibility, generated reading surfaces, and private maintainer material. It does not replace this inventory, source Markdown, active memory, PRDs, beads, protocols, maintainer review, or human approval. Public generated authority-map detail excludes `_maintainer/` file inventory; private maintainer files remain local maintainer context only.

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
  -> Product Ideation Workbook / Conviction Packet when a first-time rough idea needs pre-repo product thinking
  -> Product Discovery Validation when worth-building is uncertain
  -> PRODUCT.md fit check
  -> Local Source Intake
  -> Alignment / Grilling
  -> destination PRD shard in tasks/prds/
  -> FEATURES.md compiled inventory
  -> Architecture Shaping when risk-triggered
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
  -> read-only memory search and citation prompts
  -> optional promotion to DECISIONS.md, PRD, or authority doc
```

The diary is generated learning. Memory cards are reviewed evidence. Search results and indexes are generated evidence. Owner files hold authority.

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
  -> logs/work-graph.json/md
```

Generated sidecars summarize current state but do not replace source files.

Bootstrap Confidence is separate from compiled current-state sidecars because it compares a PrecodeOS package source with an adoption target before the target is necessarily a valid Precode repo. Existing Repo Intake is the next first-fork branch for targets that already have app code, docs, CI, product history, or active work. The supervised setup plan is the final non-mutating checklist layer after manifest preview. Supervised setup apply is the narrow mutating layer for explicitly approved setup-plan copy actions in empty or nearly empty targets only. Bootstrap Closeout adds non-mutating existing-project adaptation planning, existing-Precode package upgrade preview, support-assisted recovery guidance, and an explicit action-ID apply path for missing package-owned files only.

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
| `AGENT.md` | active-memory | Shared AI coding agent operating model, command surface, active-memory contract, stuck-user recovery trigger, and verification gate. | Loaded every session; points to scripts, adapters, the active-memory set, and the Recovery Protocol when a user says `I am stuck, help me`. |
| `DECISIONS.md` | active-memory | Hard decisions, open questions, superseded decision context. | Consulted when product, architecture, or OS decisions are made or revisited. |
| `tasks/todo.md` | active-memory | Current bead pointer and current execution view. | Must match the one `in_progress` bead. |
| `README.md` | reference | Public GitHub landing page, beginner-first orientation, quickstart, and curated navigation for PrecodeOS. | Points to the Builder OS map, practical guides, reviewer surfaces, contribution policy, governance, trademark guidance, and this inventory for exhaustive navigation. |
| `LICENSE` | reference | Apache License 2.0 terms for use, modification, and distribution. | Root legal/provenance file; not active memory or task authority. |
| `NOTICE` | reference | Creator attribution, copyright ownership, canonical site, trademark notice, and distribution notice text. | Complements `LICENSE`; preserves "Created by Dan Sears / Recode", `https://www.precodeos.org`, and PrecodeOS trademark attribution. |
| `GOVERNANCE.md` | reference | Benevolent founder-maintainer governance model and official project authority. | Explains contribution decision rights, roadmap authority, forks, and maintainer delegation. |
| `CONTRIBUTING.md` | reference | Contribution rules and inbound = Apache-2.0 policy. | Guides proposed changes while preserving provenance, active-memory limits, and beginner-safe behavior. |
| `TRADEMARK.md` | reference | PrecodeOS trademark ownership, brand-use, allowed descriptive references, fork naming, and official-project identity guidance. | Clarifies that Apache-2.0 does not grant confusing brand use, trademark rights, or official-project identity. |
| `docs/PRECODE-MANIFESTO.md` | reference | Philosophical anchor for why Precode exists, who it serves, core values, and principles. | Guides positioning and fit for future OS changes without becoming operational authority. |
| `docs/PRECODE-DAILY-COCKPIT.md` | reference | Student-first daily command, prompt, stuck recovery, Bugfix Spec Lane pointer for small repairs, no-engineer fallback prompt pointer, report, check, and learning reference for normal PrecodeOS work. | First public HTML docs entry; summarizes daily action and links to deeper guides and protocols without replacing them. |
| `docs/PRECODE-OS-README.md` | reference | Beginner-first canonical explainer for Precode's Builder OS model, six-room surface map, plain-English project-folder model, and idea-to-evidence workflow. | Points users to the how-to guide, user guide, architecture overview, file inventory, and manifesto. |
| `docs/PRECODE-GUIDED-SETUP.md` | reference | Beginner-safe guided setup for pulling PrecodeOS from GitHub and adopting it into a new or existing project. | Explains manual package adoption, copy groups, exclusions, validation, and support-engineer setup flow while deferring canonical file ownership to this inventory. |
| `docs/PRECODE-SUPPORT-RUNBOOK.md` | reference | Public-safe support-engineer field guide for guiding first-time PrecodeOS adoption, user-owned intent capture, setup, first safe session, parallel environment/scaffold readiness, stuck-user diagnosis, no-engineer fallback prompt routing, and repair routing. | Companion to guided setup, user guide, troubleshooting, file inventory, and recovery protocol; does not create product truth, approve PRDs, accept work, interpret feedback, approve repair, or approve transitions. |
| `docs/PRECODE-TROUBLESHOOTING.md` | reference | Symptom-first troubleshooting reference for setup, validation, active state, current bead, generated-report, copy, stable-fix and Bugfix Spec Lane routing, fallback prompt, and first-session confusion. | Routes users, support engineers, and agents back to owner files, advisory checks, guided setup, prompt patterns, and recovery protocol without becoming auto-repair policy. |
| `docs/HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md` | reference | Beginner-facing bridge from traditional software-building stages to Precode and AI coding agent workflows. | Teaches non-technical users how ideas become aligned, named, planned, built, verified, deployed, and learned from without replacing the user guide. |
| `docs/PRECODE-USER-GUIDE.md` | reference | Hands-on user playbook for operating Precode. | Prescriptive guide for non-technical users, including alignment, shared-language, AFK-candidate, test-strategy, review prompts, and no-engineer fallback prompt discoverability. |
| `docs/CLAUDE-CODE-FIELD-GUIDE.md` | reference | Beginner-facing public field guide for using Claude Code with PrecodeOS safely and confidently. | Companion to the user guide and prompt catalog; cross-links common sideways moments to the shared fallback prompt pack; commit-eligible public documentation, not private local material. |
| `docs/PRECODE-ARCHITECTURE-OVERVIEW.md` | reference | Reviewer-facing architecture, principles, layer model, trust boundaries, and limitations. | Deep companion to the README and this inventory, including destination/journey, glossary evidence, and stale-artifact trust boundaries. |
| `docs/PRECODE-PACKAGE-FILE-INVENTORY.md` | reference | User-facing package file dictionary and relationship map for public PrecodeOS files. | Supported by `logs/file-inventory.json`; private local material remains outside public inventory. |
| `docs-html/*.html` | generated public docs | Static HTML reading surface generated from `docs/*.md`, including a curated compass and per-page navigation. | Commit-eligible package artifact for easier reading; does not replace Markdown authority, approve work, or become active memory. |
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
| `project-evidence/PROJECT-EVIDENCE-GUIDE.md` | reference | User guidance for root-level raw project evidence storage. | Keeps notes, documents, screenshots, research, and links project-owned and evidence-only until reviewed conclusions are promoted through Local Source Intake. |
| `PROGRESS.md` | generated | Short user-facing progress snapshot for current work, completion picture, proof status, and attention prompts. | Evidence only; not active memory, task authority, or roadmap authority. |
| `OS-HEALTH.md` | generated | Generated OS health, Doctor Dashboard diagnostics, plain-English triage labels, warnings, loop metrics, and sidecar summary. | Evidence only; refreshed by `scripts/os-health.py`; Doctor Dashboard explains warning sources but does not choose tasks, approve transitions, or replace `scripts/next-step.py`. |
| `PRECODE-HELP.md` | generated | Generated next-step guidance, load plan, context footprint, adaptive-depth summary, decision reasons, shortest next action, and files-in-play warning snapshot. | Evidence only; refreshed by `scripts/os-health.py` and not active memory. |

## Task And Reference Dictionary

| File or family | Class | What it owns | How it relates |
|---|---|---|---|
| `tasks/reference/*.md` | reference | Protocols and playbooks for specific Precode behaviors, with standard license and copyright metadata. | Loaded conditionally by active bead or workflow need. |
| `tasks/reference/PRD-PROTOCOL.md` | reference | Product Definition Gate, alignment summary, destination PRD rules, advisory requirements gap/conflict review, and PRD-to-bead requirements. | Governs PRD creation, pre-approval requirements review, and approval before feature implementation. |
| `tasks/reference/LOCAL-SOURCE-INTAKE-PROTOCOL.md` | reference | Intake of local notes, docs, screenshots, client handoff artifacts, existing codebases, and research as evidence. | Feeds PRD-ready summaries without creating authority. |
| `tasks/reference/CLIENT-ENGAGEMENT-INTAKE-PROTOCOL.md` | reference | Client-engagement intake for external PRDs, design files, backend handoff plans, sprint plans, repo topology choices, and existing codebases. | Normalizes client materials into Precode owner files, PRD shards, and candidate beads without making external artifacts authority. |
| `tasks/reference/PRODUCT-DISCOVERY-VALIDATION-PROTOCOL.md` | reference | Advisory product-discovery validation before PRD shaping, including MVP-ready conviction vs. validated demand, evidence ladder, assumption categories, current-workaround analysis, Core Four methods, Discovery Summary format, and `proceed`, `pause`, `narrow`, or `kill` recommendations. | Used when worth-building uncertainty is higher than what-to-build uncertainty; treats guided research as weak evidence unless paired with behavior; feeds Local Source Intake or Idea-to-PRD as evidence only. |
| `tasks/reference/ARCHITECTURE-SHAPING-PROTOCOL.md` | reference | Risk-triggered architecture-shaping interview, Architecture Brief evidence format, routing rules, stop conditions, and PRD-to-bead handoff guidance. | Used after PRD approval and before bead proposals when auth, data, API, integration, dependency, migration, workflow, or multi-system risk should be visible before implementation planning. |
| `tasks/reference/BOOTSTRAP-CONFIDENCE-PROTOCOL.md` | reference | Read-only first-run confidence workflow for inspecting a PrecodeOS package source and target project before setup mutation. | Used before guided setup or support-assisted adoption; governs `scripts/bootstrap-check.py`, source/target identity, public file groups, exclusions, conflicts, and first safe next action. |
| `tasks/reference/EXISTING-REPO-INTAKE-PROTOCOL.md` | reference | Read-only existing-repository intake workflow for the existing-app branch at the first PrecodeOS adoption fork. | Used after Bootstrap Confidence when the target already has app code, docs, CI, product history, or active work; governs `scripts/existing-repo-intake.py`, repo-shape evidence, likely checks as future hints, owner-file gaps, conflicts, and mutation stop conditions. |
| `tasks/reference/INSTALL-UPDATE-MANIFEST-PROTOCOL.md` | reference | Non-mutating install/update manifest and dry-run preview workflow for explaining candidate setup actions before target-project mutation. | Used after Bootstrap Confidence and before any supervised setup mutation; governs `bootstrap-check.py --preview-manifest`, preview action categories, generated-evidence boundaries, stable-fix repair routing, and deferred installer/update semantics. |
| `tasks/reference/SUPERVISED-SETUP-PLAN-PROTOCOL.md` | reference | Non-mutating supervised setup-plan workflow for turning Bootstrap Confidence and manifest preview evidence into a visible setup checklist before target-project mutation. | Used after manifest preview and before any manual setup action; governs `bootstrap-check.py --supervised-setup-plan`, action IDs, approval gates, exclusions, blockers, validation steps, and evidence-only boundaries. |
| `tasks/reference/SUPERVISED-SETUP-APPLY-PROTOCOL.md` | reference | Approval-gated setup mutation workflow for copying explicitly approved PrecodeOS setup-plan paths into empty or nearly empty target projects. | Governs `bootstrap-check.py --supervised-setup-plan --apply-supervised-setup --approve-action <SP-ID>`, allowed copy actions, refusals, validation next steps, and non-installer boundaries. |
| `tasks/reference/BOOTSTRAP-CLOSEOUT-PROTOCOL.md` | reference | Final staged closeout contract for existing-project adaptation planning, package upgrade preview, support-assisted recovery guidance, and missing-package-file copy gates. | Governs `bootstrap-check.py --existing-project-adaptation-plan`, `--upgrade-preview`, `--recovery-guidance`, and `--upgrade-preview --apply-upgrade-preview --approve-action <UP-ID>` while preserving no broad installer, dirty-file overwrite, owner-file adaptation approval, hooks/CI mutation, release channels, package-manager behavior, or rollback automation. |
| `tasks/reference/AGENT-ROUTING-PROTOCOL.md` | reference | Cross-agent model tier selection, context-budget discipline, delegation boundaries, and tool-routing preferences. | Shared policy for adapters and context engineering; provider-specific controls stay in `adapters/*.md`. |
| `tasks/reference/SKILL-PLAYBOOK-PROTOCOL.md` | reference | Skill playbook strategy, implemented prompt playbooks, Ask Precode Docs Skill guidance, Product Discovery Interview Skill guidance, Small Team Collaboration Lane Skill guidance, Review / Acceptance Skill guidance, Accessibility Advisor Fit Interview guidance, Requirements Gap And Conflict Review Skill guidance, Maintainer Package Review Skill guidance, Skill / Extension Review Skill guidance, Product Conviction Packet Skill guidance, v1 skill candidates, prompt-playbook boundaries, manifest contract, hidden-authority guardrails, candidate backlog, and alternatives. | Owns the implemented Ask Precode Docs Skill, Workflow Selection Skill, Product Discovery Interview Skill, Small Team Collaboration Lane Skill, Review / Acceptance Skill, Accessibility Advisor Fit Interview, Requirements Gap And Conflict Review Skill, Maintainer Package Review Skill, Skill / Extension Review Skill, and future skill-style prompt playbook review; records No-Engineer Fallback Prompt Pack as implemented outside the skill set; keeps skills read-only, evidence-only, and subordinate to owner protocols; defines Product Conviction as a guided product-coach interview that stops at evidence and Local Source Intake handoff. |
| `tasks/reference/SEMANTIC-CHANGE-PROPOSAL-PROTOCOL.md` | reference | Semantic-change proposal triggers, required fields, maintainer review outcomes, and non-authority boundaries for trust-affecting PrecodeOS package changes. | Used before implementation or merge when changes may alter active memory, authority ownership, generated-output demotion, package install/update boundaries, governance or contribution semantics, or beginner-facing safety language. |
| `tasks/reference/DECOMPOSITION-PROTOCOL.md` | reference | Journey bead slicing, vertical slice guidance, dependencies, AFK-candidate language, and not-a-bead-yet criteria. | Used before activating candidate beads. |
| `tasks/reference/TEAM-COLLABORATION-PROTOCOL.md` | reference | Small Team Collaboration Lane invocation, coordinator and teammate role boundaries, branch/worktree-isolated parallel bead guidance, review/merge evidence, GitHub evidence boundaries, and re-entry rules. | Used when 2-5 people work on the same product build; preserves one active bead per checkout and keeps team notes, PRs, generated handoffs, and branch status as evidence until reviewed and promoted. |
| `tasks/reference/SYSTEM-DESIGN-PATTERN-PROTOCOL.md` | reference | Beginner-facing defaults for direct changes, adapter/facade boundaries, state flows, strategy boundaries, audit trails, auth/access boundaries, and deep modules. | Used before coding when a feature's implementation shape, owner file, simpler alternative, or proof path should be explicit. |
| `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md` | reference | Evidence tiers, test strategy, stable-fix proof expectations, Bugfix Spec Lane regression proof, opt-in accessibility advisory evidence shape, sensitive gates, and false-done warnings. | Informs checks, closeout, stable-fix eligibility, accessibility advisory completeness after invocation, and OS Health warnings. |
| `tasks/reference/OS-INTEGRITY-PROTOCOL.md` | reference | PrecodeOS-owned surface classes, protected-source checkpoint expectations, OS-integrity check behavior, scoped restore limits, and generated-evidence boundaries. | Governs `scripts/os-integrity-check.py`, `scripts/os-checkpoint.py`, and strict pre-commit protection for OS-owned source surfaces. |
| `tasks/reference/RELEASE-READINESS-PROTOCOL.md` | reference | User-project release-readiness lane, Release Candidate Evidence Profile, shipping evidence expectations, optional accessibility advisory status when invoked or required, stable-fix release boundaries, approval gates, rollback or blocked escape notes, and post-release review prompts. | Used before user-facing shipping risk; prepares evidence profiles and approval questions without deploying, approving release, mutating external systems, accepting review, certifying accessibility compliance, or activating the next bead. |
| `tasks/reference/REVIEW-LANES-PROTOCOL.md` | reference | Optional Security and Release / Docs Freshness Review Lanes for one active bead, including required inputs, output fields, findings, missing proof, acceptance questions, recommendations, approvals still required, and promotion paths. | Produces advisory review input only; does not accept implementation, approve review, approve release, certify security or compliance, create follow-up tasks, rewrite owner files, mutate GitHub, mutate external systems, or become a persona system. |
| `tasks/reference/BEAD-BUILD-JOURNAL-PROTOCOL.md` | reference | Generated bead build journal rules, evidence sources, Daily Cockpit surfacing, and conservative uncertainty handling. | Governs `logs/bead-build-journal.md/jsonl` behavior. |
| `tasks/reference/RALPH-LOOP-PROTOCOL.md` | reference | Bounded Ralph attempt lifecycle, retry budget, validator-set expectations, generated attempt evidence, stop decisions, and hidden-authority guardrails. | Governs optional Ralph frontmatter in beads, `scripts/ralph-loop.py`, and `logs/ralph-attempts.jsonl` / `logs/ralph-summary.md`. |
| `tasks/reference/MEMORY-PROTOCOL.md` | reference | Reviewed filesystem memory rules, generated index/search behavior, citation expectations, demotion warnings, and manual promotion path. | Governs `memory/cards/`, `scripts/memory-check.py`, and generated memory indexes without expanding active memory. |
| `tasks/reference/UBIQUITOUS-LANGUAGE-PROTOCOL.md` | reference | Shared domain-language workflow, project-glossary card expectations, terminology freshness, and PRD/bead naming guidance. | Used during alignment, PRD shaping, module/interface naming, review, and glossary memory creation. |
| `tasks/reference/LOCAL-HYGIENE-PROTOCOL.md` | reference | Advisory local cleanup boundaries for truth, evidence, generated reports, bulky logs, caches, dry-run previews, protected generated evidence, and v2 preview classifications. | Governs `scripts/local-hygiene-check.py`, `scripts/local-hygiene-dry-run.py`, `scripts/local-hygiene-dry-run.py --self-test`, and generated preview manifests. |
| `tasks/reference/RECOVERY-PROTOCOL.md` | reference | Beginner-safe recovery workflow for stuck-user diagnosis, file damage, stable-fix eligibility, Bugfix Spec Lane field contract, generated-report confusion, stale reports, active-state drift, missing proof, context loss, scope expansion, and approval confusion. | Canonical `I am stuck, help me` and "I think I broke something" guide; owns the recovery boundary for Bugfix Spec Lane and No-Engineer Fallback Prompt Pack usage; informs active-memory guidance, user docs, and next-step recovery prompts without authorizing destructive repair. |
| `tasks/reference/GOAL-FRAME-PROTOCOL.md` | reference | Reviewed durable-intent orientation, allowed owner-file locations, required fields, lifecycle, fit checks, reaffirmation, and forbidden uses. | Governs Goal Frame sections in `PRODUCT.md`, PRDs, beads, or `DECISIONS.md`, plus `logs/goal-frame.json` and `scripts/goal-frame-check.py`. |
| `tasks/reference/PROMPT-PATTERNS.md` | reference | Copyable prompts for guided Precode Idea Coach interviews, pre-repo idea coaching, Conviction Packet handoff, alignment, shared language, PRDs, Requirements Gap And Conflict Review, Accessibility Advisor Fit Interview, Bugfix Spec Lane, Review Lanes, decomposition, Small Team Collaboration Lane invocation, Maintainer Package Review Skill invocation, implementation, review, stuck recovery, No-Engineer Fallback Prompt Pack, Review / Acceptance Skill invocation, Skill / Extension Review Skill invocation, stale artifacts, and common Precode work. | Teaching aid; not authority over active memory, PRD approval, owner-file rewrites, beads, extension approval, accessibility compliance certification, review-lane findings, repair approval, app-code change approval, rollback, setup/update mutation, transition approval, team merge approval, GitHub mutation, external mutation, package-maintenance approval, roadmap or backlog creation, or acceptance decisions. |
| `tasks/templates/PRODUCT-IDEATION-WORKBOOK.md` | reference template | Default student and builder product ideation workbook for Claude/Cowork/Claude Code/Codex-assisted guided product-coach interviews, builder-lens selection, research, challenge, evidence-strength review, optional visible-iteration/MVE framing, candidate capability matrices, and Conviction Packet / Precode ingestion packet creation. | Source evidence only; ingest through Local Source Intake before promoting anything into `PRODUCT.md`, PRDs, decisions, or beads; workbook output is not a roadmap, backlog, PRD, product approval, bead, or permission to code. |
| `tasks/templates/STUDENT-IDEA-TO-MVE-WORKBOOK.md` | reference template | Legacy pointer for the former experimental Student Idea To MVE workbook; routes older student, instructor, mentor, or support references to the default Product Ideation Workbook. | Compatibility surface only; does not define a separate student workflow, implementation handoff, PRD approval, bead activation, or permission to code. |
| `tasks/templates/STUDENT-EXPERIENCE-INGESTION-PACKET.md` | reference template | Student-facing Experience handoff packet combining an approved bootcamp PRD input, design-tool brief, visual core-spine artifacts, Core Spine Gate status, target-user feedback, support engineer readiness prompt, demo-evidence reminders, and Claude Code bead-creation prompts. | Context for creating a bounded Precode bead and checking parallel environment/scaffold readiness; not product approval, bead activation, implementation authority, prototype acceptance, support-owned scope, or permission to code. |
| `tasks/templates/STUDENT-COMPLETION-EVIDENCE-PACKET.md` | reference template | Student-facing completion evidence packet for cohort demos, ownership, proof, Experience review notes, and next-direction evidence. | Evidence only; does not prove validation, approve product changes, accept implementation, or replace review decisions. |
| `tasks/templates/*.md` | reference template family | Reusable worksheets and guided artifacts outside active memory. | Templates may help create source evidence or proposals, but they do not approve work or become authority. |
| `tasks/beads/BEAD-SCHEMA.md` | reference | Bead schema, delegation mode, test strategy, review context, adaptive-depth fields, templates, closeout guidance, and review rules. | Defines shape for `tasks/beads/*.md`. |
| `tasks/beads/*.md` | execution contract | One durable journey unit of work, files in play, checks, stop conditions, delegation/test/review/adaptive-depth posture, and closeout. | One bead may be `in_progress`; active bead is pointed to by `tasks/todo.md`. |
| `tasks/prds/PRD-SHARD-SCHEMA.md` | reference | PRD directory rules, destination-shard guidance, and expected domain-language sections. | Supports `tasks/prds/*.md`. |
| `tasks/prds/*.md` | reference | Product destination shards, including domain language when terms matter. `PRD-009` owns the Release Candidate Evidence Lane profile as a human-authored release-readiness profile, not generated proof or release approval. `PRD-010` owns Supervised Setup Apply v1 as an approval-gated fresh-target setup copy slice, not a package manager or broad installer. `PRD-011` owns Local Hygiene v2 preview hardening as non-mutating classification and protection behavior, not cleanup approval. `PRD-012` owns the Precode Doctor Dashboard and plain-English triage labels as generated OS Health diagnostics, not task selection, approval, or `precode doctor` command behavior. `PRD-013` owns the optional local `precode` CLI wrapper as a facade over trusted commands, not package-manager, release-channel, registry, or approval behavior. `PRD-014` owns generated authority-map package-surface grouping, not approval, task selection, private maintainer inventory, or package-manager behavior. `PRD-015` owns the beginner stuck-trigger recovery path and No-Engineer Fallback Prompt Pack, not repair approval, rollback, setup/update mutation, app-code change approval, external mutation, or support-bot behavior. `PRD-018` owns optional Review Lanes as advisory Security and Release / Docs Freshness review templates, not acceptance approval, release approval, security certification, compliance approval, task creation, or persona behavior. | Feed `FEATURES.md` and candidate journey beads. |
| `tasks/prds-html/*.html` | generated public PRD review | Static HTML review surface generated from non-template PRD shards, including an index, per-PRD review cues, and export-only Acceptance Oracle Matrix proposal controls. | Commit-eligible package artifact for easier PRD review; does not replace Markdown PRD authority, approve PRDs, activate beads, choose tasks, accept implementation, write source Markdown, persist browser edits, or promote exported text automatically. |

## Script Dictionary

Maintained scripts should carry lightweight provenance headers: version, last updated date, `Owner: PrecodeOS`, `Created by Dan Sears / Recode.`, and `SPDX-License-Identifier: Apache-2.0`.

| File | Purpose | Inputs | Outputs or side effects |
|---|---|---|---|
| `scripts/os_parser.py` | Shared markdown/frontmatter parsing helpers. | Markdown files. | Parser utilities for other scripts. |
| `scripts/os_compiler.py` | Stable compiler facade and orchestration surface that compiles Precode state while delegating distinct state, output, and router domains to internal service modules. | Active memory, beads, PRDs, logs, docs, delegation/test/review metadata, Goal Frames, run contracts, authority-map surface classes, stable-fix eligibility inputs, optional command guardrail input. | Stable imports and `logs/*.json`, `logs/run-contract.yaml`, generated progress/handoff/memory/file inventory/authority-map/work-graph surfaces, beginner-facing decisions, stable-fix eligibility, and advisory warnings. |
| `scripts/precode_state.py` | Internal compiler state service for repo-root discovery, bead/todo parsing, path normalization, JSONL loading, and check lookup helpers. | Markdown active memory, bead files, todo state, check-result logs, and parser helpers. | Shared state records and helper functions imported by compiler/check scripts; no standalone public command. |
| `scripts/precode_outputs.py` | Internal compiler output service for JSON/YAML writers, generated report rendering, progress payloads, handoff/help/work-graph/memory-index Markdown, and sidecar writes. | Compiled state payloads passed from `os_compiler.py` or script callers. | Generated report and sidecar writes through existing commands; no standalone public command. |
| `scripts/precode_routing.py` | Internal router service for next-step decisions, load plans, recovery routing, stable-fix routing display, and context-footprint fields. | Active state passed from `os_compiler.py`, active bead, guardrail states, run-contract state, Goal Frame state, stable-fix eligibility state. | Advisory next-step payload fields such as `single_next_protocol`, `load_plan`, `context_footprint`, `stable_fix_eligibility`, and `why_not_more_context`; no standalone public command. |
| `scripts/os-health.py` | Renders OS Health. | Compiled state, including Doctor Dashboard diagnostics, plain-English triage labels, adaptive-depth reasons, guardrails, and generated work graph evidence. | `OS-HEALTH.md`, `logs/os-health.json` with `doctor_dashboard`, `logs/work-graph.json`, and `logs/work-graph.md`. |
| `scripts/precode_doctor.py` | Internal Doctor Dashboard helper for OS Health. | Compiled state payloads passed from `os_compiler.py`. | `doctor_dashboard` generated evidence and beginner triage labels inside `logs/os-health.json` and `OS-HEALTH.md`; no standalone public command. |
| `scripts/precode_cli.py` | Optional local command facade for common PrecodeOS commands. | Current PrecodeOS repo root and curated CLI arguments. | Prints and delegates to existing commands such as `session-start.sh`, `next-step.py`, `os-health.py`, validation checks, and `bootstrap-check.py`; preserves exit codes; no hidden approval, package-manager behavior, release channel, registry, or external mutation. |
| `scripts/progress.py` | Renders the generated user-facing progress snapshot. | Compiled state. | `PROGRESS.md`, `logs/progress.json`. |
| `scripts/next-step.py` | Prints canonical generated next-step routing guidance with a plain user decision and stable-fix eligibility summary. | Compiled state. | Human-readable stdout or advisory JSON including `single_next_protocol`, `load_plan`, `context_footprint`, and `stable_fix_eligibility`; no state mutation. |
| `scripts/loop-health.py` | Prints advisory Build Loop Health for the current work loop. | Compiled state plus the active bead contract and generated work graph warnings. | Compact stdout, verbose dimensions, or advisory JSON; no state mutation, scoring, task selection, or approval. |
| `scripts/ralph-loop.py` | Runs a bounded Ralph attempt for one active bead. | Active bead, optional Ralph frontmatter, one explicit attempt command, validator set, prior Ralph attempts. | `logs/ralph-attempts.jsonl` and `logs/ralph-summary.md` unless `--dry-run`; generated evidence only, not task selection, command approval, acceptance, or transition approval. |
| `scripts/bead-depth-check.py` | Prints adaptive bead-depth advisory findings. | Active bead metadata, risk hints, checks, stop conditions, declared-vs-inferred planning depth, and human-gate signals. | JSON warnings, decision reasons, and shortest next action; no state mutation. |
| `scripts/files-in-play-check.py` | Prints active-bead file mutation guardrail findings and optional command/edit-lock guidance. | Git changed paths, active bead `files_in_play`, optional `--command`, optional `--edit-lock`. | JSON warnings and plain continue/approval/stop guidance; no state mutation or command approval. |
| `scripts/os-integrity-check.py` | Prints PrecodeOS-owned surface integrity findings and strict staged checkpoint warnings for protected source edits. | Changed or staged paths, checkpoint manifests under `logs/os-checkpoints/`, git `HEAD`. | Human-readable or JSON warnings; strict mode exits nonzero when high-risk OS source edits lack a valid checkpoint; no mutation or approval. |
| `scripts/os-checkpoint.py` | Creates, lists, and explicitly restores scoped PrecodeOS source checkpoints. | Clean selected source paths or known scopes such as `validation`, `protocols`, `adapters`, `package-surface`, and `boundary`. | `logs/os-checkpoints/<id>/manifest.json` and copied source files; restore writes only with `--apply` and skips generated or append-only evidence. |
| `scripts/run-contract-check.py` | Prints advisory run-contract findings. | Active bead Run Contract, files in play, verification tiers, recorded checks, and closeout. | JSON warnings about allowed actions, proof needed, approvals, and recovery; no state mutation or command approval. |
| `scripts/accessibility-advisory-check.py` | Prints opt-in Accessibility Advisory Gate findings. | Active bead Closeout Evidence and release/accessibility advisory text after the Accessibility Advisor is invoked. | JSON `not_invoked`, pass, or warning result; no UI-default gate, accessibility compliance claim, review acceptance, release approval, task activation, or external mutation. |
| `scripts/goal-frame-check.py` | Prints advisory Goal Frame findings. | Goal Frame sections in allowed owner files and compiled state. | JSON warnings, reaffirmation requirements, and fit blockers; no state mutation, task selection, or approval. |
| `scripts/clarity-scenario-check.py` | Runs deterministic beginner-decision and recovery scenario fixtures. | In-memory bead scenarios, recovery scenario contracts, Bugfix Spec Lane text-contract checks, stable-fix eligibility scenarios, adaptive-depth scenarios, fallback prompt text-contract checks, and command-risk examples. | Advisory JSON pass/fail result; synthetic recovery fixtures and text-contract checks are regression coverage only, not real recovery evidence, repair approval, rollback approval, setup/update approval, transition approval, support-bot authority, or external-system permission. |
| `scripts/local-hygiene-check.py` | Prints advisory Local Hygiene findings, including protected generated evidence such as `logs/os-checkpoints/*`. | Compiled local hygiene state. | JSON to stdout; no cleanup mutation. |
| `scripts/local-hygiene-dry-run.py` | Previews future archive/delete review candidates without performing them and emits v2 row classifications: `candidate`, `protected`, `unexpected_review`, and `not_candidate`. | Compiled local hygiene state; optional `--self-test`. | `logs/local-hygiene-preview.json`, `logs/local-hygiene-preview.md`, stdout, and self-test JSON; no cleanup mutation. |
| `scripts/bootstrap-check.py` | Prints Bootstrap Confidence findings, optional setup previews, adaptation planning, upgrade preview, recovery guidance, and approval-gated setup/package copy apply modes for a PrecodeOS package source and target project. | `--source`, `--target`, optional `--json`, optional `--preview-manifest`, optional `--supervised-setup-plan`, optional `--existing-project-adaptation-plan`, optional `--upgrade-preview`, optional `--recovery-guidance`, optional `--apply-supervised-setup`, optional `--apply-upgrade-preview`, repeatable `--approve-action`, optional `--write-evidence`. | Plain stdout or JSON by default; preview/adaptation/recovery modes are non-mutating evidence; `--apply-supervised-setup` copies only approved fresh-target `review_copy_candidate` actions; `--apply-upgrade-preview` copies only approved missing package-owned `review_package_copy_candidate` actions and refuses dirty/unknown package states; explicit `--write-evidence` writes `logs/bootstrap-check.json` and `logs/bootstrap-check.md` in the source workspace only. |
| `scripts/existing-repo-intake.py` | Prints read-only Existing Repo Intake findings for a PrecodeOS package source and an existing target repository. | `--source`, `--target`, optional `--json`, optional `--write-evidence`, optional `--self-test`. | Plain stdout or JSON by default; explicit `--write-evidence` writes `logs/existing-repo-intake.json` and `logs/existing-repo-intake.md` in the source workspace only. |
| `scripts/public-repo-check.py` | Checks public repository hygiene against git ignore rules. | `.gitignore` and git-tracked/untracked paths. | Advisory JSON for tracked ignored files and untracked public candidates; no state mutation. |
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
| `scripts/write-guard.sh` | Guards writes against scope rules and runs strict OS-integrity checkpoint checks for protected staged source edits. | Paths, staged changes, active bead context, and OS checkpoint manifests. | Pass/fail write-scope signal; no mutation or command approval. |
| `scripts/install-git-hooks.sh` | Installs local git hooks when available. | Repo checkout. | Local hook files. |
| `scripts/pre-commit-validate.sh` | Runs validation before commit. | Working tree. | Pass/fail hook output. |
| `scripts/scheduled-audit.sh` | Shell wrapper for opt-in scheduled audits. | Local repo and optional external tools. | Audit output files and generated audit report. |
| `scripts/scheduled-audit.py` | Renders scheduled audit report. | Audit command results and compiled state. | `logs/scheduled-audit.md/json`. |
| `scripts/github-audit.py` | Read-only GitHub repository/CI audit. | Git and `gh` when configured. | JSON status output. |
| `scripts/import-github-sources.py` | Read-only GitHub issue/PR intake. | `gh` or sample source. | Generated GitHub source intake evidence. |
| `scripts/import-agent-spend.py` | Imports agent spend telemetry. | Supported usage exports or local sources. | Normalized spend rows or dry-run output. |
| `scripts/log-agent-spend.sh` | Manual spend logging fallback. | Tool/task/tokens/cost. | `logs/agent-spend.jsonl`. |
| `scripts/log-tool-run.sh` | Logs important non-check tool calls. | Tool command metadata. | `logs/tool-runs.jsonl`. |
| `scripts/update-bead-build-journal.py` | Renders generated bead build journal. | Active bead, closeout, checks, tool runs, loop events, and Git metadata. | `logs/bead-build-journal.md/jsonl`. |
| `scripts/update-learning-diary.py` | Renders generated learning diary. | Bead closeout, checks, spend, loop events. | `logs/learning-diary.md/jsonl`. |
| `scripts/update-memory-index.py` | Renders reviewed memory index. | `memory/cards/*.md`. | `logs/memory-index.md/json`. |
| `scripts/memory-check.py` | Searches or audits reviewed memory cards. | `memory/cards/*.md`, optional query/category/freshness/status/promotion filters. | Advisory JSON only; no card creation, owner-file promotion, task selection, or state mutation. |
| `scripts/prd-html.py` | Generates or checks the committed PRD HTML review surface, including export-only Acceptance Oracle Matrix proposal controls. | Non-template Markdown PRD shards in `tasks/prds/*.md`; optional `--check`; optional `--output`. | `tasks/prds-html/*.html`; generated review convenience only, not PRD authority, approval, bead activation, task selection, implementation acceptance, Markdown write-back, browser persistence, or automatic promotion. |
| `scripts/file-inventory.py` | Renders/checks file inventory metadata. | Repo files and authority contracts. | `logs/file-inventory.json` or advisory JSON. |
| `scripts/*-check.py` | Advisory quality checks. | Compiled state and logs. | JSON warnings; no state mutation. |
| `scripts/version-check.py` | Checks version metadata coverage. | Docs, scripts, workflows. | Advisory JSON. |

## Adapter, Mode, Memory, And Workflow Dictionary

| File or family | Class | What it owns | How it relates |
|---|---|---|---|
| `adapters/ADAPTER-INDEX.md` | reference | Shared adapter command surface, narrow compatibility shim matrix, routing-protocol pointer, and tool-neutral expectations. | Source of truth for shipped, advisory, and deferred adapter/shim status plus shared routing discipline. |
| `adapters/*.md` | reference | Tool-specific notes for Codex, Claude, GitHub Copilot, Cursor, Gemini, Antigravity, and related agents. | Thin wrappers around `AGENT.md` that translate shared routing tiers into provider-native controls when available. |
| `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md` | reference shims | Auto-discovery compatibility for specific tools. | Must point back to `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`. |
| `.github/PULL_REQUEST_TEMPLATE.md` | reference | Pull request evidence template for package-facing changes. | Prompts the maintainer to record changed surfaces, checks, risk, and release-candidate relevance; it does not approve work. |
| `modes/NAVIGATOR.md` | reference | Planning/navigation role guidance. | Used when choosing work or shaping tasks. |
| `modes/EXPLORER.md` | reference | Explorer role contract for bounded read-only repo inspection and source summarization. | Used when a narrow question needs cited repo facts before navigator, builder, or review decisions. |
| `modes/BUILDER.md` | reference | Implementation role guidance. | Used during scoped code or doc changes. |
| `modes/REVIEW.md` | reference | Review role guidance. | Used for code review, closeout, and acceptance checks. |
| `memory/REVIEWED-MEMORY-GUIDE.md` | reference | Reviewed memory directory guidance and search orientation. | Points to memory protocol, card directory, generated index refresh, and read-only memory search. |
| `memory/cards/MEMORY-CARD-FORMAT.md` | reference | Memory card format, required fields, search topics, and promotion-owner expectations. | Defines reviewed memory card expectations and evidence-only search boundaries. |
| `memory/cards/MEMORY-CARD-template.md` | reference template | Starter shape for reviewed memory cards. | Copied for approved memory cards; includes promotion-review reminders. |
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
| `logs/bead-build-journal.md/jsonl` | generated report | Bead-level build-change journal and evidence-backed implementation snapshot. | Not active memory, task authority, acceptance, or transition approval. |
| `logs/ralph-attempts.jsonl` and `logs/ralph-summary.md` | generated evidence/report | Bounded Ralph attempt history, validator outcomes, failure category, retry allowance, and next recommended move. | Evidence only; not active memory, task selection, command approval, review acceptance, or transition approval. |
| `logs/os-events.jsonl` | generated evidence | Compiled event stream. | Generated from logs. |
| `logs/os-health.json` | generated sidecar | Machine-readable OS Health payload, including `doctor_dashboard` diagnostic rows and plain-English triage fields. | Evidence only; Doctor Dashboard does not select tasks, approve transitions, approve commands, or replace `scripts/next-step.py`. |
| `logs/next-step.json` | generated sidecar | Machine-readable next-step guidance, load plan, single next protocol, and context footprint. | Evidence only; not task selection, transition approval, command approval, or active memory. |
| `logs/work-graph.json` and `logs/work-graph.md` | generated report/sidecar | Evidence-only bead, PRD, owner-file, check, blocker, follow-up, and transition relationship graph. | Evidence only; not task selection, review acceptance, transition approval, active memory, or a second tracker. |
| `logs/run-contract.json` and `logs/run-contract.yaml` | generated sidecar | Active bead run-contract execution profile. | Evidence only; not authority, command approval, or host-specific ZYAL contract. |
| `logs/authority-map.json` | generated sidecar | Authority contract index. | Evidence only. |
| `logs/adapter-index.json` | generated sidecar | Adapter command-surface summary. | Evidence only. |
| `logs/shim-index.json` | generated sidecar | Shim summary. | Evidence only. |
| `logs/readiness.json` | generated sidecar | Bead readiness and promotion state. | Evidence only. |
| `logs/orchestration-map.json` | generated sidecar | Intent orchestration summary. | Evidence only. |
| `logs/workflow-map.json` | generated sidecar | Workflow selection summary. | Evidence only. |
| `logs/goal-frame.json` | generated sidecar | Goal Frame status, freshness, required-field, fit-blocker, and boundary warnings. | Advisory orientation only; not task selection, PRD approval, or bead activation. |
| `logs/long-horizon-map.json` | generated sidecar | Future/blocked/deferred work summary. | Evidence only. |
| `logs/handoff-packet.md/json` | generated report | Handoff context pack. | Orientation only; not transition approval. |
| `logs/learning-diary.md/jsonl` | generated report | Session learning digest and entries. | Not active memory. |
| `logs/memory-index.md/json` | generated report | Reviewed memory card index with grouped search, citation, freshness, and promotion-warning fields. | Search aid only; not active memory, task selection, owner-file authority, or promotion approval. |
| `logs/file-inventory.json` | generated sidecar | Generated inventory metadata. | Maintenance aid only. |
| `logs/bootstrap-check.json` and `logs/bootstrap-check.md` | generated sidecar/report | Optional Bootstrap Confidence, manifest-preview, supervised setup-plan, adaptation-plan, upgrade-preview, and recovery-guidance evidence written only when `scripts/bootstrap-check.py --write-evidence` is used. | Evidence only; not setup approval, install permission, update permission, owner-file adaptation approval, dirty-file overwrite approval, release-channel metadata, package-manager behavior, rollback automation, target-project authority, or active memory. |
| `logs/existing-repo-intake.json` and `logs/existing-repo-intake.md` | generated sidecar/report | Optional Existing Repo Intake evidence written only when `scripts/existing-repo-intake.py --write-evidence` is used. | Evidence only; not owner-file adaptation, check execution, setup approval, PRD approval, bead activation, target-project authority, or active memory. |
| `logs/pattern-guidance.json` | generated sidecar | System design pattern guidance. | Advisory only. |
| `logs/scheduled-audit.md/json` | generated report | Scheduled audit summary. | Evidence only. |
| `logs/scheduled-audit-output/*` | generated evidence family | Timestamped audit helper outputs. | Document as a family, not individual files. |

## Maintenance Rules

- Add new PrecodeOS-owned files here when they become durable surfaces.
- Add generated outputs by family when they are timestamped or high-churn.
- Keep `logs/file-inventory.json` regenerated with `python3 scripts/file-inventory.py`.
- Run `python3 scripts/file-inventory.py --check` before accepting inventory-sensitive changes.
- Keep `CODEBASE-GUIDE.md` focused on target-project code layout.
