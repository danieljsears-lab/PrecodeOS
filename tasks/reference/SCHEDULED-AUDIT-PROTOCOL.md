# PrecodeOS -- Scheduled Audit Protocol
<!-- ANCHOR: scheduled-audit-protocol -->

> AUTHORITY: Scheduled audit rules, allowed read-only checks, forbidden automation, generated audit output, external status audit boundaries, scheduler examples, secret-handling rules, and finding-promotion paths.
> NOT_AUTHORITY: Active memory, task selection, product decisions, implementation plans, external system mutation, deployment policy, or generated progress state.
> LOAD_WHEN: Adding, reviewing, running, or configuring scheduled audits for PrecodeOS.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.2
Last updated: 2026-06-04

## Purpose

Scheduled audits help a builder notice quiet drift without letting automation move the project forward.

They may refresh generated reports and surface warnings. They must not edit active memory, change bead state, approve transitions, create work, merge pull requests, deploy, or mutate external systems.

## Allowed Scheduled Actions

Scheduled audits may:

- run memory validation
- refresh `OS-HEALTH.md` and `logs/os-health.json`
- refresh `logs/learning-diary.md` without appending a fake session
- dry-run spend telemetry import
- read existing logs and generated sidecars
- read local Git metadata
- read external system status when configured through read-only tools
- write generated audit reports under `logs/`

## Forbidden Scheduled Actions

Scheduled audits must not:

- edit `AGENT.md`, `DECISIONS.md`, or `tasks/todo.md`
- change bead frontmatter or bead state
- call `scripts/session-start.sh`, `scripts/session-close.sh`, or `scripts/bead-transition.py --approve`
- create PRDs, beads, requirements, issues, comments, labels, or decisions
- push, merge, deploy, rollback, migrate, rerun CI, or mutate external systems
- store secrets, tokens, credentials, dashboard values, or private raw transcripts
- treat generated reports as active memory

## Built-In Local Audits

Run these by default:

- Health Refresh Audit: regenerate OS health reports.
- Memory Validation Audit: run `bash scripts/validate-memory.sh`.
- Stale Bead Audit: flag active work with no recent evidence.
- Closeout Completeness Audit: flag missing checks, manual verification, review decision, blocked escape, or next-bead safety.
- Generated Reports Demotion Audit: confirm generated files remain demoted.
- Learning Diary Refresh Audit: refresh the learner-facing diary without appending a session.
- Spend Telemetry Audit: dry-run spend import and summarize known or unknown spend.
- Blocked Work Audit: flag blocked beads without clear escape paths.
- Intent Orchestration Audit: flag unclear intent promotion, traceability gaps, changed or blocked intent, and follow-up work without an owner.
- Tool Execution Audit: flag approval gaps, destructive tool calls, missing failure categories, stale command evidence, or tool-use logs that should not be treated as verification.
- Workflow Planning Audit: flag wrong workflow fit, PRD approval gaps, missing bead proposals, mixed planning and implementation, blocked work without an unblocker path, backlog-like active fields, or generated reports driving workflow selection.
- Long-Horizon Planning Audit: flag future work leaking into active memory, approved PRDs without bead proposals, blocked or deferred work without revisit paths, dependency gaps, or follow-up candidates without destinations.
- Completion And Handoff Audit: flag incomplete closeout evidence, vague manual verification, missing review decisions, unsafe next-bead references, stale session close evidence for close-oriented bead states, or incomplete handoff Context Packs; report an open `in_progress` session as detail rather than a warning.

## Built-In External Audits

External audits are optional and read-only.

Run only when matching local tooling and configuration are present. Otherwise, report `not_configured`.

Common audits:

- GitHub repository status through authenticated `gh`
- CI/check status for the current branch or PR
- deployment status for configured providers such as Vercel, Netlify, or a generic health URL
- linked issue status for GitHub, Linear, or Jira references
- dependency or security advisory status where a read-only source is available
- monitoring or observability status when configured
- uptime checks for explicitly configured safe `GET` health URLs
- external dashboard setup status documented in `PROJECT-CONTEXT.md`

## Generated Outputs

Write:

- `logs/scheduled-audit.json`
- `logs/scheduled-audit.md`

Both are generated evidence and must not drive active task selection.

The markdown report must include:

- authority contract
- `CLASS: generated`
- timestamp
- local audit results
- external audit results
- warnings and missing configuration
- human review prompts, not automatic actions

## Scheduler Examples

Cron example:

```cron
0 9 * * * cd /path/to/repo && bash scripts/scheduled-audit.sh
```

Launchd and GitHub Actions may call the same command. They should not pass credentials or perform state-changing steps.

## Promotion Path

Audit findings become action only after user review.

- Product or technical decisions -> `DECISIONS.md`
- Follow-up work -> a proposed bead
- Verification gaps -> bead Closeout Evidence or a follow-up check
- External setup blockers -> manual-testing or needs-info state after user approval
- Security risks -> `SECURITY.md` or a security bead

Do not promote findings directly from the generated audit report without user approval.

## GitHub Support

Use `tasks/reference/GITHUB-INTEGRATION-PROTOCOL.md` for GitHub-specific setup, audit, source-intake, and GitHub Actions rules.

Scheduled audits may call `python3 scripts/github-audit.py`. That helper is read-only and writes no authority files.
