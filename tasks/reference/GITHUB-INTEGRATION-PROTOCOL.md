# PrecodeOS -- GitHub Integration Protocol
<!-- ANCHOR: github-integration-protocol -->

> AUTHORITY: GitHub integration rules, read-only audit boundaries, issue and pull request source-intake rules, GitHub Actions validation expectations, and promotion paths for GitHub-derived evidence.
> NOT_AUTHORITY: Active memory, task selection, product decisions, implementation plans, bead state, repository mutation, CI rerun policy, deployment policy, or generated progress state.
> LOAD_WHEN: Configuring GitHub, reviewing GitHub audit findings, importing GitHub issues or pull requests as source evidence, or adding GitHub Actions validation for PrecodeOS.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.8
Last updated: 2026-07-11

## Purpose

GitHub can help PrecodeOS see repository status, CI status, pull request context, and issue context.

GitHub must not become a second operating system. GitHub issues, pull requests, checks, comments, labels, project boards, and Actions are evidence or external status until a user promotes stable conclusions into the correct Precode owner file.

Use `tasks/reference/EXTERNAL-STATUS-INTEGRATION-PROTOCOL.md` for provider-neutral external status row shape, safe health URL rules, missing-configuration behavior, and promotion paths across non-GitHub providers.

Use `tasks/reference/TOOL-EXECUTION-PROTOCOL.md` before any GitHub tool call that mutates issues, pull requests, labels, branches, checks, comments, workflows, or repository settings.

Use `tasks/reference/TEAM-COLLABORATION-PROTOCOL.md` when GitHub branches, pull requests, reviews, or checks are used to coordinate a small team working on one product build.

Active memory remains exactly:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

## Allowed Read-Only Uses

Precode GitHub tooling may:

- read local git metadata
- read repository, branch, pull request, issue, and check status through `gh`
- read workflow status and recent run outcomes
- summarize GitHub issues or pull requests as source-intake evidence
- write generated reports under `logs/`
- run Precode validation in GitHub Actions

## Forbidden Uses Without Explicit Human Action

Precode GitHub tooling must not:

- push, merge, rebase, or delete branches
- create, edit, close, label, assign, or comment on issues or pull requests
- rerun workflows or cancel workflow runs
- approve pull requests or request reviews
- deploy, promote, rollback, or mutate environments
- store tokens, credentials, secrets, or dashboard values
- change Precode active memory, bead state, PRDs, decisions, or implementation plans from GitHub findings alone

## Maintainer Workflow

For PrecodeOS itself, GitHub is primarily a public trust and release-evidence layer, then a distribution layer. It is not the source of project authority.

Use the hybrid maintainer workflow while Dan Sears / Recode remains the only maintainer:

- use branches and pull requests for package-facing or trust-affecting changes
- allow direct-to-main commits only for tiny corrections that do not change public meaning
- keep public GitHub Issues limited to feedback and package-bug intake unless the maintainer explicitly changes the issue-tracker policy
- use GitHub Releases for public package checkpoints
- keep broader contributor collaboration workflow design, project boards, and GitHub mutation automation out of scope until promoted into approved work

Create a branch and pull request for changes touching active memory, package authority, public docs, setup, bootstrap, install, update, generated-output policy, validation, release, public positioning, GitHub Actions, scripts, hooks, workflow semantics, beginner-facing safety language, or package boundaries.

Recommended branch pattern:

```text
codex/<short-change-name>
```

Direct-to-main is acceptable only when all are true:

- the change is tiny
- the change does not alter public meaning
- the change does not affect install, setup, release, or validation behavior
- the change does not touch active memory or core workflow semantics
- the change would not confuse a future adopter if shipped immediately

Examples include typo fixes, broken internal link fixes, formatting cleanup, private-local note updates, and non-semantic metadata corrections.

## Collaboration Hub Intake Path

Public GitHub Issues are a narrow intake surface for PrecodeOS feedback and package bugs.

Allowed issue intake:

- adoption friction
- confusing docs
- setup friction
- workflow questions
- package bugs in docs, scripts, protocols, generated-surface expectations, setup/copy helpers, CI, or GitHub helper behavior

Recommended issue labels are evidence labels only:

- `feedback`
- `bug`
- `source-intake`
- `docs`
- `scripts`
- `protocol`
- `setup`
- `ci`

Labels do not choose work, approve priority, approve PRDs, activate beads, accept implementation, approve merge, approve release, or grant contributor rights.

Issue templates should ask for:

- the affected package surface or feedback type
- current behavior or friction
- expected behavior
- reproduction steps or context
- checks tried, when relevant
- safe public evidence or examples
- confirmation that secrets, tokens, credentials, private dashboard values, customer records, and sensitive personal data were removed

Blank issues should stay disabled for the first Collaboration Hub slice. Security reports should route through `SECURITY.md`, not public issue templates.

