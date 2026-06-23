# PrecodeOS -- Review Lanes Protocol
<!-- ANCHOR: review-lanes-protocol -->

> AUTHORITY: Optional advisory review lane templates for one active bead.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, transition approval, review acceptance, implementation acceptance, release approval, security certification, compliance approval, generated proof, Work Graph authority, command approval, parallel execution approval, follow-up task creation, owner-file rewrite, external mutation, GitHub mutation, package-manager behavior, task-runner behavior, or a persona system.
> LOAD_WHEN: A user asks for a Security Review Lane, Release / Docs Freshness Review Lane, Dependency Graph Review Lane, or Review Lanes review for one active bead.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.2
Last updated: 2026-06-23

## Purpose

Review Lanes help a builder ask specialist review questions without managing fake specialist personas.

A lane attaches to one active bead and turns a narrow review concern into evidence, missing proof, acceptance questions, and a recommendation. It does not approve work, create work, replace Review mode, replace Release Readiness, replace Work Graph evidence, or override owner files.

When a lane reviews proof quality, it may ask for a requirement-to-proof trace: requirement, bug behavior, or acceptance criterion; evidence lane; recorded source; what this proves; what this does not prove; and remaining uncertainty. The trace is review input only. It must not treat generated tests, generated properties, trace tables, screenshots, browser notes, AI critique, external status summaries, or generated reports as complete proof by themselves.

## When To Use Review Lanes

Use a Review Lane when one active bead is complete or nearly complete and the review would benefit from a named specialist lens.

Use the Security Review Lane when the bead touches or may affect:

- authentication, authorization, roles, sessions, or account boundaries
- secrets, credentials, environment values, provider configuration, webhooks, or tokens
- personal data, uploads, files, storage, exports, logs, analytics, or privacy-sensitive records
- payments, billing, abuse prevention, rate limits, admin surfaces, or destructive actions
- dependency, package, supply-chain, or externally sourced code risk

Use the Release / Docs Freshness Review Lane when the bead touches or may affect:

- user-facing behavior, setup, support, docs, onboarding, or troubleshooting
- release-readiness notes, release-candidate evidence, smoke paths, rollback, or blocked escape
- public docs, README guidance, screenshots, examples, prompts, changelog-like notes, or support promises
- deployment, production behavior, external services, migrations, post-release follow-up, or users who need fresh instructions

Use the Dependency Graph Review Lane when the bead touches or may affect:

- `depends_on`, follow-up, transition, blocker, or decomposition relationships
- Work Graph warnings, stale graph evidence, or broad graph-coherence questions
- broad files in play, overlapping owner files, or confusing changed-file scope
- safe sequencing, split decisions, or whether relationship risks should block acceptance
- branch/worktree-isolated teammate work or a `can run in parallel` claim

Do not use a Review Lane as a general brainstorming step, a task planner, a second active bead, a required gate for every task, or a substitute for normal acceptance review.

## Required Inputs

Load only the sources needed for the lane:

- active memory and the active bead during normal Precode work
- primary authority file
- files in play or changed-file summary
- recorded checks and results
- manual verification, when relevant
- Closeout Evidence or current closeout draft
- relevant run contract, release-readiness note, or release-candidate profile if present
- `logs/work-graph.md`, `logs/work-graph.json`, or compiled Work Graph summary when dependency relationships are being reviewed
- relevant PRD, bead, dependency, blocker, follow-up, transition, or team-collaboration references when their `LOAD_WHEN` applies
- relevant owner files, such as `SECURITY.md`, `ACCEPTANCE.md`, `docs/*.md`, or the owning PRD, only when their `LOAD_WHEN` applies

If the active bead, primary authority, recorded evidence, or changed-file summary is missing, stop and ask for the missing source instead of inventing a review.

## Output Contract

Return exactly these fields:

```text
Lane:
Review target:
Authority checked:
Evidence reviewed:
Findings:
Missing proof:
Acceptance questions:
Recommendation: accepted | revise | split | blocked | stop
Approval still required:
Promotion path:
```

Recommendations are advisory only. They do not accept implementation, approve the review decision, approve release, approve security posture, activate a bead, create a follow-up task, update owner files, or mutate anything.

## Security Review Lane

Use this lane to inspect whether the bead's evidence is strong enough for a security-sensitive acceptance conversation.

Focus on:

