# PrecodeOS -- Review Lanes Protocol
<!-- ANCHOR: review-lanes-protocol -->

> AUTHORITY: Optional advisory review lane templates for one active bead, one draft PRD, or one bounded package documentation/reference surface.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, transition approval, review acceptance, implementation acceptance, release approval, security certification, compliance approval, generated proof, Work Graph authority, command approval, parallel execution approval, follow-up task creation, owner-file rewrite, external mutation, GitHub mutation, package-manager behavior, task-runner behavior, or a persona system.
> LOAD_WHEN: A user asks for a Security Review Lane, Release / Docs Freshness Review Lane, Dependency Graph Review Lane, Engineering Quality Review Lane, PRD Quality Review Lane, Cross-Reference / Staleness Review Lane, or Review Lanes review for one active bead, one draft PRD, or one bounded package documentation/reference surface.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.6
Last updated: 2026-07-10

## Purpose

Review Lanes help a builder ask specialist review questions without managing fake specialist personas.

A lane attaches to one active bead, one draft PRD, or one bounded package documentation/reference surface and turns a narrow review concern into evidence, missing proof, acceptance questions, and a recommendation. It does not approve work, approve PRDs, create work, replace Review mode, replace Release Readiness, replace Work Graph evidence, replace Requirements Gap And Conflict Review, or override owner files.

When a lane reviews proof quality, it may ask for a requirement-to-proof trace: requirement, bug behavior, or acceptance criterion; evidence lane; recorded source; what this proves; what this does not prove; and remaining uncertainty. The trace is review input only. It must not treat generated tests, generated properties, trace tables, screenshots, browser notes, AI critique, external status summaries, or generated reports as complete proof by themselves.

## When To Use Review Lanes

Use a Review Lane when one active bead is complete or nearly complete and the review would benefit from a named specialist lens, when one draft PRD needs a named pre-approval product-quality lens, or when a bounded package documentation/reference surface needs a named cross-reference and freshness review.

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

Use the Engineering Quality Review Lane when the active bead is complete or nearly complete and the user wants to check whether completed work respected the Engineering Quality floor:

- scope discipline and whether the work stayed inside the active bead, files in play, and primary authority
- simplest acceptable implementation shape, avoiding needless abstraction or broad rewrites
- owner-file, boundary, configuration, dependency, and sensitive-surface handling
- proof quality, recorded checks, manual verification, and remaining uncertainty
- stop-condition observance, approval-gate observance, and whether higher-risk work should have routed to Architecture Shaping, System Design Pattern, Verification Guardrail, Tool Execution, Security Review, Release / Docs Freshness, or Dependency Graph Review

Use the PRD Quality Review Lane when the draft PRD needs pre-approval review of:

- user problem clarity, before/after moment, strategy fit, non-goals, or assumptions
- stale or conflicting source inputs that could distort the product direction
- acceptance quality, requirement-to-proof readiness, or unclear proof expectations
- unresolved open questions, handoff readiness, or smallest first slice
- whether PRD approval review should proceed, pause, split, or return to product-definition work

Use the Cross-Reference / Staleness Review Lane when a bounded package documentation/reference surface needs review of:

- stale, deleted, renamed, or superseded file references, alias names, prompt names, or owner pointers
- missing links, missing backlinks, missing owner pointers, or stale generated-surface pointers that could misroute a builder or agent
- duplicate concept labels or contradictory guidance across public docs and reference protocols
- public/private boundary drift, especially public package guidance that appears to depend on maintainer-only material
- generated reading surfaces that may need refresh from Markdown authority instead of hand edits

For v1, run this lane over a small named file family such as `docs/*.md` and `tasks/reference/*.md`. Treat semantic drift, duplicate concepts, and contradiction risk as manual review prompts that require current owner-file comparison; do not claim a generated stale-fact decision as authority.

`scripts/prd-handoff-readiness.py --prd <path> --target review` may be used as PRD-review evidence when handoff readiness is the narrow question. Treat the packet as cited generated evidence only. It can inform findings, missing proof, acceptance questions, and recommendation, but it does not approve the PRD, create tasks, activate beads, accept implementation, mutate external tools, automate exports, create MCP behavior, create registries, or replace the Markdown PRD.

