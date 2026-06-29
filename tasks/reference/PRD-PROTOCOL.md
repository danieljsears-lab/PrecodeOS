# Precode PRD Protocol
<!-- ANCHOR: prd-protocol -->

> AUTHORITY: Product Definition Gate workflow, adaptive PRD ceremony, PRD approval rules, source-input normalization, and PRD-to-feature-to-bead compilation.
> NOT_AUTHORITY: Feature prioritization, final product decisions, active task selection, route structure, schema definitions, or implementation status.
> LOAD_WHEN: Turning a product idea into an approved PRD shard, compiling requirements into `FEATURES.md`, or deriving beads from product definition.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.19
Last updated: 2026-06-29

## Purpose

The Product Definition Gate prevents an AI coding agent from turning vague intent into code.

It sits between the product reference layer and the execution bead layer:

```text
First PRD Walkthrough for rough ideas -> Product Ideation Workbook step -> Product Brief -> Conviction Packet when useful -> source intake -> gentle PRD ramp -> PRD shard -> FEATURES.md inventory -> Architecture Shaping when risk-triggered -> execution beads -> recorded evidence
```

For first-time non-technical builders, this path may be invoked as the First PRD Walkthrough. The walkthrough is a discoverability layer over existing Product Ideation Workbook, Precode Idea Coach, Product Brief, Challenge And Clarity, Conviction Packet, Local Source Intake, and PRD shaping guidance. It does not draft or approve PRDs by itself, mutate owner files, create a roadmap or backlog, create or activate beads, compile features, or authorize implementation. Product Briefs, Conviction Packets, workbook output, research, and source summaries remain evidence only until reviewed conclusions are promoted through the normal PRD workflow.

The PRD is not active memory. It is a destination document loaded only when defining or implementing the feature it owns.

Execution beads are journey units derived from that destination. `tasks/todo.md` points to the active journey unit; the PRD may propose beads but must not activate them.

Generated PRD HTML under `tasks/prds-html/` is a committed review convenience generated from `tasks/prds/*.md`. It can make PRD status, requirements, risks, blockers, bead proposals, approval state, PRD handoff readiness, and Acceptance Oracle Matrix review easier to inspect. Generated PRD pages may export a proposed Acceptance Oracle Matrix Markdown replacement block for manual application, but Markdown PRD shards remain canonical. Generated PRD HTML cannot approve PRDs, activate beads, choose tasks, accept implementation, write source Markdown, promote generated text, persist browser edits, or replace PRD shards.

Use `PRODUCT.md` during product planning, PRD creation, PRD approval review, PRD amendment, or product drift checks. `PRODUCT.md` orients the product promise, users and jobs, strategy and non-goals, current bets, success signals, and design or voice pointers. It does not approve features, activate beads, or replace PRD shards.

Use `tasks/reference/LOCAL-SOURCE-INTAKE-PROTOCOL.md` when the idea is sourced from local notes, docs, screenshots, chat summaries, issue exports, research files, or manual drafts.

Use `tasks/reference/CANDIDATE-QUEUE-PROTOCOL.md` when the idea starts from `CANDIDATE-QUEUE.md`. A Candidate Queue entry may be cited in PRD `Source Inputs`, including product-value rating, themes, and near-bead sketch IDs when they helped shape the PRD, but it is evidence and origin trace only; it does not approve the PRD, compile requirements, reserve `B###` IDs, or authorize beads.

Use `tasks/reference/CLIENT-ENGAGEMENT-INTAKE-PROTOCOL.md` when the source is a client PRD, existing codebase, frontend design handoff, Ember/backend plan, sprint plan, or repo-topology decision.

Use `tasks/reference/IDEA-TO-PRD-WORKFLOW.md` when the idea is rough, ambiguous, customer-facing, or still needs guided framing.

Use `tasks/reference/DECOMPOSITION-PROTOCOL.md` before deriving candidate beads or splitting approved feature work.