- changed security-sensitive surfaces
- owner-file requirements from `SECURITY.md`, the primary authority, PRD, or run contract
- sensitive data or secret handling
- auth, permissions, roles, admin, destructive, payment, upload, storage, logging, or external-service risk
- dependency or supply-chain changes
- recorded checks, manual review, and unresolved security uncertainty
- rollback, blocked escape, or user approval needed before sensitive work continues

The Security Review Lane may recommend `accepted`, `revise`, `split`, `blocked`, or `stop` as review input only. It must not claim security certification, compliance approval, legal assurance, vulnerability absence, penetration-test completion, production safety, or security sign-off.

## Release / Docs Freshness Review Lane

Use this lane to inspect whether release-relevant work has fresh user-facing instructions and enough shipping evidence for an acceptance conversation.

Focus on:

- changed user-facing behavior, setup, docs, support, onboarding, or troubleshooting
- recorded checks, smoke path, browser or manual verification, and remaining uncertainty
- docs/support freshness and whether users can still follow current instructions
- release-readiness note or Release Candidate Evidence Profile when relevant
- rollback path, blocked escape, post-release follow-up, and approvals still required
- stale prompt, screenshot, README, guide, or support expectations that could mislead a builder

The Release / Docs Freshness Review Lane may recommend `accepted`, `revise`, `split`, `blocked`, or `stop` as review input only. It must not deploy, approve release, approve rollback, approve merge, mutate dashboards, mutate GitHub, mutate external services, or replace the Release Readiness Protocol.

## Dependency Graph Review Lane

Use this lane to inspect whether the bead's relationship evidence is coherent enough for a review, split, blocked, or stop conversation.

Focus on:

- blocked work, missing dependencies, or non-done dependencies
- duplicate, out-of-order, or ambiguous work relationships
- broad files in play, owner-file overlap, or changed files that make the bead hard to review
- ambiguous follow-up destinations, closeout blockers, or transition proposals
- unsafe parallel assumptions, including `can run in parallel` claims that lack branch/worktree isolation and coordinator approval
- stale generated Work Graph evidence that should be repaired through owner files and regenerated before it is trusted as review input
- recorded checks and missing proof needed to resolve the relationship risk

Generated Work Graph reports are evidence only. If graph output is stale, misleading, or incomplete, repair the Markdown owner files, beads, PRDs, closeout notes, or recorded evidence first, then regenerate the graph. Do not edit generated Work Graph reports as the source of truth.

The Dependency Graph Review Lane may recommend `accepted`, `revise`, `split`, `blocked`, or `stop` as review input only. It must not choose tasks, approve transitions, accept implementation, approve parallel execution, create follow-up tasks, rewrite owner files, run tasks, mutate GitHub, mutate external systems, replace Decomposition Protocol, replace Team Collaboration Protocol, or treat Work Graph reports as authority.

For any lane, `Missing proof` should name the requirement, bug behavior, acceptance criterion, or release risk that lacks a recorded source. Avoid vague findings such as "needs more tests" when the real gap is that no evidence is tied to the claim being accepted.

## Promotion Path

Promote accepted findings only through normal reviewed paths:

- Closeout Evidence
- PRD amendment
- owner-file update
- candidate or approved bead after user review
- release-readiness evidence
- reviewed memory after user review

Do not create follow-up tasks, update owner files, or promote findings automatically from lane output.

## Stop Conditions

Stop if:

- the active bead or primary authority is unclear
- recorded checks or manual verification are missing for the risk being reviewed
- the changed-file summary cannot be inspected
- a sensitive surface appears without an approval gate
- the lane would require secrets, credentials, private data, provider config, dashboard values, or production details
- the answer would certify security, compliance, release readiness, or acceptance
- the answer would treat generated Work Graph reports as authority, proof, task selection, or transition approval
- the answer would approve parallel execution instead of routing through branch/worktree isolation and coordinator review
- findings would need a new PRD, bead, owner-file update, release action, GitHub mutation, external mutation, or destructive command before user review

## Forbidden Actions

Review Lanes must not:

- edit files
- approve PRDs
- activate beads
- approve transitions
- accept implementation
- approve review decisions
- approve release
- approve rollback
- approve merge or migration
- approve security posture
- certify compliance
- create follow-up tasks
- rewrite owner files
- choose tasks
- run tasks from graph output
- approve parallel execution
- run mutating commands
- mutate GitHub
- mutate external systems
- treat Work Graph reports as authority, proof, transition approval, or task selection
- treat generated reports, screenshots, browser notes, GitHub status, or confidence as proof
- create a registry, optional pack, command wrapper, package-manager behavior, release-channel behavior, generated report, checker gate, task-runner system, or persona system
