# PrecodeOS — Bead Schema
<!-- ANCHOR: bead-schema -->

> AUTHORITY: Execution-bead format, bead states, and the `tasks/todo.md` to bead relationship.
> NOT_AUTHORITY: Product requirements, route structure, schema definitions, or generated progress.
> LOAD_WHEN: Creating, updating, or validating a bead in the scalable execution layer.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.24
Last updated: 2026-07-04

## Purpose

A bead is the smallest durable execution unit in the PrecodeOS loop system.

`tasks/todo.md` keeps the current pointer.
Each bead holds the full contract for one logical unit of implementation or review.

For small team work, the one-active-bead rule still applies inside each checkout. Parallel teammate work requires branch/worktree isolation plus the Small Team Collaboration Lane; it does not mean one Precode state may contain multiple active beads.

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

`bead_id` values are unique, never reused, monotonic, and gap-tolerant. A skipped number is acceptable; a duplicate is not. Use `python3 scripts/next-id.py bead` to suggest the next free bead ID before creating or repairing a bead. The helper is read-only: it does not reserve IDs, rename files, approve beads, activate work, or update references.

## Recommended Bead Kind Menu

`bead_kind` is a work-shape hint, not a hard public enum, backlog category, or approval path. Use it to make the bead easier to route and review while preserving the core bead contract: one observable outcome, one primary authority, one main verification strategy, bounded files in play, clear stop conditions, and no hidden approval gate.

Use these user-facing labels when explaining bead options, and prefer the mapped frontmatter value when creating or amending a bead:

| User-facing label | Preferred `bead_kind` value | Use when |
|---|---|---|
| Intake | `source_intake` | Collecting and summarizing source material before PRD shaping, decision logging, or candidate bead proposal. Use `source_intake` instead of `collector`; source intake is evidence only and does not approve work. |
| Shaping | `planning` | Turning uncertainty into PRD drafts, architecture notes, decisions, open questions, or candidate beads without editing app code. Use `prfaq` or `challenge` for narrow challenge-style planning when that wording is clearer. |
| Implementation | `implementation` or `feature` | Building one approved requirement slice with PRD traceability, checks, and closeout evidence. |
| Repair | `bugfix` | Fixing one reproducible defect or stable narrow breakage without widening into broader cleanup. |
| Refactor | `refactor` | Improving structure without changing product behavior. Use `cleanup` only as explanatory prose unless a local project deliberately recognizes it. |
| Setup / integration | `setup`, `external_integration`, or `manual_dashboard` | Completing scaffold, environment, dependency, third-party service, credential, dashboard, or other setup-bound work with the required approval gates. |
| Unblocker | `unblocker` | Resolving one narrow blocker before the original bead can continue. |
| Review | `review` | Reviewing evidence, acceptance, release/docs freshness, security, dependency relationships, or transition safety for one active bead. |

Do not create new bead-kind values just to make a menu feel complete. If a label is not recognized by current scripts, use it as plain-language explanation and set `bead_kind` to the closest existing value. `complexity`, `required_planning_depth`, `autonomy_level`, `verification_type`, and the Run Contract carry risk and ceremony; do not overload `bead_kind` with those decisions.

Exploratory prototype beads use this same menu. Do not add a new `prototype` bead kind for Build-React-Learn work. Use the closest existing value, usually `implementation`, `feature`, or `planning`, and describe "exploratory prototype" in the bead objective, notes, stop conditions, and closeout.

## Recommended Frontmatter Keys

These keys are optional for backward compatibility but recommended for new or amended beads:

- `delegation_mode` — `human_in_loop | afk_candidate | human_required`
- `test_strategy` — `failing_first | characterization | static_only | manual_only | not_applicable`
- `review_context` — `same_session_ok | fresh_context_recommended | fresh_context_required`
- `complexity` — `trivial | narrow | standard | high-risk | multi-system`
- `required_planning_depth` — `none | brief | PRD | PRD+architecture | PRD+architecture+test-plan`
- `autonomy_level` — `supervised | bounded-afk | human-only`
- `run_contract` — optional future structured form for risk-triggered allowed actions and proof needed
- `ralph_enabled` — `true | false`, opt-in marker for bounded Ralph attempt loops
- `ralph_max_attempts` — positive integer retry budget for Ralph, default `3`
- `ralph_retry_policy` — `bounded | ask_after_failure | stop_on_first_failure`
- `ralph_validator_set` — optional list of validator names or commands for Ralph
- `ralph_failure_budget` — short plain-English stop threshold

`delegation_mode` describes whether a scoped bead is safe to hand to an agent after context is loaded. It does not activate parallel work, approve autonomous execution, bypass human review, or override the one-active-bead rule.

`test_strategy` records how the bead should prove behavior. Prefer `failing_first` for code-changing beads when a useful test boundary exists.

`review_context` records whether review can happen in the same session or should reload the work in a fresh context before acceptance.

`complexity`, `required_planning_depth`, and `autonomy_level` are advisory adaptive-depth fields. They help Precode scale ceremony up or down without changing the one-active-bead rule. Existing beads may omit them; Precode infers beginner-readable defaults for backward compatibility. `python3 scripts/bead-depth-check.py` reports advisory warnings when declared depth looks inconsistent with risk, files in play, checks, stop conditions, proof strength, or human approval gates. Treat warnings as routing prompts: fix the metadata, add rationale, strengthen proof, ask for approval, or split the bead.

`run_contract` is optional for ordinary beads and expected only when work is sensitive, external, destructive, or `bounded-afk`. Because Precode's frontmatter parser is intentionally simple, new beads should usually express this as a `Run Contract` section unless a richer adapter emits structured frontmatter. Bounded-AFK Run Contracts should make re-entry review possible by naming allowed actions, proof needed, approval required before risky actions, stop conditions, rollback or blocked escape, and the evidence a returning builder should inspect.

Ralph fields are optional and should appear only when a bead is testable enough for bounded retry. Ralph opt-in does not run automatically, approve attempts, widen files in play, accept review, or activate the next bead.

Frontmatter is the canonical machine-readable metadata surface.
The mirrored sections below stay readable for humans and for transition-safe validation, but runtime scripts should prefer frontmatter and compiled sidecars over ad hoc prose parsing.

Use `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md` when choosing `verification_type`. Prefer the tier names `static`, `unit`, `integration`, `browser`, `manual`, and `external` for new beads.

When the bead's acceptance confidence depends on a specific requirement ID, bug behavior, or acceptance criterion, keep a compact requirement-to-proof trace in the bead body or Closeout Evidence. Name the requirement, bug behavior, or acceptance criterion; evidence lane; recorded source; what the evidence proves; what it does not prove; and remaining uncertainty. This is optional evidence framing for proof-sensitive work, not required ceremony for every tiny bead and not proof by itself.

Use `tasks/reference/DECOMPOSITION-PROTOCOL.md` when creating, reviewing, or splitting beads. Candidate beads should pass the Bead Decomposition Test before activation.

Use `tasks/prds/PRD-036-task-suitability-split-heuristics.md` or `python3 scripts/task-suitability-check.py --check` when a candidate or active bead may not be clear enough, small enough, proof-ready enough, or bounded enough to continue. Suitability output is advisory only: it may recommend `continue`, `clarify`, `route`, `split`, `block`, or `stop`, but it does not approve PRDs, activate beads, authorize implementation, accept review, approve commands, or create proof.

Use `tasks/reference/TEAM-COLLABORATION-PROTOCOL.md` when a bead is assigned to a teammate branch/worktree, when a candidate is described as `can run in parallel`, or when a coordinator needs merge/re-entry evidence. `python3 scripts/team-collaboration-check.py` can provide read-only preview evidence for branch/worktree state, owner-file impacts, stale re-entry risk, and optional GitHub status, but it does not approve parallel work, activate beads, accept implementation, or approve merge.

