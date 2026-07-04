# PrecodeOS -- Small Team Collaboration Lane
<!-- ANCHOR: team-collaboration-protocol -->

> AUTHORITY: Small Team Collaboration Lane invocation, team authority boundaries, branch/worktree-isolated parallel bead guidance, teammate handoff, review, merge, and re-entry rules for PrecodeOS.
> NOT_AUTHORITY: Active memory expansion, product decision ownership by teammates, task selection, automatic bead activation, GitHub mutation approval, merge approval, deployment approval, generated progress state, or module/pack/runtime-toggle behavior.
> LOAD_WHEN: A builder says a small team is working on the same product build, asks for Small Team Collaboration Lane, wants 2-5 people to coordinate Precode work, or needs branch/worktree-isolated parallel bead guidance.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.2.2
Last updated: 2026-06-23

## Purpose

Small Team Collaboration Lane helps 2-5 people work on the same product build without turning Precode into a project-management system or weakening the one-active-bead kernel.

The lane is built into PrecodeOS, but it is not default-active and not a separate module. It is invoked explicitly, recorded in shared repo authority, and confirmed by each teammate in their own branch or worktree context.

Active memory remains exactly:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

## Invocation Model

The coordinator invokes the lane first:

```text
Use the Small Team Collaboration Lane.

We have [2-5] people working on this product. Help us define the coordinator, product decision owner, branch or worktree rules, candidate parallel beads, review gates, merge/re-entry rules, and forbidden actions before anyone edits.

Do not activate beads, merge, push, deploy, mutate GitHub, or change external systems.
```

The first output should classify:

- team members and roles
- decision owner or coordinator
- repo topology and branch/worktree convention
- current authority files that must remain source of truth
- candidate beads that may run in parallel
- integration owner and review path
- merge, deploy, external mutation, and sensitive-surface approval gates
- stop conditions

The coordinator records accepted team agreement in shared repo authority such as `PROJECT-CONTEXT.md`, `DECISIONS.md`, a PRD, or another owner file. The conversational lane output is evidence only until promoted.

Each teammate must confirm the lane from repo state before editing:

```text
This repo is using the Small Team Collaboration Lane.

Load active memory, the team coordination notes, and the bead assigned to this branch or worktree. Confirm my role, branch/worktree, primary authority, files in play, checks, stop conditions, evidence I must return, and what requires coordinator approval before editing.
```

## Team Roles

Use only the roles needed for the current team:

| Role | Owns | Must not own |
|---|---|---|
| Coordinator | Team agreement, integration order, review routing, merge/re-entry decisions, and approval questions. | Product truth by implication, unless also named as product decision owner. |
| Product decision owner | Product direction, PRD approval, non-goals, scope tradeoffs, and acceptance meaning. | Silent task activation, merge approval without evidence, or external mutation without gates. |
| Contributor | One branch/worktree-scoped bead or source/evidence contribution. | Widening scope, approving review, merging, deploying, or rewriting owner files outside the assigned scope. |
| Reviewer | Evidence review, risks, missing proof, and recommendation. | Acceptance, merge, transition, release, or product approval unless explicitly authorized by the coordinator and owner files. |

If roles are ambiguous, stop before parallel work starts.

## Parallel Bead Rule

True parallel work requires isolation.

Allowed v1 shape:

- one branch or worktree per contributor bead
- one active bead per checkout
- one primary authority per bead
- disjoint or explicitly conflict-reviewed files in play
- recorded checks and manual verification per contributor bead
- coordinator review before merge or owner-file promotion

Forbidden v1 shape:

- multiple `in_progress` beads in one checkout
- multiple teammates editing the same active memory set at the same time
- GitHub Issues, PRs, project boards, or comments choosing work
- teammate notes or generated handoff packets becoming authority
- merge, deploy, release, or external mutation by lane output alone

`can run in parallel` means "can run in a branch/worktree-isolated teammate context after approval," not "activate multiple beads in the same Precode state."

## Review And Merge Evidence

Before a contributor branch is merged or re-entered into the integration branch, the contributor should provide:

- assigned bead and branch/worktree
- human contributor, contributor role, agent/tool surface, attribution reviewer, and attribution uncertainty when known
- primary authority and files changed
- checks run and results
- manual verification, if needed
- screenshots or external status, if relevant
- product, architecture, API, data, security, or acceptance owner-file impacts
- conflicts with current integration state
- open questions and follow-up bead candidates
- forbidden actions not taken

The coordinator or integration owner decides whether findings are promoted into owner files, accepted into the integration branch, split into follow-up beads, or blocked.

Review evidence is not acceptance. Merge readiness is not product approval.

Build attribution evidence is not blame or scoring. `scripts/build-attribution-ledger.py` may summarize who built what from bead closeout and supporting hints, but teammate accountability remains subordinate to the assigned bead, coordinator review, and accepted closeout evidence.

Review and merge evidence must remain subordinate to the assigned bead, primary authority, recorded checks, manual verification, and coordinator review.

## V2 Read-Only Preview

`scripts/team-collaboration-check.py` provides a read-only Small Team Collaboration Lane preview. It is generated evidence only and must not choose work, approve merge, mutate GitHub, update owner files, or replace coordinator review.

Default local preview reports:

