# PrecodeOS -- Session Completion And Handoff Protocol
<!-- ANCHOR: session-completion-handoff-protocol -->

> AUTHORITY: Session completion, bead closeout, review, transition proposal, transition approval, and agent handoff rules for PrecodeOS.
> NOT_AUTHORITY: Active memory expansion, product decisions, task selection, automatic review acceptance, automatic bead activation, generated progress state, or external mutations.
> LOAD_WHEN: Closing a session, checking whether a bead is ready for review, preparing an agent handoff, reviewing completion evidence, or deciding whether a transition proposal is safe to approve.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.6
Last updated: 2026-06-14

## Purpose

Completion and handoff keep the end of a session as structured as the start.

This protocol distinguishes orientation, evidence, review, and activation so a finished-sounding agent response does not become automatic task completion.

Active memory remains exactly:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

## Lifecycle Actions

| Action | May do | Must not do |
|---|---|---|
| Checkpoint | validate memory, summarize current bead, log checkpoint, refresh health | accept work, approve transition, start another bead |
| Session close | refresh closeout, record validation, assess promotion, log close, update learning diary | approve review, activate next bead, rewrite product scope |
| Bead closeout | record checks, result, manual verification, changed files, drift, lesson, follow-up, blocked escape | replace review decision or user approval |
| Review | decide `accepted`, `revise`, `split`, or `blocked` | bypass missing evidence or sensitive approval gates |
| Transition proposal | show whether the compiled readiness model permits a next bead | mutate bead state or `tasks/todo.md` |
| Transition approval | after user approval, move the current bead to `done` and the next bead to `in_progress` | run without explicit approval |
| Handoff | orient another agent with a Context Pack and generated-report warning | choose tasks, approve transitions, or activate work |

## Required Completion Fields

Closeout Evidence should include:

- recorded checks
- Ralph attempt summary when the bead used Ralph
- result
- manual verification
- files changed
- next bead
- review decision
- drift observed
- lesson to promote
- follow-up bead needed
- blocked escape
- evidence source
- allowed actions and proof needed when the bead has a Run Contract
- release-readiness note when the completed work may affect users, production, deployment, external services, docs needed for use, or post-release support

For medium/high-risk code-changing beads, prefer a fresh-context review. The implementing context may be near its reasoning limit, so review should reload active memory, the bead, primary authority, parent PRD when relevant, and the diff or evidence from a clean context before acceptance.

Use `review_context` in bead frontmatter:

- `same_session_ok` — narrow low-risk work can be reviewed in the same session
- `fresh_context_recommended` — code-changing or medium-risk work should be reviewed after a context reset or handoff
- `fresh_context_required` — high-risk, sensitive, broad, or architecture-shaping work must be reviewed in a fresh context before acceptance

Manual verification should follow `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md` when it applies.

Release-relevant closeout should also follow `tasks/reference/RELEASE-READINESS-PROTOCOL.md`. The closeout should name changed behavior, affected users, smoke evidence, browser or manual verification, docs freshness, rollback or blocked escape, known uncertainty, post-release follow-up, and approval still required before any release action.

## Required Handoff Context Pack

A handoff should be able to explain:

- active bead
- state
- done-when
- primary authority
- files in play
- out of scope
- checks
- allowed actions and proof needed when the bead has a Run Contract
- stop conditions
- open questions
- latest evidence
- latest Ralph attempt decision when Ralph was used
- release-readiness status when the bead may ship to users
- blockers
- next safe action
- generated-report warning

The handoff packet is orientation only. The next agent still starts from active memory, the active bead, and the primary authority file.

## Decision Outcomes

Use these outcomes at completion time:

- `continue`: keep working inside the active bead
- `close`: stop the session with current state recorded
- `review`: ask for evidence and acceptance review
- `split`: create or propose a narrower follow-up bead
- `block`: mark missing input or blocker clearly
- `manual_testing`: wait for manual verification
- `transition_proposal`: show the next bead proposal without activation
- `transition_approval`: user explicitly approves `python3 scripts/bead-transition.py --approve`
- `handoff`: orient another agent without task activation

## Advisory Check

`scripts/completion-check.py` is advisory. It may warn about missing recorded checks, vague manual verification, invalid review decisions, unsafe next-bead references, follow-up work without a destination, vague handback, stale session close evidence, missing handoff Context Pack fields, transition eligibility that still needs user approval, or blocked work without a clear escape path.

Ralph attempt evidence may support closeout and handoff, especially after repeated validator failures. It does not replace review acceptance, transition approval, or manual verification when those are required.

Session freshness is phase-aware. Evidence newer than the latest session close is reported as `open` detail while a bead is `in_progress`; it becomes a `stale` warning when the bead is in a close-oriented state such as `needs_info`, `manual_testing`, `review`, or `done`. A session close at or after the latest recorded check is `current`; a bead without recorded checks is `no-recorded-checks`.

Warnings are generated evidence only. They do not accept work, approve transitions, activate beads, change bead state, or rewrite active memory.