Do not use a Review Lane as a general brainstorming step, a task planner, a second active bead, a required gate for every task, a substitute for normal acceptance review, a code-quality score, or a substitute for human PRD approval.

## Required Inputs

Load only the sources needed for the lane:

- active memory and the active bead during normal Precode work
- the draft PRD when PRD quality is being reviewed
- primary authority file
- files in play or changed-file summary
- recorded checks and results
- manual verification, when relevant
- Closeout Evidence or current closeout draft
- relevant run contract, release-readiness note, or release-candidate profile if present
- `logs/work-graph.md`, `logs/work-graph.json`, or compiled Work Graph summary when dependency relationships are being reviewed
- relevant PRD, bead, dependency, blocker, follow-up, transition, or team-collaboration references when their `LOAD_WHEN` applies
- relevant owner files, such as `SECURITY.md`, `ACCEPTANCE.md`, `docs/*.md`, or the owning PRD, only when their `LOAD_WHEN` applies
- `tasks/reference/PRD-PROTOCOL.md`, relevant source inputs, acceptance oracles, open questions, proof expectations, and handoff context when PRD quality is being reviewed
- selected `docs/*.md`, `tasks/reference/*.md`, public inventory rows, generated-doc freshness results, and current owner files when cross-reference or staleness is being reviewed
- PRD handoff readiness packet output when the review question is whether a PRD is ready for decomposition, design, engineering, or review handoff
- `tasks/prds/PRD-038-engineering-quality-review-lane.md` when implementing, validating, or changing the Engineering Quality Review Lane package capability

If the active bead, draft PRD, package surface, primary authority, recorded evidence, source file family, or changed-file summary needed for the selected lane is missing, stop and ask for the missing source instead of inventing a review.

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

## PRD Quality Review Lane

Use this lane to inspect whether one draft PRD is clear enough for a human PRD approval conversation.

Focus on:

- user problem clarity and whether the painful before moment and better after moment are specific
- strategy fit, intended user, current workaround or evidence, and why the work matters now
- non-goals, not-yet scope, assumptions, stale inputs, conflicting source inputs, and open questions
- acceptance quality, observable checks, optional EARS-style wording only when it clarifies verification, and requirement-to-proof readiness
- handoff readiness, product-changing risks, architecture-shaping triggers, and the smallest first slice before decomposition
- whether findings belong in the PRD, an owner-file update, a PRD amendment, Architecture Shaping, Requirements Gap And Conflict Review, Decomposition, or a parked follow-up

The PRD Quality Review Lane complements Requirements Gap And Conflict Review. Requirements Gap And Conflict Review catches requirement gaps, conflicting constraints, missing edge cases, unstated assumptions, stale source inputs, weak acceptance oracles, and owner-file follow-ups. PRD Quality Review Lane reviews the draft PRD as a product-quality and handoff-readiness artifact before approval.

The PRD Quality Review Lane may recommend `accepted`, `revise`, `split`, `blocked`, or `stop` as review input only. It must not approve the PRD, certify PRD quality, rewrite the PRD, rewrite owner files, generate implementation tasks, activate beads, approve handoff, accept implementation, create scorecard authority, create checker authority, create generated proof, mutate GitHub, mutate external systems, replace PRD Protocol, or replace Requirements Gap And Conflict Review.

## Engineering Quality Review Lane

Use this lane to inspect whether one completed or nearly completed active bead respected the Engineering Quality floor well enough for a human acceptance conversation.

Focus on:

- whether the implementation stayed inside the active bead, files in play, and primary authority
- whether the chosen shape was the simplest acceptable implementation for the requirement and proof path
- whether owner-file and boundary integrity held across modules, configuration, dependency, external-service, secret, data, and sensitive-surface boundaries
- whether configuration or dependency handling and sensitive-surface routing were explicit when those risks appeared
- whether recorded checks, manual verification, and Closeout Evidence actually support the quality claims being reviewed
- whether stop conditions, approval gates, and routing triggers were observed before risk expanded
- whether any finding belongs in Closeout Evidence, a PRD amendment, owner-file update, candidate or approved bead, Release Readiness, reviewed memory, or another Review Lane

