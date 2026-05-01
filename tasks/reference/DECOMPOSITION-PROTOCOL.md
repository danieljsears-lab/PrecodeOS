# Precode OS -- Decomposition Protocol
<!-- ANCHOR: decomposition-protocol -->

> AUTHORITY: Bead decomposition rules, not-a-bead-yet criteria, slicing patterns, dependency mapping terms, planning-versus-execution boundaries, and appetite guidance for Precode OS.
> NOT_AUTHORITY: Active memory, task selection, product decisions, implementation plans, generated progress state, or automatic bead activation.
> LOAD_WHEN: Turning PRDs, source intake, GitHub issues, rough plans, or review findings into candidate beads; splitting broad work; or reviewing whether a bead is small enough to activate.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-04-26

## Purpose

Decomposition turns a shaped idea into work small enough to verify.

This protocol helps Precode avoid premature implementation, overbroad beads, hidden dependencies, and mixed planning plus coding.

Use `tasks/reference/INTENT-ORCHESTRATION-PROTOCOL.md` when a candidate bead comes from changed, superseded, deferred, or source-heavy intent and needs a clear promotion path before activation.

Use `tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md` before decomposition when the right next workflow is still unclear.

Use `tasks/reference/LONG-HORIZON-PLANNING-PROTOCOL.md` when candidate beads, dependencies, blocked work, or deferred slices need long-horizon review before activation.

Use `tasks/reference/SYSTEM-DESIGN-PATTERN-PROTOCOL.md` before decomposition when the candidate work needs an external service boundary, state flow, strategy-style rule boundary, auth/access boundary, audit trail, or direct-versus-pattern decision.

Active memory remains exactly:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

## Bead Decomposition Test

A candidate bead is ready to propose only when it has:

- one observable outcome
- one primary authority file
- one main verification strategy
- bounded files in play
- clear dependency status
- clear stop conditions
- no mixed planning plus implementation
- no hidden user approval gate

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

## Dependency Mapping Terms

Use these terms in bead notes, handback, or planning output:

- `blocks`
- `blocked by`
- `can run later`
- `can run in parallel`
- `waits for manual setup`
- `waits for PRD approval`
- `waits for external status`

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

## Appetite And Timebox

Use appetite to keep work finite:

| Appetite | Intended shape |
|---|---|
| `tiny` | One small doc, config, script, copy, or isolated fix |
| `small` | One narrow behavior or setup step, usually one session |
| `medium` | One verifiable slice with multiple files but one outcome |

Split when:

- files in play grow beyond the bead's expected scope
- risk level changes
- implementation-changing unknowns appear
- verification requires a different strategy
- manual setup blocks progress
- the done-when statement contains "and then"

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
