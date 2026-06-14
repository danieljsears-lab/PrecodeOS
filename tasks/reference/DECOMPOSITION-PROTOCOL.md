# PrecodeOS -- Decomposition Protocol
<!-- ANCHOR: decomposition-protocol -->

> AUTHORITY: Bead decomposition rules, not-a-bead-yet criteria, slicing patterns, dependency mapping terms, planning-versus-execution boundaries, and appetite guidance for PrecodeOS.
> NOT_AUTHORITY: Active memory, task selection, product decisions, implementation plans, generated progress state, or automatic bead activation.
> LOAD_WHEN: Turning PRDs, source intake, GitHub issues, rough plans, or review findings into candidate beads; splitting broad work; or reviewing whether a bead is small enough to activate.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.7
Last updated: 2026-06-14

## Purpose

Decomposition turns a shaped destination into journey units small enough to verify.

This protocol helps Precode avoid premature implementation, overbroad beads, hidden dependencies, and mixed planning plus coding.

Use `tasks/reference/INTENT-ORCHESTRATION-PROTOCOL.md` when a candidate bead comes from changed, superseded, deferred, or source-heavy intent and needs a clear promotion path before activation.

Use `tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md` before decomposition when the right next workflow is still unclear.

Use `tasks/reference/LONG-HORIZON-PLANNING-PROTOCOL.md` when candidate beads, dependencies, blocked work, or deferred slices need long-horizon review before activation.

Use `tasks/reference/ARCHITECTURE-SHAPING-PROTOCOL.md` before decomposition when an approved PRD needs `PRD+architecture` or `PRD+architecture+test-plan` planning depth, or when it touches auth, data models, APIs, integrations, dependencies, migrations, external services, multi-step workflows, or multi-system changes.

Use `tasks/reference/SYSTEM-DESIGN-PATTERN-PROTOCOL.md` after or alongside Architecture Shaping when the candidate work needs an external service boundary, state flow, strategy-style rule boundary, auth/access boundary, audit trail, deep module boundary, or direct-versus-pattern decision.

Use `tasks/reference/AGENT-ROUTING-PROTOCOL.md` when decomposition affects model tier, subagent delegation, long-horizon execution, or context-budget decisions.

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

If the bead needs a second primary authority, a second outcome, or a second risk model, split it.

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

The next output should be source intake, PRD shaping, decision logging, architecture/security/API/schema clarification, or an unblocker bead.

## Slicing Patterns

Use the slice that best reduces risk:

| Pattern | Use When |
|---|---|
| Vertical slice | One narrow user behavior needs UI, API, and data together |
| Walking skeleton | The system needs the smallest end-to-end path before feature depth |
| Risk-first slice | One unknown can invalidate the rest of the plan |
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

Use these delegation terms in bead frontmatter:

- `human_in_loop` — the builder must actively answer, judge, QA, or approve during the work
- `afk_candidate` — a coding agent can plausibly execute the scoped work after context is loaded
- `human_required` — the work depends on human-only access, taste, domain judgment, or approval

`afk_candidate` does not activate parallel execution, choose a smarter model, authorize subagents, widen files in play, or bypass review. It only describes whether a scoped bead is safe to hand to an agent after context is loaded.

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

When deriving beads from a PRD, treat the PRD as the destination document and each bead as one journey unit. Use Architecture Shaping first when architecture-sensitive risk could change owner files, approval gates, verification, or decomposition. `tasks/todo.md` remains the active journey pointer; do not activate proposed journey units without the normal transition gate.

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
- implementation-changing unknowns appear
- verification requires a different strategy
- manual setup blocks progress
- the done-when statement contains "and then"

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
What should be deferred?
```

Candidate beads remain proposals until user-approved activation through the normal Precode transition gate.
