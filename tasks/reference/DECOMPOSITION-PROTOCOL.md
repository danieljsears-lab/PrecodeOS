# PrecodeOS -- Decomposition Protocol
<!-- ANCHOR: decomposition-protocol -->

> AUTHORITY: Bead decomposition rules, not-a-bead-yet criteria, slicing patterns, dependency mapping terms, planning-versus-execution boundaries, and appetite guidance for PrecodeOS.
> NOT_AUTHORITY: Active memory, task selection, product decisions, implementation plans, generated progress state, or automatic bead activation.
> LOAD_WHEN: Turning PRDs, source intake, GitHub issues, rough plans, or review findings into candidate beads; splitting broad work; or reviewing whether a bead is small enough to activate.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.16
Last updated: 2026-07-04

## Purpose

Decomposition turns a shaped destination into journey units small enough to verify.

This protocol helps Precode avoid premature implementation, overbroad beads, hidden dependencies, and mixed planning plus coding.

In the first-product spine, decomposition starts only after human-reviewed PRD shaping and approval: `Idea -> Brief -> Packet -> Intake -> PRD -> Bead -> Proof -> Review -> Close`. Decomposition may propose candidate beads, but it does not activate them; proof, review, and closeout remain separate later gates.

Use `tasks/reference/INTENT-ORCHESTRATION-PROTOCOL.md` when a candidate bead comes from changed, superseded, deferred, queued, or source-heavy intent and needs a clear promotion path before activation.

Use `tasks/reference/CANDIDATE-QUEUE-PROTOCOL.md` when the source is a Candidate Queue entry. Queue entries, product-value ratings, themes, and near-bead sketches can inform decomposition only after the relevant PRD, decision, or owner file is ready; the queue itself does not authorize bead creation or activation.

Use `tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md` before decomposition when the right next workflow is still unclear.

Use `tasks/prds/PRD-036-task-suitability-split-heuristics.md` and the task-suitability questions before proposing or activating a candidate bead when the work may be broad, proof-unclear, approval-gated, or easy to mistake for one task. Suitability guidance may recommend `continue`, `clarify`, `route`, `split`, `block`, or `stop`, but it does not create candidate beads, activate work, approve PRDs, or authorize implementation.

Use Plan Mode before decomposition when a selected Candidate Queue entry needs an implementation plan. In Codex, use `/plan`; in Claude Code, use Plan Mode; in other agents, use an equivalent read-only planning mode. The implementation plan is evidence only until the owning PRD, decision, owner-file, Architecture Shaping when needed, and Decomposition review support a candidate bead proposal.

Use Plan Loop before decomposition when the user explicitly asks to explore a feature angle, option, risk, or first-slice question before committing it to a bead proposal. A Plan Packet is evidence only; it can inform Decomposition, but it does not create candidate beads or authorize activation.

Use an exploratory prototype bead when a student needs Build-React-Learn in the real repo: one tiny reversible option or vertical slice, normal activation, bounded files in play, checks, stop conditions, and closeout that decides whether to keep, revise, rebuild, discard, split, or promote learning. This is a bead pattern, not a new mode, bead-kind enum, task selector, or approval path.

Use `tasks/reference/LONG-HORIZON-PLANNING-PROTOCOL.md` when candidate beads, dependencies, blocked work, or deferred slices need long-horizon review before activation.

Use `tasks/reference/ARCHITECTURE-SHAPING-PROTOCOL.md` before decomposition when an approved PRD needs `PRD+architecture` or `PRD+architecture+test-plan` planning depth, or when it touches auth, data models, APIs, integrations, dependencies, migrations, external services, multi-step workflows, or multi-system changes.

Use `scripts/prd-handoff-readiness.py --prd <path> --target decomposition` when an approved PRD looks ready but the handoff into candidate beads is unclear. Unresolved PRD handoff blockers must route back to PRD amendment, Architecture Shaping, or unblocker planning before any bead activation. The packet is generated evidence only; it does not create candidate beads, choose their order, approve the PRD, or authorize implementation.

Use `tasks/reference/SYSTEM-DESIGN-PATTERN-PROTOCOL.md` after or alongside Architecture Shaping when the candidate work needs an external service boundary, state flow, strategy-style rule boundary, auth/access boundary, audit trail, deep module boundary, or direct-versus-pattern decision.

Use `tasks/reference/AGENT-ROUTING-PROTOCOL.md` when decomposition affects model tier, subagent delegation, long-horizon execution, or context-budget decisions.

Use `tasks/reference/TEAM-COLLABORATION-PROTOCOL.md` when a small team wants multiple people to work on the same product build or when a candidate bead is marked `can run in parallel`.

Use `tasks/beads/BEAD-SCHEMA.md` for the recommended bead kind menu when choosing whether a candidate is intake, shaping, implementation, repair, refactor, setup/integration, unblocker, or review work. Treat that menu as guidance only: a bead-kind label does not make a candidate valid if it fails the decomposition test.

Active memory remains exactly:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

## Bead Decomposition Test

A candidate bead is ready to propose only when it has:

