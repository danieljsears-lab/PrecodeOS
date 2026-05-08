# Precode OS Maintainer Roadmap
<!-- ANCHOR: precode-maintainer-roadmap -->

> AUTHORITY: Maintainer-owned roadmap for improving Precode OS.
> NOT_AUTHORITY: Active memory, user workflow authority, task selection, PRD approval, bead activation, generated progress, or implementation status.
> LOAD_WHEN: The maintainer is prioritizing Precode improvements, comparing roadmap candidates, or deciding what should become a PRD or bead.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-05-08

## Purpose

This roadmap is Dan Sears / Recode maintainer planning material for improving Precode OS itself.

It records committed direction, not committed dates. A roadmap item becomes real work only after it is promoted through the normal Precode improvement path: maintainer decision, PRD or authority update when needed, candidate bead, approval, implementation, recorded checks, and review.

This file is not active memory. It must not guide normal user project work, select tasks, approve transitions, or replace `AGENT.md`, `DECISIONS.md`, `tasks/todo.md`, PRDs, beads, or generated evidence.

## Scoring Rubric

Score each candidate from 1 to 5 on every dimension. Calculate the weighted total as:

```text
(Mission Fit * 0.30)
+ (Drift Reduction * 0.25)
+ (Beginner Value * 0.20)
+ (Leverage * 0.15)
+ (Implementation Cost * 0.10)
```

For `Implementation Cost`, a higher score means lower cost and lower complexity.

| Dimension | Weight | Question |
|---|---:|---|
| Mission Fit | 30% | Does this help non-technical builders stay oriented, bounded, proven, and recoverable? |
| Drift Reduction | 25% | Does this prevent or recover from scope, context, evidence, state, or authority drift? |
| Beginner Value | 20% | Does this make Precode easier or safer for a new builder? |
| Leverage | 15% | Does this improve many workflows rather than one narrow edge case? |
| Implementation Cost | 10% | Can this be added without bloating active memory or creating fragile complexity? |

Priority bands:

| Priority | Meaning |
|---|---|
| P0 | Next roadmap core. |
| P1 | Strengthen the main operating loop. |
| P2 | Improve judgment and quality. |
| P3 | Expand carefully after the kernel is quieter and more trusted. |

Size labels:

| Size | Meaning |
|---|---|
| S | Small, focused change. |
| M | Medium, touches several docs/scripts or one meaningful workflow. |
| L | Large, crosses multiple workflows or needs staged rollout. |

## Ranked Candidates

| Rank | Candidate | Mission Fit | Drift Reduction | Beginner Value | Leverage | Cost | Total | Size | Priority |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Product Discovery Validation | 5.0 | 4.5 | 5.0 | 4.5 | 4.0 | 4.75 | M | P0 |
| 2 | Beginner Recovery Flows | 5.0 | 5.0 | 5.0 | 4.0 | 3.5 | 4.65 | M | P0 |
| 3 | Installer / Bootstrap Experience | 5.0 | 4.0 | 5.0 | 4.5 | 3.5 | 4.55 | L | P0 |
| 4 | Goal Frame Hardening | 4.5 | 4.5 | 4.5 | 4.0 | 4.0 | 4.40 | S/M | P1 |
| 5 | Existing Repo Intake | 4.5 | 4.5 | 4.5 | 4.5 | 3.0 | 4.35 | L | P1 |
| 6 | Release Readiness / Shipping Lane | 4.5 | 4.0 | 4.0 | 4.5 | 3.5 | 4.20 | M/L | P1 |
| 7 | Memory Search And Promotion | 4.0 | 4.5 | 4.0 | 4.0 | 3.5 | 4.05 | M | P1 |
| 8 | What Next Clarity / `next-step.py` Hardening | 4.5 | 4.0 | 4.5 | 4.0 | 3.0 | 4.00 | S/M | P1 |
| 9 | File Mutation And Command Guardrails | 4.0 | 4.5 | 4.0 | 4.0 | 3.0 | 3.95 | M | P1 |
| 10 | Adaptive Planning Depth | 4.0 | 4.0 | 4.0 | 4.0 | 3.0 | 3.85 | M | P2 |
| 11 | System Design Guidance Defaults | 4.0 | 3.5 | 4.5 | 4.0 | 3.0 | 3.80 | M | P2 |
| 12 | Local Hygiene v2 | 3.5 | 4.0 | 4.0 | 3.5 | 3.0 | 3.65 | M | P2 |
| 13 | Review Lanes | 3.5 | 4.0 | 3.5 | 4.0 | 2.5 | 3.55 | L | P2 |
| 14 | Verification And Release Evidence | 3.5 | 4.0 | 3.5 | 4.0 | 2.0 | 3.50 | L | P2 |
| 15 | External Status Integrations | 3.5 | 3.5 | 3.0 | 4.0 | 2.0 | 3.35 | L | P3 |
| 16 | Optional Precode Packs | 3.5 | 3.0 | 3.0 | 4.0 | 2.5 | 3.20 | L | P3 |
| 17 | Tool Execution Ledger v2 | 3.0 | 3.5 | 3.0 | 3.5 | 2.5 | 3.10 | M | P3 |
| 18 | File Inventory / Versioning Enforcement | 3.0 | 3.0 | 2.5 | 3.5 | 3.0 | 2.95 | S/M | P3 |
| 19 | AFK / Delegation Safety Improvements | 3.0 | 3.0 | 3.0 | 3.5 | 2.5 | 2.90 | M | P3 |
| 20 | Ubiquitous Language / Glossary Hardening | 3.0 | 3.0 | 3.0 | 2.5 | 3.0 | 2.80 | S/M | P3 |
| 21 | Handoff Packet Improvements | 3.0 | 3.0 | 2.5 | 2.5 | 3.0 | 2.75 | S | P3 |

