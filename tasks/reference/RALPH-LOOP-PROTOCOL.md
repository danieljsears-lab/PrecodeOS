# PrecodeOS -- Ralph Loop Protocol
<!-- ANCHOR: ralph-loop-protocol -->

> AUTHORITY: Ralph bounded bead-attempt lifecycle, retry limits, validator-set expectations, attempt-ledger evidence shape, stop decisions, and hidden-authority guardrails for PrecodeOS.
> NOT_AUTHORITY: Active memory, task selection, product decisions, PRD approval, bead activation, review acceptance, transition approval, external mutation approval, or proof by itself.
> LOAD_WHEN: Enabling, running, reviewing, or changing Ralph-style bounded retry loops for one active Precode bead.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-13

## Purpose

Ralph is Precode's bounded bead-attempt engine.

It helps an agent and builder iterate against reality without turning retries into hidden authority. Ralph may run one explicit attempt command, run a validator set, classify the result, record generated evidence, and recommend the next move for the active bead.

Ralph must not choose a task, activate another bead, accept review, approve a transition, widen scope, rewrite owner files, or mutate external systems without the normal Precode approval gates.

Active memory remains exactly:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

## Fit

Use Ralph when all of these are true:

- one bead is active
- the bead opts in to Ralph or the user explicitly asks for a one-off Ralph run
- the work has concrete checks or validators
- files in play, stop conditions, and proof needed are clear
- failures can be classified and retried without product or architecture guessing

Do not use Ralph for:

- fuzzy product discovery
- PRD approval
- task selection
- broad refactors without bounded files in play
- auth, payments, secrets, deployments, migrations, destructive actions, or external mutation unless an approved Run Contract and explicit user gate allow the exact action
- work whose acceptance oracle is only taste, judgment, or stakeholder approval

## Bead Opt-In

Ralph is opt-in. New or amended beads may include these optional frontmatter keys:

- `ralph_enabled` -- `true | false`
- `ralph_max_attempts` -- positive integer, default `3`
- `ralph_retry_policy` -- `bounded | ask_after_failure | stop_on_first_failure`
- `ralph_validator_set` -- list of validator names or commands
- `ralph_failure_budget` -- short plain-English stop threshold

These fields do not activate Ralph automatically. They only describe whether a Ralph run is allowed and how conservative it should be.

## Attempt Lifecycle

Each Ralph run follows this lifecycle:

1. Load active memory, the active bead, and compiled state.
2. Confirm one active bead and Ralph opt-in or explicit user request.
3. Check files-in-play and Run Contract boundaries before any attempt command.
4. Run only the explicit attempt command supplied by the user or host.
5. Run the validator set.
6. Classify failure or pass.
7. Append one generated attempt entry unless running in dry-run mode.
8. Render the Ralph summary.
9. Recommend exactly one next move: `retry`, `ask`, `split`, `review`, `handoff`, or `stop`.

Ralph does not invent implementation steps. If the next implementation action is unclear, the next move is `ask`, `split`, or `stop`.

## Validator Set

The default Ralph validator set should reuse existing Precode checks:

- `bash scripts/validate-memory.sh`
- `python3 scripts/files-in-play-check.py`
- `python3 scripts/run-contract-check.py`
- `python3 scripts/tool-execution-check.py`
- `python3 scripts/loop-health.py --json`
- `python3 scripts/completion-check.py`

Beads may name a narrower or stronger validator set when the work needs specific proof. Ralph validators are evidence inputs. Passing validators still does not accept the bead.

## Attempt Ledger

Ralph generated evidence lives under `logs/`:

- `logs/ralph-attempts.jsonl`
- `logs/ralph-summary.md`

Each attempt entry should record:

- timestamp
- active bead
- attempt number
- opt-in source
- attempt command summary or `none`
- validator results
- failure category
- decision
- next recommended move
- whether another attempt is allowed
- stop reason when applicable

Do not store secrets, raw private output, credentials, dashboard values, or long command output in the Ralph ledger.

## Failure Categories

Use the smallest useful category:

- `pass`
- `validator_failed`
- `attempt_failed`
- `approval_required`
- `scope_unclear`
- `state_unclear`
- `retry_budget_exhausted`
- `missing_active_bead`
- `not_enabled`
- `unknown`

If failure repeats without new evidence, Ralph should recommend `ask`, `split`, `handoff`, or `stop` instead of burning attempts.

## Decisions

Ralph may recommend:

| Decision | Meaning |
|---|---|
| `retry` | Another bounded attempt is allowed by the bead and retry budget. |
| `ask` | Human input, approval, or missing information is needed. |
| `split` | The work no longer fits one bead or one verification strategy. |
| `review` | Evidence appears ready for human review, but not acceptance. |
| `handoff` | Context or repeated failure suggests another agent/session should reload from source state. |
| `stop` | Continuing would violate scope, approval, state, or retry-budget boundaries. |

`review` is not acceptance. `retry` is not permission to widen files in play. `handoff` is not task activation.

## Relationship To Existing Surfaces

Ralph depends on:

- the active bead contract
- Run Contracts when present
- Verification Guardrail Protocol
- Tool Execution Protocol
- Session Completion and Handoff Protocol
- generated evidence demotion rules

Ralph should feed:

- Closeout Evidence summaries when the user or agent closes the bead
- Bead Build Journal summaries when session close refreshes generated build history
- follow-up bead proposals when repeated failure reveals a real blocker
- memory or protocol promotion only after human review

## User-Facing Promise

Ralph helps users see what was tried, what reality said, why another attempt is or is not allowed, and what the next safe move is.

It is useful because failed attempts stop vanishing into chat. It is safe only if it remains bounded by one active bead, explicit checks, generated-evidence demotion, and human approval gates.
