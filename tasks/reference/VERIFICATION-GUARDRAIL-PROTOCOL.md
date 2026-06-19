# PrecodeOS -- Verification And Guardrail Protocol
<!-- ANCHOR: verification-guardrail-protocol -->

> AUTHORITY: Verification tiers, evidence-quality rules, risk-based check expectations, sensitive-surface approval gates, manual verification format, rollback expectations, and false-done warning patterns for PrecodeOS.
> NOT_AUTHORITY: Active memory, task selection, product decisions, implementation plans, generated progress state, or automatic approval of bead transitions.
> LOAD_WHEN: Creating, reviewing, or closing beads; choosing checks; working near sensitive surfaces; or evaluating whether evidence is strong enough to accept work.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.14
Last updated: 2026-06-19

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

## Proof Needed

Risk-triggered run contracts use proof needed as the plain-language wrapper over verification tiers. Internally this is the proof-lane model: a bead can say which evidence lanes must be satisfied before acceptance.

Use the same tier names as `verification_type`: `static`, `unit`, `integration`, `browser`, `manual`, and `external`.

Proof needed does not replace checks or Closeout Evidence. It makes the expected evidence explicit so `python3 scripts/run-contract-check.py` can warn when the declared proof is not reflected in `verification_type`, recorded checks, or structured manual verification.

Ordinary low-risk beads can omit proof-needed language and rely on normal `verification_type` plus checks. Sensitive, external, destructive, or `bounded-afk` beads should name proof needed in the bead Run Contract.

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

Accessibility advisory review is opt-in. Use the Accessibility Advisor Fit Interview when the user is unsure whether accessibility review is needed, when an owner file asks for it, or when a review/release decision depends on accessibility confidence. Do not infer an accessibility gate from every UI or interface file. If the advisor is invoked, record the advisory shape in Closeout Evidence or release evidence:

```text
Accessibility advisory:
- Invocation decision:
- Target:
- Automated check evidence:
- Manual review notes:
- Unresolved findings:
- Acceptance risk:
```

Automated accessibility checks are useful when available, but they are not legal compliance proof. Manual review notes and unresolved findings remain review input until recorded in Closeout Evidence, promoted into an owner file or follow-up bead, or accepted by the user through normal review.

Use `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md` when deciding whether evidence is complete enough for review, closeout, handoff, or transition proposal.

Use `tasks/reference/RELEASE-READINESS-PROTOCOL.md` when proof is being prepared for user-project shipping, deployment readiness, smoke evidence, browser/manual release checks, docs freshness, rollback or blocked escape, or post-release review. Release readiness does not weaken sensitive-surface gates or approve release actions.

For release-relevant work, proof should trace the requirement or behavior being shipped to the evidence lane and recorded source that proves it. The trace can live in Closeout Evidence, a release-readiness note, or a Release Candidate Evidence Profile. If the requirement or behavior proven, evidence lane, recorded source, smoke path, docs/support freshness, rollback or blocked escape, approvals still required, or decision state is unclear, treat the work as `needs evidence` before release review. This is an evidence-quality warning, not release approval, review acceptance, or generated proof.

Use `tasks/reference/RALPH-LOOP-PROTOCOL.md` when the active bead is testable enough for bounded retry against a validator set. Ralph attempt results are evidence inputs; they do not replace recorded checks, closeout evidence, review, or acceptance.

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
| Release-relevant user-project work | release-readiness note, smoke evidence, docs freshness when relevant, manual or browser verification when needed, and explicit approval before release action |

`validate-memory.sh` is necessary for Precode integrity, but it is not sufficient proof for every bead.

Stable-fix eligibility requires recorded proof, not just a declared check. When `scripts/next-step.py --json` reports `stable_fix_eligibility.classification` as `needs_evidence`, record the narrowest check that proves the owner-file repair, then reassess before accepting the work. A passing `eligible_stable_fix` classification is still advisory; it does not replace Closeout Evidence, review, user approval, release readiness, or sensitive-surface gates.

For Bugfix Spec Lane work, this protocol owns the regression-proof expectation: proof must show both sides of the repair, that the named defect is fixed and the named unchanged behavior still holds. For code-changing bugfixes, prefer a failing-first check that fails for the defect before the repair, or a characterization check that pins existing behavior before the change. If failing-first or characterization proof is not practical, record why and use the narrowest available static, unit, integration, browser, or manual verification that covers current behavior, expected behavior, and unchanged behavior.

Ralph can reduce false-done risk by rerunning validators and recording failures, but a passing Ralph summary is still not acceptance. The closeout and review decision must name the evidence that proves the bead's done-when target.

Adaptive-depth metadata should raise verification expectations when risk rises. `high-risk` and `multi-system` beads should usually include manual, integration, browser, or external evidence; `human-only` beads should name the human approval or manual action; `bounded-afk` beads need bounded files in play, explicit checks, and stop conditions. If `python3 scripts/bead-depth-check.py` warns about weak proof, do not accept the bead from static validation alone unless the bead records why static proof is enough for the actual risk.

`python3 scripts/files-in-play-check.py` is an advisory guardrail that compares current Git changes to the active bead `files_in_play`. Out-of-scope warnings should be resolved by classifying each changed path as generated evidence, current-bead work that needs explicit scope approval, follow-up bead work, or user-owned revert work before acceptance.

The guardrail can also classify a proposed command with `--command "<command summary>"` and can show an optional advisory edit lock with `--edit-lock`. These checks should reduce beginner confusion by saying `continue`, `approval needed`, or `stop`; they do not grant command approval, enforce filesystem permissions, or replace sensitive-surface gates. A `continue` classification for local mutation still depends on the command staying inside `files_in_play` and avoiding dependency, migration, sensitive, external, or destructive side effects unless those are explicitly approved by the active bead and user.

Use `tasks/reference/OS-INTEGRITY-PROTOCOL.md` when the risky surface is PrecodeOS itself: active memory, protocols, maintained scripts, hooks, adapters, package docs, or public/private boundary files. `scripts/os-integrity-check.py` and `scripts/os-checkpoint.py` protect OS-owned source surfaces with explicit scoped checkpoints; they do not replace `files_in_play` checks for normal app work.

## Test Strategy

Use these `test_strategy` values in bead frontmatter when helpful:

| Strategy | Use When |
|---|---|
| `failing_first` | Code-changing work can be driven by a focused red/green/refactor loop. |
| `characterization` | Existing behavior must be pinned before refactor or repair. |
| `static_only` | Docs, schemas, metadata, or static checks are enough for the risk. |
| `manual_only` | Human QA is the acceptance oracle and automation is not practical for the slice. |
| `not_applicable` | The bead does not change behavior or code in a way that needs a test strategy. |

Prefer `failing_first` for code-changing beads when the codebase has a usable test boundary. Confirm the failing test fails for the expected reason before implementing. If failing-first is not practical, record why in the bead or Closeout Evidence.

Human QA and manual verification remain the taste and acceptance layer. Automated checks reduce risk; they do not replace human judgment for product fit, UX quality, or sensitive approval gates.

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
- adaptive-depth fields are missing or inconsistent with the bead's risk
- sensitive-surface work lacks approval, manual verification, rollback, or blocked escape notes
- generated tests, screenshots, or external status are treated as proof without recorded evidence

These warnings are generated evidence only. They must not choose the next task or approve a transition.