Use `scripts/prd-handoff-readiness.py --prd <path>` when an approved PRD needs an advisory readiness packet before decomposition, design handoff, engineering handoff, or PRD review. The packet may summarize PRD status, requirement IDs, open questions, Acceptance Oracle coverage, candidate bead readiness, proof expectations, risks, owner protocols, blockers, and next safe action. It is generated evidence only: it does not approve the PRD, choose tasks, activate beads, accept implementation, mutate external tools, automate exports, create MCP behavior, create registries, create optional packs, or imply package-manager behavior.

Use `tasks/reference/INTENT-ORCHESTRATION-PROTOCOL.md` when tracing source intent through PRD requirements, bead proposals, recorded evidence, and review decisions.

Use `tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md` for Plan Loop routing when the user explicitly wants to explore a feature angle before committing to PRD amendment, Architecture Shaping, Decomposition, candidate bead proposal, or activation. A Plan Packet is evidence only and does not approve the PRD, compile requirements, create beads, or authorize implementation.

Use `tasks/reference/ARCHITECTURE-SHAPING-PROTOCOL.md` after PRD approval and before bead derivation when approved requirements imply auth, data model, API, integration, dependency, migration, external-service, multi-step workflow, or multi-system risk that should be visible to a non-technical builder before an AI coding agent plans implementation.

Use `tasks/reference/SYSTEM-DESIGN-PATTERN-PROTOCOL.md` when Architecture Shaping or PRD requirements imply external services, multi-step states, interchangeable rules, audit trails, auth/access boundaries, or an implementation-shape choice that should be clear before bead derivation.

Use `tasks/reference/UBIQUITOUS-LANGUAGE-PROTOCOL.md` when requirements, UI labels, module/interface names, tests, or source inputs depend on domain vocabulary.

## Principle

Every feature needs a PRD shard before coding begins.

The PRD does not need to be large. It needs to be clear enough that a solo non-technical builder can understand and approve:

- where the idea came from
- what the Product Brief and alignment conversation established
- which shared terms, aliases, and avoid terms matter
- what user problem is being solved
- what is explicitly not being solved
- what the user can do after the change that they cannot do now
- whether the work fits the product constitution in `PRODUCT.md`
- how the agent translated the builder's intent into requirement IDs
- how each requirement will be verified in plain English, including the evidence lane and recorded source when proof drift would matter
- whether vague acceptance criteria can be clarified with optional EARS-style wording such as `WHEN [condition/event] THE SYSTEM SHALL [expected behavior]`
- which risks require human approval
- which source inputs are evidence and which facts have been promoted
- whether project context or architecture boundaries are affected, explained without making the builder choose implementation internals
- whether architecture-sensitive approved work needs an evidence-only Architecture Brief before bead proposals
- which beads should be created first

## Adaptive Ceremony

Use the smallest PRD that controls the risk.

Adaptive ceremony includes a Fast Learning Lane for low or medium-risk work where the builder wants speed and the first build is a tiny reversible learning slice. The lane may skip the workbook, Exploration Loop, full discovery interview, PRFAQ-lite, shared-language pass, fresh chat, and deep architecture framing when they are not needed to control risk.

A Fast Learning Lane PRD is still a PRD. It must include the problem, user moment, goals and non-goals, stable requirement IDs, acceptance oracle, risk gates, approval, and one bead proposal before coding begins.

Discovery may be skipped only with an explicit reason, such as low risk, clear user problem, no sensitive surfaces, no product-promise drift, and a tiny reversible learning slice. If worth-building uncertainty becomes material, return to Product Discovery Validation instead of using the shortcut.

## Founder-Friendly Ramp

For a net-new, rough product idea from a non-technical builder, do not begin by asking PRD, architecture, workflow, module, test, or owner-file questions. Start with First PRD Walkthrough, using Product Ideation Workbook and Precode Idea Coach as ordered steps, then produce a non-authoritative Product Brief after at most three high-level product or business questions. If the builder is still before repo setup or still building product confidence, produce a Conviction Packet before Local Source Intake instead of drafting a PRD.