Use `tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md` when deciding whether the next artifact should be source intake, PRD shaping, decomposition, a planning bead, an implementation bead, a review bead, an unblocker, or state repair.

Use `tasks/reference/LONG-HORIZON-PLANNING-PROTOCOL.md` when reviewing ready, blocked, deferred, follow-up, or PRD-approved work that should remain non-active until promoted.

Use `tasks/reference/GOAL-FRAME-PROTOCOL.md` when a bead needs execution-level orientation from a reviewed Goal Frame. Goal Frames are advisory orientation only; they do not activate beads, approve transitions, or replace `tasks/todo.md`.

Use `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md` when closing a session, reviewing closeout, preparing handoff, or checking transition readiness.

Use `tasks/reference/RELEASE-READINESS-PROTOCOL.md` when a completed or nearly completed bead may affect users, production, deployment, external services, documentation needed for use, or post-release support. Release readiness prepares evidence and approval questions; it does not deploy, approve release, accept review, or activate the next bead.

A release-relevant bead may include a Release Candidate Evidence Profile when the work is nearly ready for a human release decision. Keep it in the bead body or closeout, not as required frontmatter. The profile should name the candidate label, release target, changed surfaces, affected users or workflows, checks, smoke path, manual/browser verification, docs/support freshness, rollback or blocked escape, known risks, approvals still required, and decision state. The decision state is evidence framing only: `candidate`, `needs evidence`, `blocked`, or `ready for human release decision`.

When release confidence depends on a specific requirement, behavior, or non-functional expectation, include verification and release evidence in the bead body or closeout. Name the requirement or behavior proven, evidence lane, recorded source, smoke path and result, docs/support freshness, rollback or blocked escape, approvals still required, decision state, and remaining uncertainty. This trace is advisory evidence framing only; it does not approve release, accept review, create generated proof, add required frontmatter, or create a new evidence report.

Use the Review Lanes Protocol, `tasks/reference/REVIEW-LANES-PROTOCOL.md`, when a completed or nearly completed bead needs a Security Review Lane, Release / Docs Freshness Review Lane, Dependency Graph Review Lane, Engineering Quality Review Lane, or PRD Quality Review Lane. Keep review lane output in the bead body or closeout, not as required frontmatter. Review lanes produce findings, missing proof, acceptance questions, a recommendation, approvals still required, and a promotion path. They do not accept implementation, approve review decisions, approve release, certify security or compliance, certify code quality, certify production readiness, create follow-up tasks, override owner files, create scorecard or checker authority, or activate another bead.

Use `tasks/reference/TOOL-EXECUTION-PROTOCOL.md` when a bead expects approval-required, external, destructive, secret-bearing, or important non-check tool calls. Logged tool runs are not passing verification unless also recorded through `record-check.sh` or accepted in Closeout Evidence.

Use `tasks/reference/RALPH-LOOP-PROTOCOL.md` when enabling, running, or reviewing bounded Ralph attempts for one active bead.

Use `tasks/prds/PRD-023-implemented-bead-reversal-workflow.md` when already-implemented work must be undone, removed, replaced, or superseded. A reversal is a separate normal bead. The prior bead stays `done` historical evidence; do not reopen it, delete evidence, rewrite transition logs, or treat Git revert alone as completion proof.

A reversal bead should use the closest existing `bead_kind` value such as `bugfix`, `refactor`, or `implementation`. Do not invent a new `reversal` state or hard enum for v1. The bead body or Closeout Evidence should name:

- Superseded bead
- Reversal target
- Reversal reason
- Preserved behavior
- Reversal proof
- Approvals still required

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

## Exploratory Prototype Beads

Use an exploratory prototype bead when a student needs to build a tiny reversible option or vertical slice in the real repo before deciding whether that path should be kept, revised, rebuilt, discarded, split, or promoted into product direction.