The Engineering Quality Review Lane complements the Engineering Quality Standards Protocol and is owned as a package capability by `tasks/prds/PRD-038-engineering-quality-review-lane.md`. The Standards Protocol is the pre-coding quality floor; this lane is post-implementation review input. It does not replace Security, Release / Docs Freshness, Dependency Graph, PRD Quality, Verification Guardrail, Tool Execution, Architecture Shaping, System Design Pattern, or Release Readiness.

The Engineering Quality Review Lane may recommend `accepted`, `revise`, `split`, `blocked`, or `stop` as review input only. It must not accept implementation, approve review, certify code quality, certify production readiness, score code, create checker authority, create scorecard authority, replace linters, replace tests, inspect app code, add repo heuristics, add language-aware analysis, create follow-up tasks, rewrite owner files, activate beads, approve release, mutate GitHub, mutate external systems, or turn review output into generated proof.

## Cross-Reference / Staleness Review Lane

Use this lane to inspect whether a bounded documentation/reference surface still points to the right package authorities and current generated reading surfaces.

Focus on:

- stale, deleted, renamed, or superseded file references, alias names, prompt names, command names, and owner pointers
- missing links, missing backlinks, missing owner pointers, stale generated-surface pointers, or public/private boundary drift
- duplicate concept labels, contradictory guidance, and semantic drift that need manual owner-file comparison before any claim is treated as current
- whether `docs-html/`, PRD HTML, roadmap HTML, Work Graph, or other generated surfaces should be refreshed from source Markdown rather than hand edited
- whether findings belong in an owner-file update, PRD amendment, protocol update, public package inventory update, generated-surface refresh, Candidate Queue entry, reviewed memory review, maintainer changelog entry, or maintainer roadmap follow-up

The Cross-Reference / Staleness Review Lane may recommend `accepted`, `revise`, `split`, `blocked`, or `stop` as review input only. It must not edit stale references automatically, declare stale claims authoritative, create tasks, approve review, accept implementation, approve PRDs, approve release, approve transitions, rewrite owner files, rewrite generated output as source truth, create a generated report family, create checker authority, become a required gate for every docs change, inspect private maintainer files as public package authority, mutate GitHub, mutate external systems, or replace the current owner files.

Use existing freshness and generated-surface checks before proposing new machinery. A future broad doc graph, orphan-page, backlink, contradiction, duplicate-concept, or semantic-lint system belongs in a separate roadmap candidate unless real review examples prove that this lane needs it.

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
- the draft PRD or PRD authority is unclear for PRD Quality Review Lane
- the package surface or source file family is unclear for Cross-Reference / Staleness Review Lane
- recorded checks or manual verification are missing for the risk being reviewed
- the changed-file summary cannot be inspected
- a sensitive surface appears without an approval gate
- the lane would require secrets, credentials, private data, provider config, dashboard values, or production details
- the answer would certify security, compliance, release readiness, or acceptance
- the answer would certify code quality, production readiness, scalability, reliability, or maintainability
- the answer would approve a PRD, certify PRD quality, create scorecard authority, rewrite the PRD, or turn PRD review findings into implementation tasks
- the answer would treat generated Work Graph reports as authority, proof, task selection, or transition approval
- the answer would treat generated HTML, generated reports, or review findings as source authority instead of evidence
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
- certify code quality
- certify production readiness
- create follow-up tasks
- create implementation tasks
- rewrite owner files
- rewrite PRDs
- rewrite generated output as source truth
- choose tasks
- run tasks from graph output
- approve parallel execution
- run mutating commands
- mutate GitHub
- mutate external systems
- treat Work Graph reports as authority, proof, transition approval, or task selection
- treat generated reports, screenshots, browser notes, GitHub status, or confidence as proof
- create scorecard authority
- create checker authority
- create a registry, optional pack, command wrapper, package-manager behavior, release-channel behavior, generated report, checker gate, task-runner system, or persona system
