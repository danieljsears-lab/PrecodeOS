# PrecodeOS — Bead Schema
<!-- ANCHOR: bead-schema -->

> AUTHORITY: Execution-bead format, bead states, and the `tasks/todo.md` to bead relationship.
> NOT_AUTHORITY: Product requirements, route structure, schema definitions, or generated progress.
> LOAD_WHEN: Creating, updating, or validating a bead in the scalable execution layer.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.6
Last updated: 2026-05-11

## Purpose

A bead is the smallest durable execution unit in the PrecodeOS loop system.

`tasks/todo.md` keeps the current pointer.
Each bead holds the full contract for one logical unit of implementation or review.

## Required Frontmatter Keys

- `bead_id`
- `status`
- `execution_mode`
- `bead_kind`
- `primary_authority`
- `depends_on`
- `parent_prd`
- `requirement_ids`
- `files_in_play`
- `checks`
- `verification_type`

## Recommended Frontmatter Keys

These keys are optional for backward compatibility but recommended for new or amended beads:

- `delegation_mode` — `human_in_loop | afk_candidate | human_required`
- `test_strategy` — `failing_first | characterization | static_only | manual_only | not_applicable`
- `review_context` — `same_session_ok | fresh_context_recommended | fresh_context_required`
- `complexity` — `trivial | narrow | standard | high-risk | multi-system`
- `required_planning_depth` — `none | brief | PRD | PRD+architecture | PRD+architecture+test-plan`
- `autonomy_level` — `supervised | bounded-afk | human-only`
- `run_contract` — optional future structured form for risk-triggered allowed actions and proof needed

`delegation_mode` describes whether a scoped bead is safe to hand to an agent after context is loaded. It does not activate parallel work, bypass human review, or override the one-active-bead rule.

`test_strategy` records how the bead should prove behavior. Prefer `failing_first` for code-changing beads when a useful test boundary exists.

`review_context` records whether review can happen in the same session or should reload the work in a fresh context before acceptance.

`complexity`, `required_planning_depth`, and `autonomy_level` are advisory adaptive-depth fields. They help Precode scale ceremony up or down without changing the one-active-bead rule. Existing beads may omit them; `python3 scripts/bead-depth-check.py` reports advisory warnings when the declared depth looks inconsistent with the bead's risk, files in play, checks, or stop conditions.

`run_contract` is optional for ordinary beads and expected only when work is sensitive, external, destructive, or `bounded-afk`. Because Precode's frontmatter parser is intentionally simple, new beads should usually express this as a `Run Contract` section unless a richer adapter emits structured frontmatter.

Frontmatter is the canonical machine-readable metadata surface.
The mirrored sections below stay readable for humans and for transition-safe validation, but runtime scripts should prefer frontmatter and compiled sidecars over ad hoc prose parsing.

Use `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md` when choosing `verification_type`. Prefer the tier names `static`, `unit`, `integration`, `browser`, `manual`, and `external` for new beads.

Use `tasks/reference/DECOMPOSITION-PROTOCOL.md` when creating, reviewing, or splitting beads. Candidate beads should pass the Bead Decomposition Test before activation.

Use `tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md` when deciding whether the next artifact should be source intake, PRD shaping, decomposition, a planning bead, an implementation bead, a review bead, an unblocker, or state repair.

Use `tasks/reference/LONG-HORIZON-PLANNING-PROTOCOL.md` when reviewing ready, blocked, deferred, follow-up, or PRD-approved work that should remain non-active until promoted.

Use `tasks/reference/GOAL-FRAME-PROTOCOL.md` when a bead needs execution-level orientation from a reviewed Goal Frame. Goal Frames are advisory orientation only; they do not activate beads, approve transitions, or replace `tasks/todo.md`.

Use `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md` when closing a session, reviewing closeout, preparing handoff, or checking transition readiness.

Use `tasks/reference/TOOL-EXECUTION-PROTOCOL.md` when a bead expects approval-required, external, destructive, secret-bearing, or important non-check tool calls. Logged tool runs are not passing verification unless also recorded through `record-check.sh` or accepted in Closeout Evidence.

