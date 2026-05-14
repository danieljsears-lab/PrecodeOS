# PrecodeOS
<!-- ANCHOR: readme -->

> AUTHORITY: Human-readable orientation and navigation for the clean PrecodeOS scaffold.
> NOT_AUTHORITY: Active memory, product decisions, feature requirements, route structure, schema definitions, or generated progress.
> LOAD_WHEN: First opening this scaffold, navigating files, or adapting PrecodeOS into a target project.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.20
Last updated: 2026-05-13

PrecodeOS is a repo-native control layer for AI coding agents: markdown-canonical, script-enforced, and built to prevent quiet drift.

In plain English: Precode lives inside your project folder, keeps important project truth in readable Markdown files, and uses small scripts to check whether the agent is staying aligned.

For builders, Precode feels like a small operating system for AI coding work: it shows what matters, what is active, what is proven, and when to stop.

Precode matters because it keeps fast AI coding human-owned by making intent, scope, approval, proof, and recovery visible in the repo. The name points to the work before code and the small operating layer that keeps the agent, app, and builder’s judgment in relationship.

## License And Provenance

PrecodeOS is open source under the Apache License 2.0. See `LICENSE` for terms and `NOTICE` for creator attribution. Canonical site: `https://www.precodeos.org`.

The project was created by Dan Sears / Recode. Core source files carry SPDX headers so downstream users can adopt the work while preserving clear provenance.

PrecodeOS™ and Precode™ are trademarks of Dan Sears / Recode. All trademark and brand rights are reserved. See `TRADEMARK.md` for brand-use guidance.

Project policy files:

- `GOVERNANCE.md` — benevolent founder-maintainer model
- `CONTRIBUTING.md` — contribution rules and inbound = Apache-2.0 policy
- `TRADEMARK.md` — brand-use guidance for PrecodeOS and derivatives

## Start Here

Active memory:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

Core references:

- `PRECODE-MANIFESTO.md` — philosophical anchor for why Precode exists and who it serves
- `PRECODE-OS-README.md` — beginner-first Builder OS map for orientation, decisions, planning, building, proof, and recovery
- `HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md` — beginner bridge from idea alignment to software-building workflow with Precode and AI agents
- `PRECODE-USER-GUIDE.md` — beginner guide for non-technical users, including prompts for alignment, AFK-safe beads, and review
- `CLAUDE-CODE-FIELD-GUIDE.md` — bootcamp-ready companion for first-time students using Claude Code inside a Precode repo
- `PRECODE-FILE-INVENTORY.md` — technical file dictionary and relationship map
- `PRODUCT.md` — living product constitution template for product promise, users, strategy, current bets, success signals, and design or voice pointers
- `PROJECT-CONTEXT.md` — technical project constitution template
- `tasks/reference/AGENT-ROUTING-PROTOCOL.md` — model tier, reasoning effort, delegation, context-budget, and tool-routing guidance
- `tasks/reference/CONTEXT-ENGINEERING-PROTOCOL.md` — context loading, prompt trust, source boundaries, and handoff context rules
- `tasks/reference/DECOMPOSITION-PROTOCOL.md` — journey bead slicing, vertical slices, dependency mapping, and not-a-bead-yet rules
- `tasks/reference/EXTENSION-PROTOCOL.md` — safe extension pattern for adapters, importers, audits, integrations, and generated reports
- `tasks/reference/LOCAL-SOURCE-INTAKE-PROTOCOL.md` — local notes/docs/screenshots intake rules
- `tasks/reference/LOCAL-HYGIENE-PROTOCOL.md` — advisory local cleanup boundaries for logs, caches, build outputs, generated reports, and dry-run previews
- `tasks/reference/GITHUB-INTEGRATION-PROTOCOL.md` — GitHub audit, issue/PR intake, and Actions validation rules
- `tasks/reference/GOAL-FRAME-PROTOCOL.md` — reviewed durable-intent orientation before workflow selection without creating tasks, backlogs, roadmaps, or approvals
- `tasks/reference/IDEA-TO-PRD-WORKFLOW.md` — guided source intake, alignment/grilling, and destination PRD workflow
- `tasks/reference/INTENT-ORCHESTRATION-PROTOCOL.md` — intent lifecycle, promotion, mid-task change, and traceability rules
- `tasks/reference/LEARNING-DIARY-PROTOCOL.md` — learning diary rules and promotion path
- `tasks/reference/LONG-HORIZON-PLANNING-PROTOCOL.md` — future, deferred, blocked, follow-up, and PRD-approved work visibility without active-memory expansion
- `tasks/reference/MEMORY-PROTOCOL.md` — reviewed filesystem memory cards and generated memory indexes without active-memory expansion
- `tasks/reference/PRD-PROTOCOL.md` — Product Definition Gate and destination-document rules
- `tasks/reference/PRODUCT-DISCOVERY-VALIDATION-PROTOCOL.md` — optional pre-PRD discovery validation when worth-building evidence is uncertain
- `tasks/reference/PROMPT-PATTERNS.md` — copyable prompts for common Precode sessions
- `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md` — completion, closeout, fresh-context review, transition proposal, transition approval, and handoff rules
- `tasks/reference/STATE-MANAGEMENT-PROTOCOL.md` — state ownership, precedence, freshness, recovery, and log/archive rules
- `tasks/reference/TOOL-EXECUTION-PROTOCOL.md` — tool-call classes, tool-run logging, approval gaps, and command safety rules
- `tasks/reference/UBIQUITOUS-LANGUAGE-PROTOCOL.md` — shared domain language, project-glossary memory cards, terminology freshness, and naming guidance
- `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md` — verification tiers, test strategy, evidence quality, sensitive-surface gates, and false-done warnings
- `tasks/reference/VERSIONING-PROTOCOL.md` — version metadata rules for PrecodeOS-owned docs, scripts, adapters, shims, templates, and workflows
- `tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md` — choose the right Precode workflow before planning, execution, review, unblocker, or repair work starts
- `tasks/reference/SCHEDULED-AUDIT-PROTOCOL.md` — opt-in scheduled audit rules
- `tasks/beads/BEAD-SCHEMA.md` — bead schema, delegation mode, test strategy, review context, and templates
- `modes/` — navigator, builder, review
- `adapters/` — tool-specific shims