## P0: Next Roadmap Core

### Product Discovery Validation

Problem: Precode helps shape ideas, but it does not yet fully help builders validate whether an idea is worth building.

Why it matters: non-technical builders can code a polished wrong thing quickly. Product discovery is the upstream steering layer that asks whether the problem, user, alternative, demand signal, and smallest learning step are real enough to justify implementation.

Direction: add a lightweight Product Discovery Protocol, stronger workbook prompts, evidence-strength language, interview guidance, alternatives and workaround analysis, competitive/category framing, pricing or demand signals, experiment design, and proceed/pause/narrow/kill decisions.

First implementation shape: reference protocol plus workbook/user-guide updates. Keep it prescriptive and beginner-safe, not a full product-management framework.

Guardrails: do not make discovery a mandatory ceremony for tiny tasks. Do not let generated discovery summaries approve PRDs, create beads, or choose work.

Promotion path: create a Product Discovery PRD or protocol bead, then update the workbook and guides after review.

### Beginner Recovery Flows

Problem: builders will move files, rename files, edit generated reports, approve too quickly, lose context, or get a confused agent.

Why it matters: Precode's anti-drift promise is incomplete unless recovery is as visible as prevention. A beginner needs a clear "I think I broke something" path that restores confidence without requiring software-engineering instincts.

Direction: add recovery flows for file moves, renames, bad direct edits, stale generated reports, broken active state, missing checks, confused sessions, and accidental scope expansion.

First implementation shape: recovery protocol, user-guide section, `next-step.py` recovery recommendation improvements, and advisory checker prompts.

Guardrails: recovery guidance must not run destructive commands automatically, overwrite user edits, or treat generated reports as repair authority.

Promotion path: create a recovery workflow PRD or bead scoped to documentation first, then add script support only where the workflow proves stable.

### Installer / Bootstrap Experience

Problem: if setup is confusing, Precode's operating model never reaches the builder.

Why it matters: the people Precode serves may not know how to copy a file tree, install hooks, run scripts, or decide which docs apply to their app. Adoption needs a guided first-run path.

Direction: add a beginner-safe bootstrap experience for new repos and existing repos, with setup checks, missing-dependency guidance, active-memory verification, and first-session orientation.

First implementation shape: bootstrap protocol and script or command wrapper that inspects without mutating by default, then offers explicit setup steps.

Guardrails: do not hide repository changes, install hooks silently, overwrite project docs, or create active memory without explanation.

Promotion path: start with a bootstrap planning PRD, then implement a dry-run bootstrap helper before any mutating setup flow.

## P1: Strengthen The Main Operating Loop

### Goal Frame Hardening

Problem: Goal Frames are useful durable orientation, but stale or task-like Goal Frames could become hidden authority.

Why it matters: builders need persistent direction without turning goals into a backlog, roadmap, or silent task selector.

Direction: improve detection, reaffirmation prompts, stale-frame warnings, candidate handling from the Product Ideation Workbook, and `next-step.py` advisory display.

First implementation shape: strengthen `goal-frame-check.py`, compiled state output, and beginner prompts.

Guardrails: Goal Frames must not approve PRDs, activate beads, choose tasks, or bypass reaffirmation.

Promotion path: create a Goal Frame hardening bead tied to `GOAL-FRAME-PROTOCOL.md`.

### Existing Repo Intake

Problem: many builders will bring an existing app, not start from a clean Precode scaffold.

Why it matters: an agent can damage an unfamiliar repo when it lacks a safe map of stack, structure, risks, docs gaps, and first safe work.

Direction: add an existing-repo intake workflow that summarizes stack, app shape, owner-file gaps, sensitive surfaces, generated evidence, and likely first PRD or bead without editing app code.