Use `python3 scripts/run-contract-check.py` when a bead has or should have a risk-triggered run contract.

## Required Bead Sections

- `State`
- `Primary Authority`
- `Depends On`
- `Parent PRD`
- `Requirement IDs`
- `Objective`
- `Done When`
- `Files In Play`
- `Checks`
- `Verification Type`
- `Delegation Mode`
- `Test Strategy`
- `Review Context`
- `Stop If`
- `Run Contract` when the bead is sensitive, external, destructive, or `bounded-afk`
- `Closeout Evidence`
- `Handback`

## Run Contract

Use this section only when the bead needs tighter execution policy. Omit it for ordinary low-risk work.

```text
## Run Contract

- Required: true
- Allowed paths: `path/or/file.md`, `another/path`
- Allowed tool classes: `read_only`, `verification`, `local_mutation`
- Forbidden actions: deploy, merge, migrate, edit secrets
- Approval required before: external mutation, destructive command, secret-bearing action
- Proof needed: `static`, `manual`
- Stop if: allowed actions, proof needed, approval, or rollback path becomes unclear
- Rollback or blocked escape: name rollback, blocked escape, unblocker, or why rollback is not applicable
- Expires when: bead reaches review or done
```

Plain user-facing wording should be: Allowed actions, Proof needed, Approval required before, and Stop if. The internal terms are capability lease for allowed actions and proof lanes for proof needed.

## Goal Frame

Use this section only when a bead needs execution-specific orientation. Omit it for ordinary narrow beads.

- Status: `draft | active | reaffirm_needed | retired`
- Last reaffirmed: `YYYY-MM-DD`
- Owner file: `tasks/beads/<bead>.md`
- Horizon: `session | feature`
- Workflow guidance: `implementation | review | repair`
- Goal:
- Why now:
- Success signal:
- Out of scope:
- Approval gates:
- Reaffirmation trigger:

## Allowed States

- `ready`
- `in_progress`
- `needs_info`
- `manual_testing`
- `review`
- `done`

## Operating Rules

- Only one bead may be `in_progress` at a time.
- Every bead must name exactly one primary authority file.
- `tasks/todo.md` and the bead frontmatter should agree on the active bead and its current state.
- Product-feature beads must cite one parent PRD shard and the requirement IDs they implement.
- Code-changing beads should declare `test_strategy` and `review_context`.
- New or amended beads should declare `complexity`, `required_planning_depth`, and `autonomy_level` when the risk level affects planning, verification, or delegation safety.
- `afk_candidate` beads must have bounded files in play, explicit checks, stop conditions, and review evidence before acceptance.
- Sensitive, external, destructive, or `bounded-afk` beads should include a Run Contract that names allowed actions, proof needed, approval gates, stop conditions, expiration, and rollback or blocked escape.
- `tasks/todo.md` must point to the current active bead.
- If a task grows past one logical unit, split it into another bead rather than widening the current one.
- Planning beads may produce PRDs, open questions, candidate requirements, architecture notes, source summaries, or candidate beads; they should not edit app code.
- Execution beads may produce implementation changes and recorded evidence; they should not reshape product definition mid-flight.
- Run checks through `bash scripts/record-check.sh -- <command>` so command output and exit codes are recorded.
- Closeout Evidence must use a stable labeled-bullet schema and record actual command results, result, manual verification status, files changed, whether the next bead is safe to activate, review decision, drift observed, lesson to promote, follow-up bead needed, and blocked escape status.
- Manual verification should use the Verification Guardrail Protocol format: who checked, what was checked, environment, result, and remaining uncertainty.
- High-risk or sensitive beads must name approval gates and rollback, blocked escape, or unblocker guidance before acceptance.
- Learning promotion is part of closeout: product or technical decisions move to `DECISIONS.md`, repeated agent mistakes move to the shared lessons/rules layer, validator misses become validator follow-up work, and authority mismatches move to the owning authority file.
- If a bead is blocked by manual setup or missing information, set it to `needs_info` or `manual_testing`, record a blocked escape path, and create or name a narrower unblocker bead instead of widening the current bead.
- `python3 scripts/os-health.py` compiles bead metadata into generated sidecars, including `logs/readiness.json`, `logs/next-step.json`, `logs/authority-map.json`, `logs/adapter-index.json`, `logs/shim-index.json`, and `logs/os-events.jsonl`.
- `python3 scripts/files-in-play-check.py` compares current Git changes to the active bead `files_in_play` and warns about out-of-scope paths without approving or blocking the work.
- `python3 scripts/files-in-play-check.py --command "<command summary>"` classifies command risk as a plain `continue`, `approval needed`, or `stop` decision before the command runs.
- `python3 scripts/files-in-play-check.py --edit-lock` shows an optional advisory lock view for high-risk beads; it is evidence only, not a real filesystem lock or approval.
- `python3 scripts/bead-transition.py` may propose the next bead automatically, but `python3 scripts/bead-transition.py --approve` is required before the next bead becomes `in_progress`.

