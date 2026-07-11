# PrecodeOS -- External Status Integration Protocol
<!-- ANCHOR: external-status-integration-protocol -->

> AUTHORITY: Provider-neutral external status rules, read-only status row shape, safe health URL boundaries, generated evidence handling, missing-configuration behavior, and promotion paths for external-status findings.
> NOT_AUTHORITY: Active memory, task selection, product decisions, implementation plans, bead state, release approval, deployment approval, merge approval, provider configuration approval, dashboard mutation, external system mutation, or generated progress state.
> LOAD_WHEN: Adding, reviewing, configuring, or interpreting read-only external status checks for GitHub, CI, deployment, uptime, monitoring, dependency advisories, issue trackers, or dashboards.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-07-11

## Purpose

External status can reveal blocked or risky work that lives outside PrecodeOS: repository state, CI, pull requests, deployment status, uptime, monitoring, issue trackers, and advisory sources.

External status is evidence only. It must not choose tasks, approve PRDs, activate beads, accept implementation, approve reviews, approve releases, approve merges, deploy, roll back, mutate dashboards, or replace owner files.

Use `tasks/reference/GITHUB-INTEGRATION-PROTOCOL.md` for GitHub-specific rules. Use `tasks/reference/SCHEDULED-AUDIT-PROTOCOL.md` when external status is collected by scheduled audits. Use `tasks/reference/TOOL-EXECUTION-PROTOCOL.md` before any tool call that could mutate an external system.

## Status Row Shape

Provider-neutral status rows should include:

- `provider`
- `check_name`
- `status`
- `configured`
- `advisory_only`
- `summary`
- `details`
- `warnings`
- `checked_at`
- `source`
- `forbidden_uses`

`status` should be one of `pass`, `warning`, `fail`, `info`, or `not_configured`. Missing tools, missing authentication, missing local configuration, and unsupported providers should normally return `not_configured` or `warning`, not fail the package by default.

## Allowed Read-Only Uses

External status integrations may:

- read local Git metadata
- read GitHub repository, pull request, issue, review, check, and workflow status through read-only commands when configured
- perform safe unauthenticated `GET` checks against explicitly reviewed health URLs in `PROJECT-CONTEXT.md`
- summarize configured-provider absence as `not_configured`
- write generated evidence under `logs/`
- feed scheduled audit reports and release-readiness evidence prompts

## Safe Health URLs

Safe health URLs must be recorded in `PROJECT-CONTEXT.md` before scheduled audits use them.

Health URL checks must:

- use `GET`
- avoid request bodies and custom auth headers
- avoid secrets, credentials, private dashboard URLs, billing pages, customer data, and token-bearing query strings
- report redirects, timeouts, and HTTP errors as evidence only
- stay optional and read-only

Do not store tokens, credentials, cookies, private dashboard values, or environment-specific secrets in `PROJECT-CONTEXT.md` or generated audit output.

## Forbidden Uses

External status integrations must not:

- comment on, edit, label, assign, close, approve, merge, rerun, cancel, push, rebase, or delete GitHub resources
- deploy, promote, roll back, migrate, restart, or mutate provider environments
- mutate dashboards, monitoring configuration, issue trackers, labels, project boards, releases, or workflow settings
- store secrets, tokens, credentials, cookies, dashboard values, billing values, or private health endpoints
- choose tasks, rank candidates, approve PRDs, activate beads, accept implementation, approve reviews, approve release, approve merge, approve transition, or create follow-up work by itself

## Promotion Path

External status findings become action only after review:

| Finding type | Promotion destination |
|---|---|
| Product or technical decision | `DECISIONS.md` |
| Architecture, API, security, deployment, or integration fact | Owning authority file such as `PROJECT-CONTEXT.md`, `ARCHITECTURE.md`, `API.md`, or `SECURITY.md` |
| Follow-up work | Proposed or approved bead |
| Release-readiness concern | Release Candidate Evidence Profile or closeout evidence |
| Repeated process lesson | Relevant protocol or adapter |
| Maintainer package change | Maintainer roadmap, changelog, or package owner file after explicit maintainer review |

Generated status rows and scheduled audit summaries are evidence only. They do not write owner files, approve external mutation, or replace human review.
