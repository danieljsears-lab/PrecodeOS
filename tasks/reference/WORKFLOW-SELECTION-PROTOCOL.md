# PrecodeOS -- Workflow Selection Protocol
<!-- ANCHOR: workflow-selection-protocol -->

> AUTHORITY: Workflow-selection guidance for choosing the next Precode planning, execution, review, unblocker, or repair path before work starts.
> NOT_AUTHORITY: Active memory, product decisions, approved requirements, task selection, bead activation, implementation plans, generated progress state, or external mutations.
> LOAD_WHEN: Deciding which Precode workflow to use for a rough idea, local source material, PRD work, bead proposal, blocked task, review, closeout, or state repair.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.4
Last updated: 2026-05-12

## Purpose

Workflow selection helps a user or agent choose the right Precode path before starting work.

Use this protocol when the next step is unclear, when too many protocols could apply, or when an agent may be jumping from idea to implementation too quickly.

Active memory remains exactly:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

## Workflow Decision Path

When broad durable intent is present, check whether a reviewed Goal Frame exists before choosing a workflow:

```text
broad user intent -> Goal Frame proposal/reaffirmation -> workflow selection -> intake / PRD / decomposition / bead / review
```

Goal Frames are advisory orientation only. A stale, missing, or conflicting Goal Frame should trigger a reaffirmation prompt before workflow guidance.

Choose the workflow that matches the current situation:

| Current situation | Recommended workflow | Next artifact |
|---|---|---|
| Broad, risky, market-facing, paid, evidence-poor, or solution-first product idea where worth-building is uncertain | Product Discovery Validation | Discovery Summary with `proceed | pause | narrow | kill` recommendation |
| Rough idea, scattered notes, screenshots, research, chat summary, or issue export | Local Source Intake | reviewed source summary |
| Shaped idea that still needs product clarity | Idea-to-PRD / PRFAQ-lite | PRD shard draft |
| Approved PRD with stable requirement IDs | Decomposition Protocol | candidate bead proposals |
| High-risk, uncertain, or challenge-worthy idea | PRFAQ/challenge planning bead | questions, risk notes, or narrowed proposal |
| Bug, refactor, setup, review, external integration, manual dashboard work, or blocked work | matching bead template | narrow bead proposal |
| Completed, messy, or disputed work | review, closeout, state repair, or unblocker flow | recorded evidence, review decision, or repair bead |

If no row fits, stop and name what is missing: source evidence, product definition, authority owner, decomposition, verification path, approval gate, or state repair.

If the workflow involves sensitive, external, destructive, or `bounded-afk` execution, the next bead proposal should include a Run Contract or explicitly explain why one is not needed. Use plain output language: Allowed actions, Proof needed, Approval required before, and Stop if.

Use `tasks/reference/PRODUCT-DISCOVERY-VALIDATION-PROTOCOL.md` before PRD shaping when the main uncertainty is whether the user problem, current workaround, demand signal, alternative, or smallest learning step is real enough to justify product definition. Its Discovery Summary is evidence only; it may recommend `proceed`, `pause`, `narrow`, or `kill`, but it does not approve a PRD, activate beads, choose work, or rewrite owner files.

## Workflow Selection Output

When asked to choose a workflow, return:

- Current situation:
- Recommended workflow:
- Artifact to produce next:
- Required authority source:
- User approval needed:
- Run contract needed:
- Stop condition:
- Generated-report warning:

The output is guidance only. It does not approve a PRD, activate a bead, choose the next task, or rewrite owner files.

## Workflow Boundaries

- Local source summaries are evidence, not product authority.
- PRFAQ-lite and PRD drafts shape intent, but do not start implementation.
- Approved PRDs can propose beads, but do not activate them.
- Candidate beads must pass the Bead Decomposition Test before activation.
- Planning beads may produce planning artifacts, but should not edit app code.
- Execution beads may implement scoped work, but should not reshape product definition.
- Review and repair flows may identify follow-up work, but follow-up work becomes action only through the correct owner file or approved bead.
- Generated reports may warn about workflow drift, but must not drive task selection.

Use `tasks/reference/LONG-HORIZON-PLANNING-PROTOCOL.md` when workflow selection discovers future, deferred, blocked, follow-up, or PRD-approved work that should remain visible but non-active.

Use `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md` when the correct workflow is checkpoint, session close, review, handoff, or transition proposal.

Use `tasks/reference/SYSTEM-DESIGN-PATTERN-PROTOCOL.md` when workflow selection reveals a feature that needs an external boundary, state flow, strategy-style rule boundary, auth/access boundary, audit trail, or a plain-English implementation-shape choice before coding.

Use `tasks/reference/GOAL-FRAME-PROTOCOL.md` when workflow selection needs durable direction but the direction should not become a backlog, roadmap, implementation plan, or active task.

## Common Stop Conditions

Stop before work starts when:

- the problem is unclear
- no primary authority source is named
- product-feature work lacks an approved PRD or requirement IDs
- candidate work mixes planning and implementation
- the verification path is unknown
- a sensitive-surface approval gate is unresolved
- blocked work has no escape path
- generated reports or source summaries appear to be acting as authority

## Advisory Check

`scripts/workflow-check.py` is advisory. It may warn about wrong workflow fit, PRD approval gaps, approved PRDs without bead proposals, mixed planning and implementation, blocked work without an unblocker path, backlog-like active fields, or generated reports appearing to drive task selection.

Warnings are generated evidence only. They do not choose tasks, approve PRDs, activate beads, change bead state, or edit active memory.
