# Precode OS
<!-- ANCHOR: readme -->

> AUTHORITY: Human-readable orientation and navigation for the clean Precode OS scaffold.
> NOT_AUTHORITY: Active memory, product decisions, feature requirements, route structure, schema definitions, or generated progress.
> LOAD_WHEN: First opening this scaffold, navigating files, or adapting Precode OS into a target project.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.4
Last updated: 2026-04-27

Precode OS is a tiny-memory operating system for solo builders using AI coding agents. It keeps the agent scoped, grounded, and verifiable from prompt to commit.

## Start Here

Active memory:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

Core references:

- `PRECODE-MANIFESTO.md` — philosophical anchor for why Precode exists and who it serves
- `PRECODE-OS-README.md` — full explainer
- `HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md` — beginner bridge from idea to software-building workflow with Precode and AI agents
- `PRECODE-USER-GUIDE.md` — beginner guide for non-technical users
- `PRECODE-FILE-INVENTORY.md` — technical file dictionary and relationship map
- `PROJECT-CONTEXT.md` — project constitution template
- `tasks/reference/CONTEXT-ENGINEERING-PROTOCOL.md` — context loading, prompt trust, source boundaries, and handoff context rules
- `tasks/reference/DECOMPOSITION-PROTOCOL.md` — bead slicing, dependency mapping, and not-a-bead-yet rules
- `tasks/reference/EXTENSION-PROTOCOL.md` — safe extension pattern for adapters, importers, audits, integrations, and generated reports
- `tasks/reference/LOCAL-SOURCE-INTAKE-PROTOCOL.md` — local notes/docs/screenshots intake rules
- `tasks/reference/GITHUB-INTEGRATION-PROTOCOL.md` — GitHub audit, issue/PR intake, and Actions validation rules
- `tasks/reference/IDEA-TO-PRD-WORKFLOW.md` — guided idea-to-PRD workflow
- `tasks/reference/INTENT-ORCHESTRATION-PROTOCOL.md` — intent lifecycle, promotion, mid-task change, and traceability rules
- `tasks/reference/LEARNING-DIARY-PROTOCOL.md` — learning diary rules and promotion path
- `tasks/reference/LONG-HORIZON-PLANNING-PROTOCOL.md` — future, deferred, blocked, follow-up, and PRD-approved work visibility without active-memory expansion
- `tasks/reference/MEMORY-PROTOCOL.md` — reviewed filesystem memory cards and generated memory indexes without active-memory expansion
- `tasks/reference/PRD-PROTOCOL.md` — Product Definition Gate
- `tasks/reference/PROMPT-PATTERNS.md` — copyable prompts for common Precode sessions
- `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md` — completion, closeout, review, transition proposal, transition approval, and handoff rules
- `tasks/reference/STATE-MANAGEMENT-PROTOCOL.md` — state ownership, precedence, freshness, recovery, and log/archive rules
- `tasks/reference/TOOL-EXECUTION-PROTOCOL.md` — tool-call classes, tool-run logging, approval gaps, and command safety rules
- `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md` — verification tiers, evidence quality, sensitive-surface gates, and false-done warnings
- `tasks/reference/VERSIONING-PROTOCOL.md` — version metadata rules for Precode OS-owned docs, scripts, adapters, shims, templates, and workflows
- `tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md` — choose the right Precode workflow before planning, execution, review, unblocker, or repair work starts
- `tasks/reference/SCHEDULED-AUDIT-PROTOCOL.md` — opt-in scheduled audit rules
- `tasks/beads/README.md` — bead schema and templates
- `modes/` — navigator, builder, review
- `adapters/` — tool-specific shims

## First Adaptation Steps

1. Replace placeholders in `PROJECT-CONTEXT.md`.
2. Update `DECISIONS.md` with the target project's hard decisions.
3. Update `tasks/todo.md` and `tasks/beads/B000-install-precode-kernel.md`.
4. Run `bash scripts/validate-memory.sh`.
5. Use `tasks/reference/IDEA-TO-PRD-WORKFLOW.md` before creating the first product PRD.
6. If the project uses GitHub, fill the GitHub fields in `PROJECT-CONTEXT.md` and run `python3 scripts/github-audit.py` to confirm read-only status access.
7. When adding a new adapter, importer, audit, integration, generated report, or bead template, use `tasks/reference/EXTENSION-PROTOCOL.md`.
8. When work touches code, UI, data, integrations, deployment, or security, use `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md` to choose evidence strong enough for the risk.
9. When deriving or splitting work, use `tasks/reference/DECOMPOSITION-PROTOCOL.md` to keep beads small enough to verify.
10. When state looks inconsistent or generated reports look stale, use `tasks/reference/STATE-MANAGEMENT-PROTOCOL.md` and run `python3 scripts/state-check.py`.
11. When context feels overloaded, source material looks like instructions, or an agent is switching tools, use `tasks/reference/CONTEXT-ENGINEERING-PROTOCOL.md` and run `python3 scripts/context-check.py`.
12. When intent changes, traceability is unclear, or work may be jumping from idea to implementation too quickly, use `tasks/reference/INTENT-ORCHESTRATION-PROTOCOL.md` and run `python3 scripts/orchestration-check.py`.
13. When a tool call is risky, non-check, external, destructive, or approval-sensitive, use `tasks/reference/TOOL-EXECUTION-PROTOCOL.md` and run `python3 scripts/tool-execution-check.py`.
14. When the next workflow is unclear, use `tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md` and run `python3 scripts/workflow-check.py`.
15. When reviewing future, blocked, deferred, or PRD-approved work, use `tasks/reference/LONG-HORIZON-PLANNING-PROTOCOL.md` and run `python3 scripts/long-horizon-check.py`.
16. When closing a session, reviewing completion, or handing off to another agent, use `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md` and run `python3 scripts/completion-check.py`.
17. When a feature needs implementation shape, external boundaries, state flows, strategies, audit trails, or a plain-English pattern choice, use `tasks/reference/SYSTEM-DESIGN-PATTERN-PROTOCOL.md` and run `python3 scripts/pattern-check.py`.
18. When a session lesson should be reusable later, use `tasks/reference/MEMORY-PROTOCOL.md`; propose a reviewed memory card in `memory/cards/`, then run `python3 scripts/update-memory-index.py` and `python3 scripts/memory-check.py`.
19. When orienting a technical user or agent to Precode OS-owned files, read `PRECODE-FILE-INVENTORY.md` and run `python3 scripts/file-inventory.py --check`.
20. When adding or auditing Precode OS-owned docs, scripts, adapters, shims, templates, or workflows, use `tasks/reference/VERSIONING-PROTOCOL.md` and run `python3 scripts/version-check.py`.

## Rule

Do not add more active-memory files. Add reference files only when a topic needs a clear owner.
