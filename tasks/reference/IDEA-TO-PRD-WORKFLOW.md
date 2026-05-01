# Precode Idea To PRD Workflow
<!-- ANCHOR: idea-to-prd-workflow -->

> AUTHORITY: Guided local source intake, idea framing, PRFAQ-lite, shallow-artifact prevention, PRD readiness, and bead-derivation workflow for Precode OS.
> NOT_AUTHORITY: Final product decisions, active task selection, route structure, schema definitions, implementation plans, or generated progress state.
> LOAD_WHEN: Turning a rough idea, note, chat summary, issue export, research result, screenshot, design, diagram, or manual draft into a PRD shard and candidate beads.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-04-26

## Purpose

This workflow helps a solo builder move from a rough product idea to an approved PRD shard without asking the builder to become a product manager first.

The workflow is intentionally light. It borrows the useful parts of progressive context, Working Backwards PRFAQ thinking, Shape Up-style bounded appetite, and small-iteration discipline, but routes every output through Precode authority ownership.

The path is:

```text
local material or idea -> source intake -> guided framing -> PRFAQ-lite -> PRD shard -> FEATURES.md compile -> bead proposals
```

Use `tasks/reference/INTENT-ORCHESTRATION-PROTOCOL.md` when explaining which lifecycle state the idea is in, deciding whether intent is ready to promote, or handling changed intent that needs a PRD amendment, decision, defer note, or follow-up bead.

None of these artifacts are active memory. The active-memory set remains:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

## Workflow Lenses

Use these as optional Navigator lenses, not first-class modes or named agents.

| Lens | Job | Use When |
|---|---|---|
| Analyst lens | Find the real problem, evidence, assumptions, and alternatives | The idea is vague, market-shaped, or based on a hunch |
| Product Manager lens | Turn the problem into goals, non-goals, requirements, and acceptance oracles | The builder wants to know what should actually ship |
| Architect lens | Check stack fit, project conventions, integration boundaries, and implementation risk | The idea touches architecture, data, auth, payments, dependencies, or external services |
| Reviewer lens | Challenge shallow artifacts before code starts | The PRD sounds polished but still cannot guide beads |

The lenses are prompts for thinking. They do not create new active-memory files, new agent hierarchy, or separate authority.

## Fresh Chat Rule

Use a fresh chat when a workflow stage has produced a stable artifact and the next stage needs a cleaner context.

Good fresh-chat boundaries:

- local source intake complete -> guided framing
- idea intake complete -> PRFAQ-lite
- PRFAQ-lite complete -> PRD shard
- PRD approved -> bead derivation
- bead accepted -> next bead

Before starting fresh, update the durable artifact and run the appropriate validation or checkpoint. Do not rely on chat history as the source of truth.

## Stage 1: Intake Local Sources Or The Idea

Capture the request in the builder's words before turning it into implementation.

When the request comes from local material, first load `tasks/reference/LOCAL-SOURCE-INTAKE-PROTOCOL.md` and create a short source summary.

Ask only questions that can change:

- user or audience
- problem severity
- scope boundary
- success definition
- risk level
- authority file ownership
- verification path

Do not ask questions that can be answered by reading the repo.

Minimum output:

- idea summary
- target user
- suspected problem
- desired outcome
- known source inputs
- open questions that could change implementation

## Stage 2: Source Inputs

Normalize the raw inputs into a short source list or source summary.

Supported inputs:

- notes or docs
- screenshots or designs
- chat transcript summary
- GitHub issues
- research files
- customer quotes
- manual drafts
- existing feature docs

Source inputs are evidence, not authority. Promote only stable conclusions into the PRD shard, `DECISIONS.md`, or the owning reference file.

Use the Local Source Intake Protocol when the source material is more than a single plain-language idea or when it includes screenshots, drafts, exports, research, conflicting notes, or possible secrets.

## Stage 3: PRFAQ-Lite

Use PRFAQ-lite when the work is new, ambiguous, customer-facing, risky, or easy to overbuild.

Keep it short:

- Press-release claim: What changed for the user?
- Customer problem: What pain or job does this solve?
- Before/after moment: What can the user do after this that they cannot do now?
- Customer FAQ: What would a skeptical user ask?
- Internal FAQ: What would the builder, future maintainer, or reviewer worry about?
- Appetite: How much work is worth spending before learning?
- Non-goals: What attractive ideas are intentionally excluded?
- Kill or pause criteria: What would make this not worth building now?

