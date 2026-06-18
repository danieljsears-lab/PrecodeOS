# PrecodeOS -- Review Lanes Protocol
<!-- ANCHOR: review-lanes-protocol -->

> AUTHORITY: Optional advisory review lane templates for one active bead.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, review acceptance, implementation acceptance, release approval, security certification, compliance approval, generated proof, command approval, follow-up task creation, owner-file rewrite, external mutation, GitHub mutation, package-manager behavior, or a persona system.
> LOAD_WHEN: A user asks for a Security Review Lane, Release / Docs Freshness Review Lane, or Review Lanes review for one active bead.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-18

## Purpose

Review Lanes help a builder ask specialist review questions without managing fake specialist personas.

A lane attaches to one active bead and turns a narrow review concern into evidence, missing proof, acceptance questions, and a recommendation. It does not approve work, create work, replace Review mode, replace Release Readiness, or override owner files.

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
- findings would need a new PRD, bead, owner-file update, release action, GitHub mutation, external mutation, or destructive command before user review

## Forbidden Actions

Review Lanes must not:

- edit files
- approve PRDs
- activate beads
- accept implementation
- approve review decisions
- approve release
- approve rollback
- approve merge or migration
- approve security posture
- certify compliance
- create follow-up tasks
- rewrite owner files
- run mutating commands
- mutate GitHub
- mutate external systems
- treat generated reports, screenshots, browser notes, GitHub status, or confidence as proof
- create a registry, optional pack, command wrapper, package-manager behavior, release-channel behavior, generated report, checker gate, or persona system