- one observable outcome
- one primary authority file
- one main verification strategy
- explicit delegation mode
- explicit test strategy when code changes
- explicit review context
- adaptive depth when risk affects ceremony: `complexity`, `required_planning_depth`, and `autonomy_level`
- bounded files in play
- clear dependency status
- clear stop conditions
- no mixed planning plus implementation
- no hidden user approval gate
- Architecture Brief evidence or an explicit low-risk skip reason when `required_planning_depth` is `PRD+architecture` or `PRD+architecture+test-plan`

If the bead needs a second primary authority, a second outcome, a second proof strategy, a second risk model, or a separate approval gate, split it.

`bead_kind` should describe the candidate's work shape, not replace decomposition judgment. If the plain-language label and frontmatter value differ, use the closest currently recognized frontmatter value from `tasks/beads/BEAD-SCHEMA.md` and explain the user-facing label in notes or handback.

## Not A Bead Yet

Use `not a bead yet` when the work has:

- unclear user problem
- vague acceptance oracle
- multiple authority owners
- unresolved sensitive-surface approval
- unknown verification path
- broad "make it better" scope
- unclear dependency order
- missing PRD approval for product feature work
- missing Architecture Brief evidence for architecture-sensitive approved PRDs
- implementation-changing open questions
- multiple outcomes, owner surfaces, proof paths, approval gates, or risk models

The next output should be source intake, PRD shaping, decision logging, architecture/security/API/schema clarification, or an unblocker bead.

## Slicing Patterns

Use the slice that best reduces risk:

| Pattern | Use When |
|---|---|
| Vertical slice | One narrow user behavior needs UI, API, and data together |
| Walking skeleton | The system needs the smallest end-to-end path before feature depth |
| Risk-first slice | One unknown can invalidate the rest of the plan |
| Exploratory prototype slice | The student needs a small reversible build to compare approaches before committing the product path |
| Shell-first slice | Structure or navigation must exist before behavior |
| Cleanup slice | Refactor or remove clutter without changing product behavior |
| Review slice | Evidence, acceptance, or transition safety needs review before more work |
| Manual setup slice | External UI, dashboard, billing, secret, or user-only setup blocks progress |
| Unblocker slice | One narrow blocker must be resolved before the original bead continues |

Do not combine slicing patterns unless the work is still one logical unit with one verification strategy.

For user-facing behavior, reject first beads that are only `schema first`, `backend first`, `frontend first`, `service first`, or `tests later` unless the bead is explicitly a risk-first or unblocker slice. Those are usually horizontal slices that delay end-to-end feedback.

A strong first vertical slice should cross enough layers to produce something observable, even if the UI, rules, data shape, or edge cases are intentionally thin.

## Dependency Mapping Terms

Use these terms in bead notes, handback, or planning output:

- `blocks`
- `blocked by`
- `can run later`
- `can run in parallel`
- `waits for manual setup`
- `waits for PRD approval`
- `waits for external status`

`can run in parallel` means the candidate may run in a branch/worktree-isolated teammate context after coordinator approval and with its own bounded bead evidence. `scripts/team-collaboration-check.py` may provide read-only preview evidence for branch/worktree state, owner-file impacts, and re-entry risk, but the preview does not approve parallel work, activate multiple beads in one checkout, allow simultaneous edits to one active memory set, bypass review, or let GitHub issues, pull requests, comments, or project boards choose work.

Use these delegation terms in bead frontmatter:

- `human_in_loop` — the builder must actively answer, judge, QA, or approve during the work
- `afk_candidate` — a coding agent can plausibly execute the scoped work after context is loaded
- `human_required` — the work depends on human-only access, taste, domain judgment, or approval

`afk_candidate` does not activate parallel execution, choose a smarter model, authorize subagents, widen files in play, or bypass review. It only describes whether a scoped bead is safe to hand to an agent after context is loaded.

Before marking a bead `afk_candidate`, verify that it has bounded files in play, explicit checks, explicit stop conditions, a declared `test_strategy`, a declared `review_context`, and no hidden approval gate. It should be possible for the builder to return later, reload the Context Pack, inspect recorded evidence, and decide whether the next action is continue, review, split, or block.

Use `bounded-afk` as the stronger `autonomy_level` only when work may continue while the builder is away. Bounded-AFK work should usually include a Run Contract with allowed actions, proof needed, approval required before risky actions, stop conditions, rollback or blocked escape, and re-entry evidence. This is advisory execution policy, not autonomous permission.

Keep solo AFK and small-team parallelism separate:

- `afk_candidate` / `bounded-afk` describe one active bead in one checkout while the builder may be away.
- `can run in parallel` describes branch/worktree-isolated teammate work after coordinator approval.
- Neither label approves activation, review acceptance, merge, external mutation, or scope expansion.

When a candidate depends on cloud-agent, PR, teammate branch/worktree, or delegated-agent return, require re-entry evidence before the next bead or merge decision. The candidate should be able to return scope, changed files, checks and results, manual verification, approval still required, unresolved risks, external status evidence, forbidden actions not taken, and a next human action of continue, review, split, block, or handoff. Do not use that evidence to approve activation, merge, transition, or external mutation.