## Bead Template Library

Use templates to make work easier without weakening the bead contract.

Every template still needs the required frontmatter, required sections, one primary authority file, checks, stop conditions, and Closeout Evidence.

| Template | Use When | Primary Authority Pattern |
|---|---|---|
| Feature bead | Implementing one approved PRD requirement slice | PRD shard or one feature-specific reference file |
| Bugfix bead | Repairing one reproducible defect | Bug report, acceptance doc, or codebase guide |
| Refactor bead | Improving structure without changing product behavior | Codebase guide or architecture file |
| Setup bead | Completing scaffold, environment, dependency, or dashboard setup | Setup or deployment protocol |
| Planning bead | Shaping an uncertain product bet before implementation | `tasks/reference/PLANNING-PROTOCOL.md` or PRD protocol |
| PRFAQ/challenge planning bead | Hardening rough, risky, or source-heavy ideas before PRD approval | `tasks/reference/LOCAL-SOURCE-INTAKE-PROTOCOL.md` or `tasks/reference/IDEA-TO-PRD-WORKFLOW.md` |
| External integration bead | Adding or changing third-party service behavior | Integration authority plus security/payment docs when relevant |
| Manual-dashboard bead | Work depends on external UI, credentials, or user-only setup | Deployment or integration authority |
| Review bead | Reviewing evidence, acceptance, and transition safety | Bead plus primary authority |
| Unblocker bead | Narrow work that unblocks a stuck bead | Exact blocker authority |

## Decomposition Review Before Activation

Before activating a bead, confirm:

- one observable outcome
- one primary authority
- one main verification strategy
- bounded files in play
- clear dependency status
- no mixed planning plus implementation
- no hidden user approval gate
- explicit delegation mode, test strategy, and review context for new code-changing beads
- deferred work is named or explicitly out of scope

## Migrating Work Into Beads

Convert stories, GitHub issues, notes, or freeform plans into beads only after identifying:

- the parent PRD or reason no PRD is needed
- stable requirement IDs or a non-product maintenance objective
- one primary authority file
- one logical done-when target
- files likely in play
- checks and manual verification
- stop conditions

Do not copy an entire issue or story into a bead. Distill it into the execution contract and link or name the source as context.

## Review Inputs Vs Evidence

Generated tests, browser screenshots, Playwright or browser verification notes, security or accessibility notes, human QA notes, design review notes, external QA, and AI critiques from any coding agent are review inputs.

They become evidence only when:

- a command is run through `bash scripts/record-check.sh -- <command>`
- the result is recorded in Closeout Evidence
- manual verification states what was checked and the outcome
- unresolved findings become follow-up beads, decisions, or authority-file updates

Keep the distinction clear:

- "test generated" is not the same as "test passed"
- "review suggested" is not the same as "finding resolved"
- "screenshot captured" is not the same as "manual verification accepted"
- "memory validation passed" is not enough proof for every code, UI, integration, security, or deployment bead