Use "First PRD Walkthrough" as the plain-language request for this ramp when the builder wants the shortest safe route from rough idea to PRD readiness. If the walkthrough produces a Conviction Packet, workbook output, notes, research, screenshots, or other source material, route that material through Local Source Intake before drafting the PRD. Human PRD approval remains required before feature compilation, decomposition, bead activation, or coding.

The Product Brief should name the product idea, intended user, painful before moment, better after moment, current workaround or evidence, assumptions, primary hypothesis or learning target when useful, not-yet list, smallest useful version, and next best question.

The Conviction Packet should name the strongest evidence, weakest assumption, primary hypothesis or learning target, guided research notes, MVP-ready first slice, smallest learning step, and not-yet list. It is evidence only and must go through Local Source Intake before PRD shaping.

The agent owns the technical translation after the builder confirms the product story. Requirement IDs, acceptance-check matrices, architecture/project context impact, module/interface candidates, agent context contracts, and bead proposals are internal control surfaces unless the builder must approve a specific risk or tradeoff.

Bypass this ramp for bugs, maintenance, approved PRD follow-through, narrow feature changes, and tiny low-risk work where the product problem and scope are already clear.

### Low Risk

Use for small UI copy, visual polish, or docs-only behavior.

Minimum required:
- source inputs
- problem
- user moment
- goals and non-goals
- requirement IDs
- acceptance oracle matrix
- bead proposals
- anti-shallow checks
- approval

### Medium Risk

Use for normal feature work, multi-step UI, API behavior, or stateful flows.

Include all low-risk sections plus:
- users
- PRFAQ-lite when the user problem or scope is still forming
- alternatives considered
- risk and permission model
- architecture/project context impact
- agent context contract
- compilation notes for `FEATURES.md`

### High Risk

Use for auth, payments, personal data, uploads, destructive actions, external integrations, new dependencies, or ambiguous product bets.

Include all sections plus:
- explicit human approval gates
- security and privacy requirements
- manual dashboard steps
- rollout or experiment plan when success needs measurement
- stop conditions that block bead creation until resolved

If the work is an experiment or rollout, also load `tasks/reference/PLANNING-PROTOCOL.md`.

For high-risk PRDs, do not turn approval into architecture permission. Approval means the product destination is stable enough to compile and shape. Architecture-sensitive work may still need Architecture Shaping before decomposition.

## PRD Workflow

### 1. Intake The Idea

Capture the user's plain-language request without converting it to implementation yet.

Ask only questions that can change product definition, risk, scope, or verification. For early founder intake, keep those questions product-facing: user, pain, before/after moment, current workaround, evidence, business constraint, scope boundary, and non-goals.

When the idea may change product promise, target users, non-goals, current bets, success signals, or design and voice direction, load `PRODUCT.md` and check fit before drafting requirements.

If the request comes from Candidate Queue entries, Candidate Queue shaping proposals, notes, docs, GitHub issues, research, screenshots, chat summaries, issue exports, or manual drafts, use the Local Source Intake Protocol and summarize those inputs in the PRD `Source Inputs` section. Source inputs are evidence, not authority.

### 1a. External PRD Normalization

When a client brings an external PRD, product spec, design handoff, backend plan, sprint plan, or existing codebase, do not treat that artifact as a Precode PRD.

First use `tasks/reference/CLIENT-ENGAGEMENT-INTAKE-PROTOCOL.md` and `tasks/reference/LOCAL-SOURCE-INTAKE-PROTOCOL.md` to summarize:

- source inputs and references
- stable client facts
- stale or conflicting inputs
- open questions that could change implementation
- repo topology and existing codebase facts when relevant
- design, architecture, API, schema, security, or acceptance impacts
- owner files likely affected

Then create or amend a Precode PRD shard using the normal PRD workflow. The external PRD remains source evidence until the Precode PRD shard is reviewed and approved.

### 2. Align Before Writing Requirements

Use an alignment session when the idea is ambiguous, risky, source-heavy, user-facing, or likely to hide product, architecture, testing, or approval decisions.