First implementation shape: protocol plus advisory script that reads files and writes generated intake evidence.

Guardrails: do not infer authority from generated scans. Do not rewrite project docs or install Precode automatically.

Promotion path: create an Existing Repo Intake PRD and a read-only helper bead.

### Release Readiness / Shipping Lane

Problem: Precode is strong before and during implementation, but shipping needs clearer gates.

Why it matters: deployment, rollback, smoke tests, browser checks, canary evidence, and docs freshness are where "works locally" becomes "safe enough to ship."

Direction: add release bead templates, deployment readiness prompts, smoke-test evidence, browser verification, canary checks, rollback notes, and post-release review.

First implementation shape: release readiness protocol and bead closeout guidance.

Guardrails: do not deploy, promote, roll back, or change dashboards from generated guidance or scheduled audits.

Promotion path: create a release-lane PRD and start with docs/templates before provider-specific automation.

### Memory Search And Promotion

Problem: reviewed memory exists, but it should become easier to search, cite, export, and promote safely.

Why it matters: memory helps future sessions only if it is findable, trustworthy, and clearly subordinate to owner files.

Direction: improve memory index search, citation prompts, card freshness, promotion warnings, and export-friendly structure.

First implementation shape: update memory protocol and `update-memory-index.py` before adding richer tooling.

Guardrails: memory must not become active memory, hidden instructions, task selection, or a replacement for `DECISIONS.md`.

Promotion path: create a memory-search bead scoped to generated indexes and docs.

### What Next Clarity / `next-step.py` Hardening

Problem: beginners often need one clear next human decision more than another report.

Why it matters: Precode's generated help should translate repo state into a small set of actions: continue, ask, prove, review, approve transition, repair, or stop.

Direction: improve state-specific decisions, first-line clarity, warning noise, Goal Frame handling, recovery prompts, and plain-English output.

First implementation shape: targeted `next-step.py` and `PRECODE-HELP.md` output refinements with deterministic fixtures.

Guardrails: generated next-step help must not choose tasks, approve transitions, or become active memory.

Promotion path: create a next-step hardening bead and record fixture coverage.

### File Mutation And Command Guardrails

Problem: agents can touch the wrong files or run risky commands before the builder understands the impact.

Why it matters: file-scope and command-risk guardrails are practical brakes for quiet drift and unsafe momentum.

Direction: tune sensitive-surface patterns, destructive-command detection, approval-needed prompts, edit-lock language, and split/revert/approve guidance.

First implementation shape: improve `files-in-play-check.py`, command-risk examples, and user-facing prompts.

Guardrails: do not silently block normal work or auto-approve commands.

Promotion path: create a guardrail hardening bead tied to the Tool Execution and Verification protocols.

## P2: Improve Judgment And Quality

### Adaptive Planning Depth

Problem: not every task needs the same planning depth, but builders need help knowing when a task is tiny, normal, risky, or too broad.

Why it matters: too little planning creates drift; too much planning creates process burden.

Direction: add clearer examples, better warnings, migration guidance, and depth recommendations tied to concrete decisions.

First implementation shape: improve bead-depth docs, examples, and checker output.

Guardrails: do not make every bead carry PRD ceremony or break old beads.

Promotion path: create an adaptive-depth documentation and checker bead.

### System Design Guidance Defaults

Problem: non-technical builders often cannot tell whether a feature needs direct implementation, an adapter, a state flow, a strategy boundary, or an audit trail.

Why it matters: code shape affects future change, safety, and maintainability before the builder can recognize the pattern.

Direction: make pattern guidance more example-driven, prescriptive, and tied to common beginner situations.

First implementation shape: enrich the System Design Pattern Protocol, guide prompts, and `pattern-check.py`.

Guardrails: do not require named patterns for simple one-off changes.

Promotion path: create a system-design examples bead.

### Local Hygiene v2

Problem: local clutter, bulky logs, caches, and generated outputs can confuse builders and agents.

Why it matters: cleanup is risky for non-technical users because truth, evidence, cache, and generated files look similar.

Direction: move from advisory dry-run only toward explicit, user-approved cleanup actions with protection rules, previews, and rollback notes.

First implementation shape: harden previews and protected-file classification before any mutating cleanup command.

Guardrails: do not delete, archive, move, compact, or rewrite files without explicit approval and a preview.

Promotion path: create a Local Hygiene v2 PRD before adding mutation.

### Review Lanes

Problem: specialists such as design, security, QA, docs, release, and performance reviewers are useful, but persona sprawl would overwhelm builders.

Why it matters: Precode can translate specialist judgment into acceptance questions without making the user manage a fake team.

Direction: add optional review lane templates that attach to beads and produce evidence or findings.

First implementation shape: start with two lanes, likely security and release/docs freshness, before broader lane expansion.

