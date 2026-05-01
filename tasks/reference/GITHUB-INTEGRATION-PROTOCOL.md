# Precode OS -- GitHub Integration Protocol
<!-- ANCHOR: github-integration-protocol -->

> AUTHORITY: GitHub integration rules, read-only audit boundaries, issue and pull request source-intake rules, GitHub Actions validation expectations, and promotion paths for GitHub-derived evidence.
> NOT_AUTHORITY: Active memory, task selection, product decisions, implementation plans, bead state, repository mutation, CI rerun policy, deployment policy, or generated progress state.
> LOAD_WHEN: Configuring GitHub, reviewing GitHub audit findings, importing GitHub issues or pull requests as source evidence, or adding GitHub Actions validation for Precode OS.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-04-26

## Purpose

GitHub can help Precode OS see repository status, CI status, pull request context, and issue context.

GitHub must not become a second operating system. GitHub issues, pull requests, checks, comments, labels, project boards, and Actions are evidence or external status until a user promotes stable conclusions into the correct Precode owner file.

Use `tasks/reference/TOOL-EXECUTION-PROTOCOL.md` before any GitHub tool call that mutates issues, pull requests, labels, branches, checks, comments, workflows, or repository settings.

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

## Audit Path

`scripts/github-audit.py` is a read-only helper for scheduled audits.

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