Ask one question at a time. Include a recommended answer with each question. Keep going until the builder and agent have a shared design concept that can be summarized into a PRD without relying on chat history.

For non-technical builders, summarize progress as a Product Brief after at most three high-level questions. Defer architecture, module/interface, test-strategy, owner-file, acceptance-matrix, and system-behavior questions until product alignment is stable or a surfaced risk requires approval.

Do not produce a plan while implementation-changing alignment questions remain. Store only the stable alignment summary, rejected options, and open questions in the PRD. The raw transcript remains source evidence.

### 2a. Clarify Shared Language

When terms are domain-heavy, overloaded, or inconsistent across sources, create a short `Domain Language` pass before requirements harden.

Name:

- terms introduced by the feature
- existing terms reused from product docs, code, or reviewed memory
- aliases the builder or users may say
- avoid or confusing terms
- UI, code, test, docs, support, or module/interface examples that should use the same vocabulary
- stale vocabulary that should remain historical evidence only

If the shared language should survive beyond the PRD, propose a reviewed `project_glossary` memory card with source pointers, examples, freshness, and promotion owner when applicable. Do not treat glossary memory as authority, and do not use it to rename broadly without current owner-file review.

### 3. Frame Before Writing Requirements

Use lightweight framing before requirements:

- `Product Brief`: non-authoritative summary of the idea, user, before/after moment, evidence, assumptions, not-yet list, smallest useful version, and next best question
- `Primary hypothesis / learning target`: testable belief or learning question that names the user or situation, pain or current workaround, expected behavior, supporting evidence, weakest assumption, and falsifier; evidence only, not PRD approval or implementation permission
- `Hypothesis review status`: optional learning review label from `tasks/reference/HYPOTHESIS-REVIEW-PROTOCOL.md` such as `untested`, `tested`, `narrowed`, `killed`, `promoted`, `stale`, or `not applicable`; evidence only, not PRD approval, Candidate Queue ranking, bead activation, task selection, analytics requirement, or implementation permission
- `Product Fit`: how the idea aligns with `PRODUCT.md`, or which product-constitution gap must be resolved
- `Domain Language`: terms introduced, reused, rejected, or likely to shape UI/code/test names
- `User Moment`: before/after description of what changes for the user
- `PRFAQ-Lite`: short customer-facing claim and skeptical questions when the work is ambiguous
- `Alternatives Considered`: options rejected, including doing nothing
- `Architecture / Project Context Impact`: whether `PROJECT-CONTEXT.md` or another authority file must be loaded
- `Module / Interface Shape`: which deep module, public interface, behavior contract, or test boundary should be human-owned before internals are delegated
- `Anti-Shallow Checks`: missing problem, missing non-goals, unverifiable requirements, or hidden sensitive surfaces
- `Smallest First Bead`: the narrowest useful execution unit, with likely checks and manual verification

Treat the technical items in this framing list as agent translation work. Ask the builder to approve plain-English tradeoffs, not to invent architecture or testing vocabulary.

Do not create implementation beads while these sections still expose unresolved implementation-changing gaps.

### 4. Create Or Update A PRD Shard

Use `tasks/prds/PRD-000-template.md`.

Set status to `draft` while shaping the product definition.
Keep the structured PRD metadata in frontmatter and the deeper requirement definition in the body sections.

### 5. Resolve Blockers

Move unresolved implementation-changing questions into the PRD `Open Questions` section.

When a question becomes a hard decision, record it in `DECISIONS.md` and point back to it from the PRD.

### 6. Run Requirements Gap And Conflict Review

Before PRD approval, design promotion, bead derivation, or implementation, run an advisory requirements review when the PRD or spec is broad, ambiguous, source-heavy, user-facing, risky, or likely to hide edge cases.

The review checks the requirement set as a whole, not just individual rows. It should identify:

- requirement gaps
- conflicting constraints
- missing edge cases
- unstated assumptions
- vague or unverifiable acceptance oracles
- stale or conflicting source inputs
- owner-file follow-ups needed before implementation

