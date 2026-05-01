# Precode OS -- Verification And Guardrail Protocol
<!-- ANCHOR: verification-guardrail-protocol -->

> AUTHORITY: Verification tiers, evidence-quality rules, risk-based check expectations, sensitive-surface approval gates, manual verification format, rollback expectations, and false-done warning patterns for Precode OS.
> NOT_AUTHORITY: Active memory, task selection, product decisions, implementation plans, generated progress state, or automatic approval of bead transitions.
> LOAD_WHEN: Creating, reviewing, or closing beads; choosing checks; working near sensitive surfaces; or evaluating whether evidence is strong enough to accept work.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-04-26

## Purpose

Verification guardrails help Precode distinguish "the agent says it is done" from recorded proof.

This protocol strengthens evidence quality without adding active memory. It does not choose tasks, approve transitions, or replace user judgment.

Use `tasks/reference/TOOL-EXECUTION-PROTOCOL.md` when a command is important but is not itself verification evidence, or when a tool call is external, destructive, secret-bearing, approval-sensitive, or failure-prone.

Use `tasks/reference/SYSTEM-DESIGN-PATTERN-PROTOCOL.md` when verification depends on a boundary shape, such as an adapter, state flow, strategy-style rule boundary, auth/access boundary, or audit trail.

Active memory remains exactly:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

## Verification Tiers

Use these tier names in bead `verification_type` whenever possible:

| Tier | Meaning |
|---|---|
| `static` | Document validation, syntax checks, lint, typecheck, schema checks, or non-runtime validation |
| `unit` | Focused tests for isolated functions, scripts, components, or utilities |
| `integration` | Tests that exercise connected modules, APIs, databases, queues, auth flows, or service boundaries |
| `browser` | Browser, Playwright, visual, responsive, accessibility, or end-to-end UI verification |
| `manual` | Human verification with a clear environment, checked behavior, result, and remaining uncertainty |
| `external` | Read-only status from GitHub, CI, deployment, uptime, monitoring, security advisory, or dashboard systems |

Legacy labels such as `doc validation` are acceptable during migration, but new beads should use the tier names.

## Evidence Vs Review Input

Evidence is durable proof:

- a command run through `bash scripts/record-check.sh -- <command>`
- closeout evidence that records actual command result and output path
- manual verification that states who checked, what was checked, environment, result, and remaining uncertainty
- an unresolved finding promoted into a follow-up bead, decision, or authority-file update

Review input is useful but not enough by itself:

- screenshots
- generated tests
- AI critique
- browser notes
- design review notes
- security or accessibility notes
- GitHub issue, PR, or CI status summaries
- external dashboard observations

Review input becomes evidence only after it is recorded, accepted, or promoted.

Use `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md` when deciding whether evidence is complete enough for review, closeout, handoff, or transition proposal.

## Minimum Expectations

Use the smallest proof that controls the risk.

| Work type | Minimum expectation |
|---|---|
| Docs-only or protocol work | `static` validation, usually `bash scripts/validate-memory.sh` |
| Script or tooling work | `static` syntax check plus dry-run or recorded command result |
| Product feature work | PRD traceability plus `static` and the narrowest useful runtime check |
| UI work | `browser` or manual visual verification in addition to static checks |
| API, data, auth, or integration work | `integration`, explicit manual approval gates, and rollback or blocked escape path |
| Deployment, migration, payments, security, or destructive work | user-approved sensitive-surface gate, `external` or manual verification, and rollback or escape path |

`validate-memory.sh` is necessary for Precode integrity, but it is not sufficient proof for every bead.

## Sensitive-Surface Gates

Pause for explicit user approval before work mutates or configures:

- authentication or authorization
- payments or billing
- personal data
- uploads or file storage
- database migrations or destructive data changes
- deployments, promotions, rollbacks, or environment variables
- GitHub issue, pull request, label, comment, merge, branch, or workflow mutation
- external dashboards
- security policy, secrets, tokens, credentials, or access control
- destructive local or external actions

Sensitive beads should name:

- exact mutation allowed
- approval gate
- secrets/privacy exclusions
- rollback or escape path
- manual verification requirement

## Manual Verification Format

Use this stable format in Closeout Evidence:

```text
Manual verification:
- Who checked:
- What was checked:
- Environment:
- Result:
- Remaining uncertainty:
```

If manual verification is not applicable, say why:

```text
Manual verification: not applicable because <reason>.
```

## Rollback And Blocked Escape

High-risk beads should record one of:

- rollback path
- blocked escape path
- narrower unblocker bead
- exact manual input needed
- reason rollback is not applicable

Do not accept high-risk work with only vague language such as "can revert if needed."

## False-Done Warning Patterns

Generated health or audit reports may warn when:

- only memory validation exists for a code-changing bead
- manual verification is missing or vague
- review decision is not accepted
- closeout exists but required checks are missing or failing
- active changes appear outside `files_in_play`
- sensitive-surface work lacks approval, manual verification, rollback, or blocked escape notes
- generated tests, screenshots, or external status are treated as proof without recorded evidence

These warnings are generated evidence only. They must not choose the next task or approve a transition.