GitHub Issues, comments, labels, pull requests, reviews, checks, and project boards are source evidence until reviewed. Promote stable conclusions through the Local Source Intake Protocol into PRDs, `FEATURES.md`, `DECISIONS.md`, architecture/security/API/schema docs, package docs, protocols, or candidate beads.

Project boards are not active project-management authority by default. A board may be used only as external evidence after the maintainer explicitly defines a reviewed workflow. Board columns, cards, and statuses must not choose tasks, approve roadmap direction, activate beads, approve merge, approve package release, or replace owner files.

Creating, editing, labeling, assigning, commenting on, closing, transferring, pinning, or locking issues; changing issue templates or repository settings; creating labels; adding project boards; or changing board status is GitHub mutation. Use `tasks/reference/TOOL-EXECUTION-PROTOCOL.md` and require explicit maintainer approval before any such action.

## Audit Path

`scripts/github-audit.py` is a read-only GitHub-specific helper for scheduled audits and compatibility with existing command lists. `scripts/external-status.py` is the provider-neutral external status surface and may include GitHub rows using the same read-only boundaries.

It should report:

- current branch
- remote and default branch when discoverable
- local working tree drift
- local branch ahead/behind state when an upstream exists
- open pull request for the current branch
- pull request review and check status when available
- latest workflow run for the current branch
- open pull request count
- authentication, tooling, or configuration gaps

The audit output is generated evidence. Findings become work only when a user promotes them into the owning Precode file or approves a follow-up bead.

## Small Team Status Path

For Small Team Collaboration Lane, GitHub can expose branch, pull request, review, and check status as team evidence.

GitHub status may help a coordinator see:

- contributor branches and pull requests
- check results
- review comments or unresolved findings
- merge conflicts or stale branches when available
- likely owner-file impacts from a pull request summary

GitHub status must not choose tasks, approve PRDs, activate beads, accept implementation, approve merge, approve release, or replace coordinator review. A contributor PR is source evidence until reviewed against the assigned bead, primary authority, recorded checks, manual verification, and team agreement.

GitHub author, reviewer, assignee, branch, pull request, and check-run data may support Build Attribution Ledger review, but it remains external evidence until reviewed into bead Closeout Evidence. It must not assign blame, score contributors, accept implementation, approve merge, or replace coordinator review.

GitHub evidence must not choose tasks or become GitHub mutation approval.

Do not create, edit, close, label, assign, comment on, approve, merge, rerun, cancel, push, rebase, or delete GitHub resources without explicit user approval and an active bead that allows the exact action.

`scripts/team-collaboration-check.py --github` is the read-only aggregation path for team GitHub evidence. It may report repository metadata, current branch pull requests, open pull requests, recent workflow runs, review decisions, merge-state labels, and check rollups when `gh` is available and authenticated.

The output is generated evidence only. Missing `gh`, missing authentication, missing branch/upstream configuration, inaccessible PRs, unavailable checks, or network/API errors must be reported as `not_configured` or `warning`. The script must not silently infer GitHub state, and it must not mutate issues, pull requests, labels, comments, workflows, branches, releases, or project boards.

## Source Intake Path

`scripts/import-github-sources.py` may read an issue, pull request, or local GitHub JSON export and produce a short generated source summary.

The summary may include:

- source type and URL
- title, state, labels, author, and dates
- short body summary
- short comments summary
- acceptance hints
- open questions
- candidate requirements
- candidate bead notes
- likely authority files affected

The output is not a PRD, bead, or decision. Use the Local Source Intake Protocol to promote reviewed conclusions into PRDs, `FEATURES.md`, `DECISIONS.md`, architecture/security/API/schema docs, or beads.

## GitHub Actions Path

GitHub Actions may run Precode validation, but should stay read-only.

Recommended first workflow:

- run `bash scripts/validate-memory.sh` on pushes and pull requests
- optionally run dry-run helpers that do not mutate Precode state
- avoid commands that update bead closeout, approve transitions, write comments, create issues, rerun CI, deploy, or push commits

## Release Checkpoint Path

Use GitHub Releases for public checkpoints after a package baseline or release candidate is ready.

This path is for PrecodeOS package checkpoints. User-project shipping readiness belongs to `tasks/reference/RELEASE-READINESS-PROTOCOL.md` and does not imply GitHub issue, pull request, release, workflow, deployment, or environment mutation.

Each release should include:

- a version tag, such as `v0.1.1`
- concise release notes
- validation evidence
- known risks or remaining uncertainty
- install or update cautions

Release notes should answer what changed, who should care, what checks passed, what remains experimental, and whether the release is install-ready, preview-only, or maintainer-only.

Do not imply package-manager, CLI installer, auto-update, deployment, or release-channel semantics unless those capabilities exist in approved PrecodeOS package work.

## Setup Checklist

Document GitHub configuration in `PROJECT-CONTEXT.md`:

- repository URL
- default branch
- pull request branch naming convention
- CI provider and primary workflow names
- issue tracker mode
- linked project board, if any
- safe read-only status checks

Do not document secrets, tokens, credentials, billing values, or private dashboard settings.