If a dependency blocks activation, it belongs in `depends_on`, the PRD open questions, or a named unblocker bead.

## Planning Vs Execution Boundaries

Planning beads may produce:

- source summaries
- PRFAQ-lite drafts
- PRD drafts or amendments
- open questions
- architecture or risk notes
- candidate requirements
- candidate bead proposals

Planning beads should not edit app code.

Execution beads may produce:

- implementation changes
- focused refactors
- tests or checks
- recorded evidence
- closeout notes

Execution beads should not reshape product definition. If new product scope appears, stop and promote it through PRD or decision ownership.

Exploratory prototype beads may edit app code, but their purpose is learning. They must state what option is being tested, what evidence would make the student keep or discard it, and what should happen after review. Keeping the prototype as retained product work requires normal evidence and review. Rebuilding or discarding it is not failure; route the learning to PRD amendment, Plan Loop, Hypothesis Review / Learning Loop, Candidate Queue, a decision, or a new candidate bead.

When deriving beads from a PRD, treat the PRD as the destination document and each bead as one journey unit. A Candidate Queue ID may explain where the intent came from, and near-bead sketch IDs like `CQ-001-short-name-S01` may explain early shaping, but the queue does not replace parent PRD, requirement IDs, primary authority, checks, stop conditions, or final bead IDs. Use Architecture Shaping first when architecture-sensitive risk could change owner files, approval gates, verification, or decomposition. `tasks/todo.md` remains the active journey pointer; do not activate proposed journey units without the normal transition gate.

A Plan Packet may explain the explored angle, options considered, risks, and a stage-appropriate first-slice sketch. It does not replace the parent PRD, Architecture Brief, owner-file decision, or Bead Decomposition Test. If the Plan Packet still contains implementation-changing uncertainty, mark the candidate `not a bead yet` and route back to PRD amendment, Architecture Shaping, owner-file update, Product Discovery, Candidate Queue, or stop.

External sprint plans, Ember `Backend-dev-plan.md` sprints, backend implementation lists, or client project plans are source inputs for decomposition, not beads by default. Use `tasks/reference/CLIENT-ENGAGEMENT-INTAKE-PROTOCOL.md` when those plans arrive from a client engagement. Precode may split, merge, reorder, defer, or reject external sprint items so each candidate bead still has one outcome, one primary authority, bounded files in play, checks, and stop conditions.

## Appetite And Timebox

Use appetite to keep work finite:

| Appetite | Intended shape |
|---|---|
| `tiny` | One small doc, config, script, copy, or isolated fix |
| `small` | One narrow behavior or setup step, usually one session |
| `medium` | One verifiable slice with multiple files but one outcome |

Adaptive-depth fields make appetite machine-readable:

| Field | Values | Use |
|---|---|---|
| `complexity` | `trivial`, `narrow`, `standard`, `high-risk`, `multi-system` | Describes risk/size so tiny work stays light and risky work gets more scrutiny. |
| `required_planning_depth` | `none`, `brief`, `PRD`, `PRD+architecture`, `PRD+architecture+test-plan` | Describes how much product/architecture/test planning must exist before work starts. |
| `autonomy_level` | `supervised`, `bounded-afk`, `human-only` | Describes whether an agent can work after context load or whether human action/judgment owns the step. |

Use `python3 scripts/bead-depth-check.py` to surface advisory mismatches, such as a high-risk bead with brief planning or a bounded-AFK bead without checks and stop conditions.

The checker is a routing aid, not a gate. If it warns, classify the mismatch before activation:

- invalid or missing metadata: fix the field or accept the inferred default for legacy/tiny work
- low-risk work with heavy planning ceremony: lower the declared depth or record the hidden risk
- broad work declared `trivial`: narrow the files in play or split the bead
- high-risk, sensitive, or multi-system work with weak planning: add PRD, Architecture Brief, test-plan, approval, rollback, or blocked-escape detail
- high-risk work with weak proof: add manual, browser, integration, or external verification
- `bounded-afk` work without checks or stop conditions: add them before delegation
- `human-only` work without a manual gate: name the user approval, dashboard step, external action, or human-owned judgment

Split when:

- files in play grow beyond the bead's expected scope
- risk level changes
- a second primary authority, outcome, proof strategy, risk model, or approval gate appears
- implementation-changing unknowns appear
- verification requires a different strategy
- manual setup blocks progress
- the done-when statement contains "and then"
- task suitability returns `split`, `route`, `block`, or `stop`

For `PRD+architecture` and `PRD+architecture+test-plan` beads, do not propose implementation beads until Architecture Brief evidence exists or the PRD/bead notes explain why Architecture Shaping was safely skipped.

## Decomposition Review Checklist

Before activating a bead, ask:

```text
Does this bead have one observable outcome?
Does it name exactly one primary authority?
Is the verification strategy known?
Are files in play bounded?
Are dependencies clear?
Are sensitive approval gates resolved or named?
Is this planning, execution, review, setup, or unblocker work?
Would task suitability return continue, clarify, route, split, block, or stop?
What should be deferred?
```

Candidate beads remain proposals until user-approved activation through the normal Precode transition gate.