- current branch and worktree
- detected or requested integration branch
- active bead and one-active-bead-per-checkout status
- active bead primary authority and files in play
- local changed paths and branch comparison paths when available
- owner-file impact candidates
- overlap with active bead scope
- stale branch or re-entry risks
- delegation re-entry fields for teammate, delegated-agent, or cloud-agent return
- merge/re-entry review packet fields
- teammate assignment packet fields
- forbidden uses and generated-report warning

Optional GitHub preview:

```text
python3 scripts/team-collaboration-check.py --github
```

This may read branch, pull request, review, check, and workflow status through `gh` when available and authenticated. Missing `gh`, missing authentication, missing upstream/default branch, network failure, unavailable comparison base, or inaccessible GitHub status must be reported as `not_configured` or `warning`, not silently guessed.

To compare against a specific integration branch:

```text
python3 scripts/team-collaboration-check.py --integration-branch <branch>
```

The script must not create branches, create worktrees, push, pull, rebase, merge, create pull requests, approve pull requests, comment, label, assign, rerun workflows, deploy, release, or mutate external systems.

## Team Merge And Re-entry Review Pack

The coordinator's merge/re-entry review should include:

- assigned bead and branch/worktree
- primary authority and files changed
- checks run and results
- manual verification, if needed
- owner-file impacts
- conflicts with the integration branch
- stale evidence or stale branch signals
- delegated-agent or cloud-agent return evidence: scope returned, changed files, checks and results, manual verification, approval still required, unresolved risks, external status evidence, and forbidden actions not taken
- open questions and follow-up bead candidates
- forbidden actions not taken

The preview can help collect these fields, but the coordinator still decides whether to promote findings into owner files, ask for more proof, split follow-up work, block, or approve a separate merge action.

## Team Owner-File Conflict Preview

Owner-file impact candidates include active memory, PRDs, reference protocols, bead files, public docs, and common product authority files such as `PROJECT-CONTEXT.md`, `FEATURES.md`, `PRODUCT.md`, `ARCHITECTURE.md`, `API.md`, `DATA-MODELS.md`, and `SECURITY.md`.

If two teammates touch the same owner file family, the coordinator must review the conflict before merge or re-entry. A preview warning is not proof of a conflict, and a clean preview is not proof that merge is safe.

## GitHub And External Status

GitHub branches, pull requests, reviews, checks, labels, comments, and project-board status are external evidence.

GitHub evidence must not choose tasks.
Cloud-agent, CI, pull request, and review summaries follow the same rule. They may populate delegated re-entry evidence fields, but they do not approve continue, implementation acceptance, merge, release, transition, GitHub mutation, external mutation, or owner-file promotion.

They may help answer:

- which contributor branch exists
- whether checks passed
- whether a review found issues
- whether a PR conflicts with current integration state

They must not:

- choose tasks
- approve PRDs
- activate beads
- accept review
- approve merge
- deploy
- mutate issues, PRs, labels, comments, workflows, branches, releases, or project boards without explicit user approval

Use `tasks/reference/GITHUB-INTEGRATION-PROTOCOL.md` and `tasks/reference/TOOL-EXECUTION-PROTOCOL.md` before GitHub mutation.

## Re-entry Rules

When a teammate returns after another contributor or coordinator changed integration state, re-entry starts by checking:

- current branch/worktree
- active bead in that checkout
- current integration branch state, if available
- whether the assigned bead still has one outcome and one primary authority
- whether files in play conflict with merged work
- whether checks or manual verification are stale
- whether any teammate AFK or delegated-agent work changed files beyond the assigned bead
- whether recorded evidence is enough for coordinator review without relying on chat history
- whether cloud-agent or PR status is only evidence and still leaves explicit approval gates unresolved
- whether the next action is continue, rebase/update, review, split, block, or handoff

If re-entry changes the product decision, PRD, owner-file scope, files in play, or verification strategy, stop and ask the coordinator before editing.

Small-team re-entry is not the same as solo `afk_candidate` work. Team parallelism always requires branch/worktree isolation, coordinator review, and merge/re-entry evidence; AFK metadata on one bead does not approve multiple active beads or merge work back into the integration branch.

## Stop Conditions

Stop before work continues when:

- no coordinator or product decision owner is named
- the team agreement is not recorded in a shared owner file
- a teammate cannot name their branch/worktree, bead, primary authority, files in play, or checks
- two contributors need the same files and no conflict plan exists
- a PR or issue is being treated as authority
- AFK or delegated-agent output is being treated as acceptance, merge approval, or permission to widen the assigned bead
- a merge, deploy, release, external mutation, or sensitive action is requested without explicit approval
- generated reports, teammate notes, or handoff packets are being used as instructions
- the work requires multiple active beads in one checkout

## Promotion Path

Team findings become durable only through normal Precode promotion:

| Finding | Promotion destination |
|---|---|
| Team coordination decision | `PROJECT-CONTEXT.md` or `DECISIONS.md` |
| Product requirement or scope change | PRD shard and `FEATURES.md` after approval |
| Architecture, API, data, security, or acceptance fact | Owning authority file |
| Contributor work | Branch/worktree bead evidence, then coordinator review |
| Follow-up work | Candidate or approved bead |
| GitHub or teammate observation | Source evidence until reviewed |

Do not create optional-pack, registry, module, package-manager, installer, runtime-toggle, or project-management semantics for this lane.
