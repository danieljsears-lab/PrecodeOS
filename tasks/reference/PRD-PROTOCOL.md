# Precode PRD Protocol
<!-- ANCHOR: prd-protocol -->

> AUTHORITY: Product Definition Gate workflow, adaptive PRD ceremony, PRD approval rules, source-input normalization, and PRD-to-feature-to-bead compilation.
> NOT_AUTHORITY: Feature prioritization, final product decisions, active task selection, route structure, schema definitions, or implementation status.
> LOAD_WHEN: Turning a product idea into an approved PRD shard, compiling requirements into `FEATURES.md`, or deriving beads from product definition.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-04-26

## Purpose

The Product Definition Gate prevents an AI coding agent from turning vague intent into code.

It sits between the product reference layer and the execution bead layer:

```text
local material or idea -> source intake -> guided framing -> PRD shard -> FEATURES.md inventory -> execution beads -> recorded evidence
```

The PRD is not active memory. It is a reference shard loaded only when defining or implementing the feature it owns.

Use `tasks/reference/LOCAL-SOURCE-INTAKE-PROTOCOL.md` when the idea is sourced from local notes, docs, screenshots, chat summaries, issue exports, research files, or manual drafts.

Use `tasks/reference/IDEA-TO-PRD-WORKFLOW.md` when the idea is rough, ambiguous, customer-facing, or still needs guided framing.

Use `tasks/reference/DECOMPOSITION-PROTOCOL.md` before deriving candidate beads or splitting approved feature work.

Use `tasks/reference/INTENT-ORCHESTRATION-PROTOCOL.md` when tracing source intent through PRD requirements, bead proposals, recorded evidence, and review decisions.

Use `tasks/reference/SYSTEM-DESIGN-PATTERN-PROTOCOL.md` when PRD requirements imply external services, multi-step states, interchangeable rules, audit trails, auth/access boundaries, or an implementation-shape choice that should be clear before bead derivation.

## Principle

Every feature needs a PRD shard before coding begins.

The PRD does not need to be large. It needs to be clear enough that a solo non-technical builder can answer:

- where the idea came from
- what user problem is being solved
- what is explicitly not being solved
- what the user can do after the change that they cannot do now
- which requirement IDs exist
- how each requirement will be verified
- which risks require human approval
- which source inputs are evidence and which facts have been promoted
- whether project context or architecture boundaries are affected
- which beads should be created first

## Adaptive Ceremony

Use the smallest PRD that controls the risk.

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

## PRD Workflow

### 1. Intake The Idea

Capture the user's plain-language request without converting it to implementation yet.

Ask only questions that can change product definition, risk, scope, or verification.

If the request comes from notes, docs, GitHub issues, research, screenshots, chat summaries, issue exports, or manual drafts, use the Local Source Intake Protocol and summarize those inputs in the PRD `Source Inputs` section. Source inputs are evidence, not authority.

### 2. Frame Before Writing Requirements

Use lightweight framing before requirements:

- `User Moment`: before/after description of what changes for the user
- `PRFAQ-Lite`: short customer-facing claim and skeptical questions when the work is ambiguous
- `Alternatives Considered`: options rejected, including doing nothing
- `Architecture / Project Context Impact`: whether `PROJECT-CONTEXT.md` or another authority file must be loaded
- `Anti-Shallow Checks`: missing problem, missing non-goals, unverifiable requirements, or hidden sensitive surfaces
- `Smallest First Bead`: the narrowest useful execution unit, with likely checks and manual verification

Do not create implementation beads while these sections still expose unresolved implementation-changing gaps.

### 3. Create Or Update A PRD Shard

Use `tasks/prds/PRD-000-template.md`.

Set status to `draft` while shaping the product definition.
Keep the structured PRD metadata in frontmatter and the deeper requirement definition in the body sections.

### 4. Resolve Blockers

Move unresolved implementation-changing questions into the PRD `Open Questions` section.

When a question becomes a hard decision, record it in `DECISIONS.md` and point back to it from the PRD.

### 5. Approve The PRD

Set status to `approved` only when:
- goals and non-goals are clear
- before/after user moment is clear
- requirement IDs are stable
- every requirement has an acceptance oracle
- risk and permission gates are explicit
- approval risks and sensitive surfaces are named
- architecture/project-context impacts are known
- shallow-artifact checks have passed or have been resolved
- the feature can be compiled into `FEATURES.md`
- bead proposals are narrow enough to execute one logical unit at a time

### 6. Compile Into `FEATURES.md`

`FEATURES.md` remains the compiled feature inventory.

After PRD approval, update `FEATURES.md` with:
- the feature summary
- functional requirements
- MVP or later-scope status
- pointers back to the PRD shard for deeper requirement definition

Do not copy the whole PRD into `FEATURES.md`.
Compile only the stable feature summary and functional requirements, not the full narrative shard.

### 7. Derive Beads

Create beads from the approved PRD.

Candidate beads must pass the Bead Decomposition Test before activation. If a proposal is too broad, has multiple authority owners, lacks verification, or mixes planning with implementation, mark it `not a bead yet` and keep shaping.

Use `tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md` if it is unclear whether the next artifact should be a PRD amendment, bead proposal, challenge-planning bead, review bead, unblocker bead, or state repair.

Use `tasks/reference/LONG-HORIZON-PLANNING-PROTOCOL.md` when approved PRDs have proposed or deferred work that should be reviewed without becoming active work.

Each bead must include:
- `Parent PRD`
- `Requirement IDs`
- one primary authority file
- done-when statement
- files in play
- checks
- stop conditions

The PRD may propose beads, but `tasks/todo.md` and the bead transition command control which bead becomes active.

### 8. Amend Carefully

If the PRD changes after beads exist:
- add an amendment note in the PRD
- update `FEATURES.md` only if the compiled inventory changed
- create follow-up beads for new work
- do not widen an active bead silently

## Definition Of Ready

A feature is ready for implementation when:
- its PRD shard is `approved`
- `FEATURES.md` has the compiled requirement inventory
- the first bead cites the parent PRD and requirement IDs
- open questions are either resolved or explicitly non-blocking
- sensitive work has clear human approval gates
- project-context and architecture impacts have an owning file or are explicitly none
- PRFAQ-lite or user-moment framing has prevented shallow solution-first requirements
- verification is known before code starts
- the smallest first bead is identified and does not require multiple primary authority files
- candidate beads pass the decomposition test or are explicitly marked `not a bead yet`

## Stop Conditions

Stop before bead creation if:
- the PRD is not approved
- requirement IDs are missing
- acceptance oracles are vague
- non-goals are missing for broad work
- risks require a human decision
- the feature would need route, schema, or security changes that have no owning authority file update

Stop during implementation if:
- the bead no longer maps to the PRD requirement IDs
- a new requirement appears
- a blocker changes the PRD
- an approval gate is reached