When an acceptance oracle is vague, the agent may suggest optional EARS-style phrasing: `WHEN [condition/event] THE SYSTEM SHALL [observable expected behavior]`. Use the pattern only when it makes verification clearer. Do not require EARS syntax, reject clear non-EARS acceptance criteria, change PRD table schema, treat the wording as proof, or treat the rewrite as PRD approval, implementation acceptance, bead activation, or implementation authority.

Return questions and suggested fixes only. The review output is review input, not authority. It must not approve the PRD, rewrite owner files, create or activate beads, convert findings into implementation instructions, accept design promotion, or treat generated review text as proof.

Use this stable output shape:

```text
Review target:
Authority checked:
Requirement gaps:
Conflicts:
Missing edge cases:
Unstated assumptions:
Acceptance weaknesses:
Suggested owner-file updates:
Stop conditions:
Recommendation: revise | clarify | split | ready-for-human-approval-review | stop
```

Resolve implementation-changing findings before approval. Non-blocking concerns may remain only when they are explicitly named as non-blocking, moved to not-yet scope, or routed to a follow-up PRD amendment, owner-file update, architecture-shaping pass, review bead, or candidate bead.

### 6a. Run PRD Quality Review Lane When The Draft Needs A Product-Quality Lens

Use the PRD Quality Review Lane when a draft PRD looks structurally complete but still needs pre-approval review for user problem clarity, before/after moment, strategy fit, non-goals, assumptions, stale or conflicting inputs, acceptance quality, requirement-to-proof readiness, open questions, handoff readiness, or smallest first slice.

The lane complements Requirements Gap And Conflict Review. Requirements Gap And Conflict Review catches requirement gaps, conflicts, missing edge cases, unstated assumptions, stale source inputs, weak acceptance oracles, and owner-file follow-ups. PRD Quality Review Lane reviews the draft PRD as a product-quality and handoff-readiness artifact.

The lane output is advisory review input only. It must not approve the PRD, rewrite the PRD or owner files, create implementation tasks, activate beads, approve handoff, create scorecard authority, create checker authority, create generated proof, or replace human PRD approval.

### 6b. Map Requirements To Proof

Use the Acceptance Oracle Matrix to make proof expectations inspectable before bead work begins. Each important requirement should have an expected behavior, the narrowest useful automated or manual check, and the likely evidence location.

When a requirement, bug behavior, or acceptance criterion is risky, easy to misunderstand, or likely to be reviewed later, name the evidence lane and recorded source that will prove it. This requirement-to-proof trace is advisory traceability, not a separate approval gate. Do not require enterprise trace tables for tiny work, and do not treat generated tests, generated properties, screenshots, browser notes, AI critique, generated reports, or matrix text as proof until the result is recorded or accepted through normal evidence paths.

### 7. Approve The PRD

Set status to `approved` only when:
- goals and non-goals are clear
- before/after user moment is clear
- product-constitution fit has been checked when relevant
- requirement IDs are stable
- every requirement has an acceptance oracle
- acceptance oracles are observable and testable, with optional EARS-style wording only where it improves clarity
- requirements review gaps, conflicts, assumptions, and acceptance weaknesses are resolved or explicitly non-blocking
- risk and permission gates are explicit
- approval risks and sensitive surfaces are named
- architecture/project-context impacts are known
- Architecture Shaping need is identified or explicitly skipped when risk triggers are present
- shallow-artifact checks have passed or have been resolved
- the feature can be compiled into `FEATURES.md`
- bead proposals are narrow enough to execute one logical unit at a time

### 8. Compile Into `FEATURES.md`

`FEATURES.md` remains the compiled feature inventory.

After PRD approval, update `FEATURES.md` with:
- the feature summary
- functional requirements
- MVP or later-scope status
- pointers back to the PRD shard for deeper requirement definition

Do not copy the whole PRD into `FEATURES.md`.
Compile only the stable feature summary and functional requirements, not the full narrative shard.

### 9. Shape Architecture Risk When Needed