PRFAQ-lite can live inside the PRD shard. It does not need a separate permanent file unless the feature is large enough to justify one.

## Stage 4: Anti-Shallow Check

Before creating requirements, challenge the artifact.

Stop if the artifact:

- names a solution but not a user problem
- contains goals without non-goals
- lacks a before/after user moment
- has requirements that cannot be verified
- says "simple" while touching auth, payments, data, uploads, external services, or destructive actions
- needs a route, schema, security, or architecture change with no owning authority file
- proposes more than one logical unit for the first bead
- relies on generated text that the user has not approved

If the artifact fails, keep shaping. Do not create implementation beads yet.

## Stage 5: Create Or Update The PRD Shard

Use `tasks/prds/PRD-000-template.md`.

The PRD shard owns:

- source inputs summary
- PRFAQ-lite
- problem
- users
- goals and non-goals
- requirements with stable IDs
- acceptance oracle matrix
- risk and permission model
- architecture/project-context impact
- agent context contract
- bead proposals
- compilation notes
- open questions
- approval

The PRD shard does not own:

- route inventory
- schema field definitions
- security policy
- pricing decisions
- active task selection
- generated progress

Move those facts to their owning files and leave pointers in the PRD.

## Stage 6: Context And Architecture Check

Load `PROJECT-CONTEXT.md` when the PRD or bead might change:

- stack choices
- architectural boundaries
- coding conventions
- dependency policy
- integration patterns
- environment assumptions
- testing or deployment expectations

Use lightweight C4-style thinking only as needed:

- System context: who uses this and what external systems are touched?
- Container view: which app, service, database, queue, or external tool is involved?
- Component view: which modules or routes are likely in play?

Do not create diagrams or architecture docs unless they clarify a real decision.

## Stage 7: Product Definition Gate

A PRD can move to `approved` only when:

- the user problem is clear
- goals and non-goals are explicit
- requirement IDs are stable
- every requirement has an acceptance oracle
- sensitive surfaces have approval gates
- implementation-changing open questions are resolved or marked non-blocking
- project-context and authority impacts are known
- the first bead can be one logical unit

If the PRD is not ready, set status to `needs_info` and name the exact question or evidence needed.

## Stage 8: Derive Beads

Derive beads from approved PRD requirements.

Load `tasks/reference/DECOMPOSITION-PROTOCOL.md` before turning PRD requirements into candidate beads.

Each bead proposal must include:

- requirement IDs
- one primary authority file
- done-when target
- files likely in play
- checks
- manual verification
- stop conditions

Prefer the smallest valuable change that preserves quality. Move edge cases, polish, and uncertain follow-ups into later beads instead of widening the first bead.

If the work fails the Bead Decomposition Test, mark it `not a bead yet` and return to source intake, PRD shaping, decision logging, architecture/security/API/schema clarification, or an unblocker bead.

## Stage 9: Handoff To Execution

Before implementation begins:

- compile stable requirements into `FEATURES.md`
- create or update candidate beads
- ensure only one bead is active
- update `tasks/todo.md` only when the user approves activation
- use `bash scripts/session-start.sh` before Builder work

The workflow may propose the next bead. It must not activate it without the normal bead-transition gate.

## Builder Prompts

Useful prompts for a non-technical builder:

```text
Use the Precode Idea To PRD Workflow on this idea.
Do not write code.
First help me clarify the user problem, non-goals, and smallest valuable version.
```

```text
Turn these notes into a draft PRD shard.
Keep active memory tiny.
Use PRFAQ-lite only where it helps.
List the questions that could change implementation.
```

```text
Review this PRD for shallow artifacts.
Tell me what is missing before it can become beads.
Do not create implementation beads until the Product Definition Gate is ready.
```

```text
Derive the first three candidate beads from this approved PRD.
Each bead must be one logical unit, cite requirement IDs, and name one primary authority file.
Use the Decomposition Protocol and tell me if any candidate is not a bead yet.
```

Use `tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md` when the next step could plausibly be source intake, PRFAQ-lite, PRD drafting, decomposition, a challenge bead, review, or state repair.