This is a bead pattern, not a new mode, schema enum, approval path, or permission to code. The bead still needs normal activation, one active bead, one primary authority, bounded files in play, checks, stop conditions, and Closeout Evidence.

Build-React-Learn means:

- Build: implement one tiny reversible prototype option inside the current PRD, PRD draft, Plan Packet, or approved exploratory scope.
- React: review what the student or user saw, what worked, what failed, what changed their mind, what evidence exists, and what the prototype does not prove.
- Learn: decide whether to keep, revise, rebuild, discard, split, amend the PRD, run Plan Loop, use Hypothesis Review / Learning Loop, park a Candidate Queue item, or propose the next candidate bead.

Closeout Evidence for an exploratory prototype bead should include `Prototype decision: keep | revise | rebuild | discard | split | promote learning to PRD/decision`, plus a short reason and the next safe Precode workflow. A working prototype proves only that the prototype can work; it does not approve product direction, accept implementation, or activate another bead.

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
- `bead_id` must be unique across bead files and must match the `B###` prefix in the bead filename. `bash scripts/validate-memory.sh` fails on duplicates or filename/frontmatter mismatch.
- In small team work, only one bead may be `in_progress` per checkout; parallel beads must use separate branches or worktrees and return through coordinator review before integration. Team preview output is generated evidence only.
- Every bead must name exactly one primary authority file.
- `tasks/todo.md` and the bead frontmatter should agree on the active bead and its current state.
- Product-feature beads must cite one parent PRD shard and the requirement IDs they implement.
- Code-changing beads should declare `test_strategy` and `review_context`.
- New or amended beads should declare `complexity`, `required_planning_depth`, and `autonomy_level` when the risk level affects planning, verification, delegation safety, or human approval gates.
- `afk_candidate` beads must have bounded files in play, explicit checks, stop conditions, and review evidence before acceptance.
- Sensitive, external, destructive, or `bounded-afk` beads should include a Run Contract that names allowed actions, proof needed, approval gates, stop conditions, expiration, and rollback or blocked escape.
- `tasks/todo.md` must point to the current active bead.
- If a task grows past one logical unit, split it into another bead rather than widening the current one.
- Planning beads may produce PRDs, open questions, candidate requirements, architecture notes, source summaries, or candidate beads; they should not edit app code.
- Execution beads may produce implementation changes and recorded evidence; they should not reshape product definition mid-flight.
- Run checks through `bash scripts/record-check.sh -- <command>` so command output and exit codes are recorded.
- Closeout Evidence must use a stable labeled-bullet schema and record actual command results, result, manual verification status, files changed, whether the next bead is safe to activate, review decision, drift observed, lesson to promote, follow-up bead needed, blocked escape status, and reference follow-through status when public package or maintainer-history surfaces may need review.
- Closeout Evidence should also record Build Attribution fields when contributor accountability or handoff traceability matters: `Human contributor`, `Contributor role`, `Agent/tool surface`, `Attribution reviewed by`, and `Attribution uncertainty`. These fields are reviewed attribution evidence only; they do not assign blame, score contributors, accept implementation, approve merge, or make agent/tool identity responsible for human decisions.
- Requirement-to-proof traces should be included when requirement IDs, bug behavior, or acceptance criteria are central to review confidence. Generated tests, generated properties, trace tables, screenshots, browser notes, AI critique, external status summaries, and generated reports are not complete proof without recorded checks, structured manual verification, Closeout Evidence, accepted review, or promoted follow-up evidence.
- Reference follow-through should be recorded as `Reference follow-through: resolved`, `deferred`, or `not applicable`, with a short reason. Use it to show whether public reference docs, protocols, package inventory, generated HTML freshness, maintainer changelog, or roadmap/journal history were reviewed; it is not acceptance, transition approval, or generated-output authority.
- Manual verification should use the Verification Guardrail Protocol format: who checked, what was checked, environment, result, and remaining uncertainty.
- High-risk or sensitive beads must name approval gates and rollback, blocked escape, or unblocker guidance before acceptance.
- Learning promotion is part of closeout: product or technical decisions move to `DECISIONS.md`, repeated agent mistakes move to the shared lessons/rules layer, validator misses become validator follow-up work, and authority mismatches move to the owning authority file.
- If a bead is blocked by manual setup or missing information, set it to `needs_info` or `manual_testing`, record a blocked escape path, and create or name a narrower unblocker bead instead of widening the current bead.
- Ralph-enabled beads must remain bounded to one active bead, one retry budget, declared validators, files in play, stop conditions, and human review. Ralph attempt evidence is not acceptance.
- `python3 scripts/os-health.py` compiles bead metadata into generated sidecars, including `logs/readiness.json`, `logs/next-step.json`, `logs/progress.json`, `logs/authority-map.json`, `logs/adapter-index.json`, `logs/shim-index.json`, and `logs/os-events.jsonl`.
- `accepted-hold` is a generated re-entry classification, not a bead status. It means closeout and acceptance evidence are complete while the current bead remains held because next-bead transition inputs are missing or not ready. Route to authoring or proposing the next bead; do not continue implementation, repeat acceptance review, mark the bead `done`, or activate another bead from the classification alone.
- `python3 scripts/files-in-play-check.py` compares current Git changes to the active bead `files_in_play` and warns about out-of-scope paths without approving or blocking the work.
- `python3 scripts/files-in-play-check.py --command "<command summary>"` classifies command risk as a plain `continue`, `approval needed`, or `stop` decision before the command runs.
- `python3 scripts/files-in-play-check.py --edit-lock` shows an optional advisory lock view for high-risk beads; it is evidence only, not a real filesystem lock or approval.
- `python3 scripts/ralph-loop.py` may run one explicit attempt command and a validator set for a Ralph-enabled bead, then write generated attempt evidence under `logs/`; it does not choose tasks, approve commands, accept review, or transition beads.
- `python3 scripts/bead-transition.py` may propose the next bead automatically, but `python3 scripts/bead-transition.py --approve` is required before the next bead becomes `in_progress`.
- Reversal beads follow the same one-active-bead, files-in-play, checks, closeout, review, and transition rules as every other bead. The superseded bead remains historical evidence and must not be reopened to hide or erase prior work.

