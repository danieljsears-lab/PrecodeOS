# PrecodeOS -- Release Readiness Protocol
<!-- ANCHOR: release-readiness-protocol -->

> AUTHORITY: User-project release-readiness lane, shipping evidence expectations, release-relevant bead guidance, approval gates, rollback or blocked-escape notes, and post-release review prompts for PrecodeOS.
> NOT_AUTHORITY: Active memory, task selection, bead activation, deployment approval, release approval, provider configuration, dashboard mutation, rollback execution, GitHub mutation, generated progress state, or generated evidence truth.
> LOAD_WHEN: A completed or nearly completed bead may affect users, production, deployment, external services, documentation needed for use, or post-release support.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.4
Last updated: 2026-06-19

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
- accessibility advisory status when the Accessibility Advisor was invoked, an owner file required it, or release confidence depends on it

Use existing Closeout Evidence where possible. Do not duplicate proof in a separate report unless the release-relevant bead needs a concise shipping summary.

## Release Candidate Evidence Profile

Use a Release Candidate Evidence Profile when release-relevant work is nearly ready for a human release decision and the builder needs one compact view of what changed, what is proven, what is still uncertain, and which approvals remain.

The profile is human-authored evidence framing. It is not a generated report, release approval, deployment approval, review acceptance, merge approval, rollback approval, GitHub action, provider action, package-release checkpoint, CLI command, release-channel behavior, or package-manager behavior.

Profile fields:

- candidate label
- release target or environment
- changed surfaces
- affected users or workflows
- recorded checks and results
- smoke path and result
- browser or manual verification status
- docs or support freshness
- rollback path or blocked escape
- known risks and remaining uncertainty
- accessibility advisory status when invoked or required
- explicit approvals still required before release, deployment, promotion, merge, migration, dashboard change, secret change, GitHub mutation, provider mutation, rollback, external mutation, or post-release owner action
- decision state

Decision state must use one of:

- `candidate`: evidence is being assembled and no release decision is ready yet
- `needs evidence`: required checks, smoke path, docs/support freshness, manual/browser verification, rollback, or approval framing is missing
- `blocked`: release-candidate review cannot continue until a named blocker, missing owner action, or unblocker bead is resolved
- `ready for human release decision`: evidence and remaining approvals are clear enough for the user to decide the next release action

`ready for human release decision` is not approval to release. It only means the evidence profile is clear enough for the human to make the release decision explicitly.

Use this copyable profile shape:

```text
Release Candidate Evidence Profile:
- Candidate label:
- Release target or environment:
- Changed surfaces:
- Affected users or workflows:
- Recorded checks and results:
- Smoke path and result:
- Browser or manual verification status:
- Docs or support freshness:
- Rollback path or blocked escape:
- Known risks and remaining uncertainty:
- Accessibility advisory status:
- Approvals still required:
- Decision state: candidate | needs evidence | blocked | ready for human release decision
```

## Verification And Release Evidence Review

Use verification and release evidence review when release confidence depends on proving a specific requirement, behavior, or non-functional expectation.

This review is human-authored traceability. It is not a generated report, release approval, review acceptance, deployment approval, rollback approval, package release management, provider checklist, release-channel behavior, or package-manager behavior.

Release evidence should name:

- requirement or behavior proven
- evidence lane used: `static`, `unit`, `integration`, `browser`, `manual`, or `external`
- recorded check, Closeout Evidence, or manual verification source
- smoke path and result
- docs or support freshness
- rollback path or blocked escape
- approvals still required
- decision state
- remaining uncertainty

Missing traceability means `needs evidence`. It does not approve release, block release by itself, replace review, or make generated checker output proof.

Use this compact shape inside Closeout Evidence, a release-readiness note, or a Release Candidate Evidence Profile when a release-relevant bead needs clearer proof:

```text
Verification and release evidence:
- Requirement or behavior proven:
- Evidence lane:
- Recorded source:
- Smoke path and result:
- Docs or support freshness:
- Rollback path or blocked escape:
- Approvals still required:
- Decision state: candidate | needs evidence | blocked | ready for human release decision
- Remaining uncertainty:
```

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

Accessibility review is optional unless the user invokes the Accessibility Advisor, an owner file requires it, or release review explicitly depends on accessibility confidence. Use the Accessibility Advisor Fit Interview when that choice is unclear. If invoked, include the advisory target, automated check evidence when available, manual review notes, unresolved findings, and acceptance risk in Closeout Evidence or the Release Candidate Evidence Profile. Do not claim legal compliance, certify WCAG/ADA conformance, or treat accessibility notes as release approval.

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

## Release Candidate Prompt

```text
Prepare a Release Candidate Evidence Profile for this release-relevant bead.
Do not deploy, promote, roll back, merge, migrate, change dashboards, change secrets, mutate GitHub resources, mutate external services, approve review, accept implementation, or activate the next bead.
Use the profile fields from the Release Readiness Protocol: candidate label, release target, changed surfaces, affected users or workflows, recorded checks and results, requirement or behavior proven, evidence lane, recorded source, smoke path and result, browser or manual verification status, docs or support freshness, rollback or blocked escape, known risks and remaining uncertainty, approvals still required, and decision state.
Use only one decision state: candidate, needs evidence, blocked, or ready for human release decision.
Make clear that ready for human release decision is not release approval.
```

## Review Prompt

```text
Before I approve release, compare the release-readiness note with Closeout Evidence.
Tell me what evidence is recorded, what remains review input only, what manual or browser verification is missing, what rollback or blocked escape exists, and which release actions still require my explicit approval.
```

## Release Candidate Review Prompt

```text
Review this Release Candidate Evidence Profile against Closeout Evidence and recorded checks.
Tell me what is recorded evidence, what is review input only, what evidence is missing, whether the rollback or blocked escape is specific enough, which approvals are still required, and whether the decision state should be candidate, needs evidence, blocked, or ready for human release decision.
Do not approve release, deploy, promote, roll back, merge, migrate, change dashboards, change secrets, mutate GitHub resources, mutate external services, accept implementation, or activate the next bead.
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