Guardrails: review lanes must not override active beads or owner files.

Promotion path: create a review-lane PRD and implement one or two templates first.

### Verification And Release Evidence

Problem: evidence quality should scale with risk, but Precode should avoid enterprise ceremony for small tasks.

Why it matters: builders need to know what proof is strong enough for the surface being changed.

Direction: add risk-based test matrix, requirement-to-test traceability, browser evidence, screenshot/log references, NFR checks, and release gates.

First implementation shape: extend Verification Guardrail guidance and checker warnings before enforcing anything.

Guardrails: generated advisory checks are not proof of done.

Promotion path: create a verification-evidence bead tied to release readiness.

## P3: Expand Carefully

### External Status Integrations

Problem: GitHub, CI, deployment, monitoring, dependency, and uptime status live outside Precode.

Why it matters: external status can reveal blocked or risky work, but it must remain evidence rather than authority.

Direction: expand read-only integrations and scheduled audit summaries.

First implementation shape: improve GitHub first, then provider-optional deployment and monitoring checks.

Guardrails: do not comment, merge, deploy, roll back, mutate dashboards, or store secrets.

Promotion path: create provider-specific beads only after read-only contracts are stable.

### Optional Precode Packs

Problem: Precode needs extensibility without making the core bloated.

Why it matters: packs can add domain workflows while preserving tiny active memory.

Direction: define optional packs for planning, UI review, security, release, docs, and existing-repo intake.

First implementation shape: document pack boundaries and create one exemplar pack.

Guardrails: packs must not add active-memory files or weaken one-owner-per-fact rules.

Promotion path: create an Extension Protocol follow-up bead.

### Tool Execution Ledger v2

Problem: important tool actions are not always verification, but they still matter for audit and recovery.

Why it matters: builders need to distinguish "the agent ran a tool" from "a check proved the work."

Direction: improve classification, approval notes, stale evidence warnings, and command-risk visibility.

First implementation shape: harden `log-tool-run.sh` and `tool-execution-check.py`.

Guardrails: tool-run logs must not count as verification unless recorded through checks or accepted closeout evidence.

Promotion path: create a Tool Execution v2 bead.

### File Inventory / Versioning Enforcement

Problem: Precode now has many owned files, and stale inventory or version gaps can hide drift.

Why it matters: maintainers and agents need reliable file maps, but enforcement should not become noisy before migration stabilizes.

Direction: move advisory inventory/version warnings toward stronger validation once the file set is stable.

First implementation shape: improve `version-check.py`, `file-inventory.py --check`, and generated inventory references.

Guardrails: do not manually version generated reports.

Promotion path: create a versioning enforcement bead after advisory output is clean.

### AFK / Delegation Safety Improvements

Problem: unattended or parallel agent work can create scope and evidence drift.

Why it matters: AFK candidates should be bounded, checkable, and reviewable without implying approval for autonomous work.

Direction: clarify AFK candidate rules, stop conditions, evidence requirements, and re-entry checks.

First implementation shape: update decomposition, user guide, and checker warnings.

Guardrails: AFK metadata must not activate parallel execution or bypass human review.

Promotion path: create a delegation safety bead.

### Ubiquitous Language / Glossary Hardening

Problem: product language can drift across PRDs, code, UI, and memory.

Why it matters: shared vocabulary helps agents preserve the user's intent without relying on chat memory.

Direction: improve glossary card workflows, freshness checks, examples, and naming review prompts.

First implementation shape: strengthen the Ubiquitous Language Protocol and memory-index guidance.

Guardrails: glossary cards are evidence only and must not override current code, active beads, approved PRDs, or owner files.

Promotion path: create a glossary hardening bead.

### Handoff Packet Improvements

Problem: handoff packets orient future agents, but can become misleading if stale or treated as instructions.

Why it matters: better handoff improves continuity while preserving active memory as the starting point.

Direction: improve handoff packet freshness, missing-field warnings, next-safe-action phrasing, and generated-report warnings.

First implementation shape: update completion/handoff checks and generated packet copy.

Guardrails: handoff packets must not approve transitions or activate work.

Promotion path: create a handoff improvement bead.

## How To Add A New Candidate

1. Name the candidate in one plain-English phrase.
2. Write the problem it solves.
3. Score it using the rubric in this file.
4. Assign size: `S`, `M`, or `L`.
5. Assign priority: `P0`, `P1`, `P2`, or `P3`.
6. Compare it against existing candidates.
7. Add it to the ranked table only after deciding what it displaces, follows, or depends on.
8. Record whether it needs a PRD, authority-doc update, candidate bead, or research comparison before implementation.

New candidates should improve Precode's mission: helping non-technical builders use AI coding agents with orientation, scope control, evidence, human approval, and recovery.