## Bead Template Library

Use templates to make work easier without weakening the bead contract.

Every template still needs the required frontmatter, required sections, one primary authority file, checks, stop conditions, and Closeout Evidence.

| Template | Use When | Primary Authority Pattern |
|---|---|---|
| Feature bead | Implementing one approved PRD requirement slice | PRD shard or one feature-specific reference file |
| Bugfix bead | Repairing one reproducible defect | Bug report, acceptance doc, or codebase guide |
| Refactor bead | Improving structure without changing product behavior | Codebase guide or architecture file |
| Reversal / supersession bead | Undoing, removing, replacing, or superseding already-implemented work while preserving prior evidence | `tasks/prds/PRD-023-implemented-bead-reversal-workflow.md` plus the prior bead and current owner file |
| Setup bead | Completing scaffold, environment, dependency, or dashboard setup | Setup or deployment protocol |
| Release readiness bead | Preparing shipping evidence, smoke checks, docs freshness, rollback or blocked escape, and approval questions before user-project release | `tasks/reference/RELEASE-READINESS-PROTOCOL.md` |
| Release candidate evidence bead | Preparing or reviewing a compact candidate profile for nearly shippable user-project work before a human release decision | `tasks/reference/RELEASE-READINESS-PROTOCOL.md` |
| Review lane bead | Preparing or reviewing optional Security or Release / Docs Freshness findings for one active bead | `tasks/reference/REVIEW-LANES-PROTOCOL.md` |
| Exploratory prototype bead | Building one tiny reversible option to learn whether to keep, revise, rebuild, discard, split, or promote the learning | PRD, PRD draft, Plan Packet, or approved exploratory scope |
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
