# PrecodeOS -- Release Readiness Protocol
<!-- ANCHOR: release-readiness-protocol -->

> AUTHORITY: User-project release-readiness lane, shipping evidence expectations, release-relevant bead guidance, approval gates, rollback or blocked-escape notes, and post-release review prompts for PrecodeOS.
> NOT_AUTHORITY: Active memory, task selection, bead activation, deployment approval, release approval, provider configuration, dashboard mutation, rollback execution, GitHub mutation, generated progress state, or generated evidence truth.
> LOAD_WHEN: A completed or nearly completed bead may affect users, production, deployment, external services, documentation needed for use, or post-release support.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.1
Last updated: 2026-06-14

## Purpose

Release readiness helps a builder answer one question before user-facing risk changes:

```text
Is this change evidenced, reversible or safely escapable, and explicitly approved enough to ship?
```

This protocol prepares evidence and approval questions. It does not deploy, promote, roll back, merge, change dashboards, change secrets, mutate external systems, approve a bead, activate a next bead, or replace the user's release decision.

Use `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md` for verification tiers and sensitive-surface gates. Use `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md` for closeout, review, and transition rules. Use `tasks/reference/GITHUB-INTEGRATION-PROTOCOL.md` for GitHub status or package checkpoint boundaries.

Active memory remains exactly:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

## When A Bead Is Release-Relevant

A normal bead becomes release-relevant when its output could affect:

- deployed or production behavior
- user-visible flows, pages, forms, emails, exports, or notifications
- authentication, authorization, payments, billing, personal data, uploads, storage, or security
- database schema, migrations, background jobs, queues, webhooks, or integrations
- dashboards, environment variables, secrets, provider settings, DNS, or infrastructure
- public docs, setup instructions, support expectations, or user-facing release notes
- rollback, blocked escape, monitoring, support, or post-release learning

Tiny local-only docs or code cleanup can skip this lane unless it changes user-facing behavior, setup, support, release, validation, or sensitive surfaces.

Stable-fix eligibility does not skip this lane. If `scripts/next-step.py --json` classifies work as `broader_change` because it is release-relevant or user-facing, prepare release readiness even when the code or docs edit is small. A stable fix can stay in the current bead only when it does not affect release behavior, setup/support expectations, sensitive surfaces, or user-facing evidence needs.

## Release Readiness Notes

Before release approval, prepare a short release-readiness note with:

- changed behavior
- affected users or workflows
- release target or environment
- recorded checks and their results
- smoke test path and result
- browser or manual verification, when relevant
- external status evidence, when relevant and read-only
- docs freshness or user-facing instruction changes
- rollback path or blocked escape
- known risks and remaining uncertainty
- post-release follow-up or observation plan
- explicit approval still needed before deployment, promotion, rollback, merge, migration, dashboard change, secret change, or external mutation

Use existing Closeout Evidence where possible. Do not duplicate proof in a separate report unless the release-relevant bead needs a concise shipping summary.

## Smoke Evidence

Smoke evidence is the smallest practical proof that the release target still works after the change.

Examples:

- open the changed page or flow and complete the shortest meaningful path
- run the narrow command or health check that proves the release target starts
- confirm a form, API route, integration callback, or generated artifact behaves as expected
- check that public docs needed by users are current

Smoke evidence is not acceptance by itself. It supports the review decision and release approval.

## Browser And Manual Verification

Use browser evidence for user-facing UI or flows. Use manual verification when a human judgment, external UI, credentialed dashboard, or production-only behavior is the acceptance oracle.

Manual verification should follow the Verification Guardrail Protocol format:

```text
Manual verification:
- Who checked:
- What was checked:
- Environment:
- Result:
- Remaining uncertainty:
```

Screenshots, browser notes, generated tests, GitHub status, and dashboard observations are review input until recorded in Closeout Evidence or explicitly accepted by the user.

## Rollback Or Blocked Escape

Every release-relevant bead should name one of:

- rollback path
- blocked escape path
- narrower unblocker bead
- manual owner action needed
- reason rollback is not applicable

Do not accept vague language such as "we can revert if needed" for high-risk release work.

## Forbidden Actions Without Explicit Approval

An agent must not use this protocol to:

- deploy, promote, roll back, or merge
- run migrations or destructive commands
- change dashboards, provider settings, DNS, secrets, credentials, environment variables, billing, auth, payments, storage, or private data
- create, edit, close, label, assign, comment on, approve, merge, or rerun GitHub resources
- treat generated reports, screenshots, browser notes, GitHub status, or release-readiness notes as release approval
- approve a review decision, activate the next bead, or update active memory
- imply package-manager, update-channel, release-channel, CLI, or provider-specific automation behavior

If approval is granted, record the exact allowed action, expected effect, evidence to capture, and rollback or blocked escape before mutation.

## Builder Prompt

```text
Prepare release readiness for this bead.
Do not deploy, promote, roll back, merge, migrate, change dashboards, change secrets, mutate external services, or activate the next bead.
Show changed behavior, affected users, release target, recorded checks, smoke test path, browser or manual verification needed, docs freshness, rollback or blocked escape, known uncertainty, post-release follow-up, and exactly what I must approve before any release action.
```

## Review Prompt

```text
Before I approve release, compare the release-readiness note with Closeout Evidence.
Tell me what evidence is recorded, what remains review input only, what manual or browser verification is missing, what rollback or blocked escape exists, and which release actions still require my explicit approval.
```

## Post-Release Review

After a user-approved release action, record:

- what was released or changed
- who approved the release action
- when and where it happened
- smoke check result after release
- user, support, monitoring, or dashboard observations, if available
- follow-up bead, memory proposal, PRD amendment, or owner-file update needed

Post-release review is evidence. It does not automatically choose the next task.