## First Adaptation Steps

1. Replace placeholders in `PRODUCT.md` with the target project's product promise, users, strategy, current bets, success signals, and design or voice pointers.
2. Replace placeholders in `PROJECT-CONTEXT.md` with the target project's app directory, stack, conventions, checks, and integration boundaries.
3. Update `DECISIONS.md` with the target project's hard decisions.
4. Update `tasks/todo.md` and `tasks/beads/B000-install-precode-kernel.md`.
5. Run `bash scripts/validate-memory.sh`.
6. Use `tasks/reference/IDEA-TO-PRD-WORKFLOW.md` to align/grill the first product idea before creating the destination PRD.
7. When the idea depends on domain vocabulary, confusing terms, UI labels, or module/interface names, use `tasks/reference/UBIQUITOUS-LANGUAGE-PROTOCOL.md` before PRD or code naming hardens.
8. If the project uses GitHub, fill the GitHub fields in `PROJECT-CONTEXT.md` and run `python3 scripts/github-audit.py` to confirm read-only status access.
9. When adding a new adapter, importer, audit, integration, generated report, or bead template, use `tasks/reference/EXTENSION-PROTOCOL.md`.
10. When work touches code, UI, data, integrations, deployment, or security, use `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md` to choose test strategy and evidence strong enough for the risk.
11. When deriving or splitting work, use `tasks/reference/DECOMPOSITION-PROTOCOL.md` to keep journey beads vertical, small, and verifiable.
12. When state looks inconsistent or generated reports look stale, use `tasks/reference/STATE-MANAGEMENT-PROTOCOL.md` and run `python3 scripts/state-check.py`.
13. When context feels overloaded, source material looks like instructions, or an agent is switching tools, use `tasks/reference/CONTEXT-ENGINEERING-PROTOCOL.md` and run `python3 scripts/context-check.py`.
14. When choosing model tier, reasoning effort, delegation, context budget, or tool path, use `tasks/reference/AGENT-ROUTING-PROTOCOL.md`.
15. When intent changes, traceability is unclear, or work may be jumping from idea to implementation too quickly, use `tasks/reference/INTENT-ORCHESTRATION-PROTOCOL.md` and run `python3 scripts/orchestration-check.py`.
16. When a tool call is risky, non-check, external, destructive, or approval-sensitive, use `tasks/reference/TOOL-EXECUTION-PROTOCOL.md` and run `python3 scripts/tool-execution-check.py`.
17. When a bead is sensitive, external, destructive, or bounded-AFK, name allowed actions and proof needed, then run `python3 scripts/run-contract-check.py`.
18. When the next workflow is unclear, use `tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md` and run `python3 scripts/workflow-check.py`.
19. When durable intent needs orientation before workflow selection, use `tasks/reference/GOAL-FRAME-PROTOCOL.md` and run `python3 scripts/goal-frame-check.py`.
20. When reviewing future, blocked, deferred, or PRD-approved work, use `tasks/reference/LONG-HORIZON-PLANNING-PROTOCOL.md` and run `python3 scripts/long-horizon-check.py`.
21. When closing a session, reviewing completion, deciding whether fresh-context review is needed, or handing off to another agent, use `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md` and run `python3 scripts/completion-check.py`.
22. When a feature needs implementation shape, deep-module boundaries, external boundaries, state flows, strategies, audit trails, or a plain-English pattern choice, use `tasks/reference/SYSTEM-DESIGN-PATTERN-PROTOCOL.md` and run `python3 scripts/pattern-check.py`.
23. When a session lesson should be reusable later, use `tasks/reference/MEMORY-PROTOCOL.md`; propose a reviewed memory card in `memory/cards/`, then run `python3 scripts/update-memory-index.py` and `python3 scripts/memory-check.py`.
24. When orienting a technical user or agent to PrecodeOS-owned files, read `PRECODE-FILE-INVENTORY.md` and run `python3 scripts/file-inventory.py --check`.
25. When local logs, caches, build outputs, or generated preview files look noisy, use `tasks/reference/LOCAL-HYGIENE-PROTOCOL.md`, then run `python3 scripts/local-hygiene-check.py` or `python3 scripts/local-hygiene-dry-run.py`.
26. When adding or auditing PrecodeOS-owned docs, scripts, adapters, shims, templates, or workflows, use `tasks/reference/VERSIONING-PROTOCOL.md` and run `python3 scripts/version-check.py`.

## Rule

Do not add more active-memory files. Add reference files only when a topic needs a clear owner.