After PRD approval and feature compilation, run `tasks/reference/ARCHITECTURE-SHAPING-PROTOCOL.md` before bead derivation when the approved PRD touches auth, data models, APIs, integrations, dependencies, migrations, external services, multi-step workflows, or multi-system changes.

Architecture Shaping produces an evidence-only Architecture Brief. The brief may recommend a PRD amendment, owner-file update, planning bead, unblocker bead, run contract, or safer decomposition, but it does not approve implementation.

If shaping reveals product-changing technical risk, return to PRD amendment or blocking open questions. If shaping reveals durable architecture facts, promote them into the correct owner file before treating them as authority.

### 10. Derive Beads

Create beads from the approved PRD.

Candidate beads must pass the Bead Decomposition Test before activation. If a proposal is too broad, has multiple authority owners, lacks verification, or mixes planning with implementation, mark it `not a bead yet` and keep shaping.

Use `tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md` if it is unclear whether the next artifact should be a PRD amendment, bead proposal, challenge-planning bead, review bead, unblocker bead, or state repair.

If a Plan Packet exists, treat it as source evidence for the next owner workflow. Before PRD approval, it can inform PRD drafting, PRD amendment, Product Discovery, Candidate Queue, owner-file updates, or a stop decision, but it cannot propose beads. After PRD approval, it can inform Architecture Shaping or Decomposition, but candidate beads must still pass the Decomposition Protocol. Before candidate activation, it can challenge or refine the proposal, but it must not update `tasks/todo.md` or activate work.

Use `tasks/reference/LONG-HORIZON-PLANNING-PROTOCOL.md` when approved PRDs have proposed or deferred work that should be reviewed without becoming active work.

Each bead must include:
- `Parent PRD`
- `Requirement IDs`
- one primary authority file
- `delegation_mode`
- `test_strategy`
- `review_context`
- done-when statement
- files in play
- checks
- stop conditions
- domain terms when terminology affects implementation, UI, tests, or review

The PRD may propose beads, but `tasks/todo.md` and the bead transition command control which bead becomes active.

### 11. Amend Carefully

If the PRD changes after beads exist:
- add an amendment note in the PRD
- update `PRODUCT.md` only if the product promise, users, strategy, current bets, success signals, or design and voice pointers changed
- update `FEATURES.md` only if the compiled inventory changed
- create follow-up beads for new work
- do not widen an active bead silently

## Stale Artifact Rule

Completed PRDs, closed issue imports, archived beads, generated summaries, old alignment transcripts, and previous journey notes are historical evidence.

If current code, active memory, the active bead, an approved current PRD, or an owner file conflicts with an old destination or journey artifact, prefer the current authority and record the conflict as a stale input, open question, decision candidate, PRD amendment, or follow-up bead.

## Definition Of Ready

A feature is ready for implementation when:
- its PRD shard is `approved`
- `FEATURES.md` has the compiled requirement inventory
- the first bead cites the parent PRD and requirement IDs
- open questions are either resolved or explicitly non-blocking
- sensitive work has clear human approval gates
- project-context and architecture impacts have an owning file or are explicitly none
- product-constitution impacts have been checked when the work can change product direction
- PRFAQ-lite or user-moment framing has prevented shallow solution-first requirements
- requirements gap and conflict review has no unresolved implementation-changing findings
- verification is known before code starts
- the smallest first bead is identified and does not require multiple primary authority files
- candidate beads pass the decomposition test or are explicitly marked `not a bead yet`

## Stop Conditions

Stop before bead creation if:
- the PRD is not approved
- requirement IDs are missing
- acceptance checks are vague
- non-goals are missing for broad work
- requirements review finds unresolved gaps, conflicts, assumptions, edge cases, or acceptance weaknesses that change implementation scope
- risks require a human decision
- the feature would need route, schema, or security changes that have no owning authority file update

Stop during implementation if:
- the bead no longer maps to the PRD requirement IDs
- a new requirement appears
- a blocker changes the PRD
- an approval gate is reached
