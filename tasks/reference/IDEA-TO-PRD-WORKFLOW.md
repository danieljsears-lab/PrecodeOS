# Precode Idea To PRD Workflow
<!-- ANCHOR: idea-to-prd-workflow -->

> AUTHORITY: Guided local source intake, idea framing, PRFAQ-lite, shallow-artifact prevention, PRD readiness, and bead-derivation workflow for PrecodeOS.
> NOT_AUTHORITY: Final product decisions, active task selection, route structure, schema definitions, implementation plans, or generated progress state.
> LOAD_WHEN: Turning a rough idea, note, chat summary, issue export, research result, screenshot, design, diagram, or manual draft into a PRD shard and candidate beads.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.6
Last updated: 2026-05-18

## Purpose

This workflow helps a solo builder move from a rough product idea to an approved PRD shard without asking the builder to become a product manager first.

The workflow is intentionally light. It borrows the useful parts of progressive context, Working Backwards PRFAQ thinking, Shape Up-style bounded appetite, and small-iteration discipline, but routes every output through Precode authority ownership.

Use `PRODUCT.md` as the builder-facing product constitution when the idea may affect product promise, users and jobs, strategy and non-goals, current bets, success signals, or design and voice direction. `PRODUCT.md` orients product planning; it does not approve PRDs, compile features, activate beads, or replace feature PRD shards.

For a net-new, rough product idea from a non-technical builder, the default path is:

```text
Product Ideation Workbook -> Product Brief -> Local Source Intake -> gentle PRD ramp -> technical shaping only when needed -> PRD shard -> FEATURES.md compile -> bead proposals
```

Bypass the workbook for bugs, maintenance, approved PRD follow-through, narrow feature changes, and other work where the product problem and scope are already clear.

The PRD shard is the destination document: it describes where the work is trying to arrive, what counts as done, and which requirements are stable enough to verify.

The bead proposals are journey units: they describe the smallest safe steps toward that destination. `tasks/todo.md` is the active journey pointer and remains the only active-work selector.

Use `tasks/reference/INTENT-ORCHESTRATION-PROTOCOL.md` when explaining which lifecycle state the idea is in, deciding whether intent is ready to promote, or handling changed intent that needs a PRD amendment, decision, defer note, or follow-up bead.

Use `tasks/reference/UBIQUITOUS-LANGUAGE-PROTOCOL.md` when the idea depends on domain vocabulary, aliases, UI labels, code/test naming, confusing terms, or stale vocabulary from older artifacts.

Use `tasks/reference/PRODUCT-DISCOVERY-VALIDATION-PROTOCOL.md` before PRD shaping when the idea is broad, risky, market-facing, paid, evidence-poor, solution-first, or when the main uncertainty is whether the problem, user, current workaround, demand signal, or smallest learning step is real enough to justify a PRD.

None of these artifacts are active memory. The active-memory set remains:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

## Workflow Lenses

Use these as optional Navigator lenses, not first-class modes or named agents.

| Lens | Job | Use When |
|---|---|---|
| Analyst lens | Find the real problem, evidence, assumptions, and alternatives | The idea is vague, market-shaped, or based on a hunch |
| Product Manager lens | Turn the problem into goals, non-goals, requirements, and acceptance checks | The builder wants to know what should actually ship |
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

For net-new, rough product ideas from a non-technical builder, route the builder to `tasks/templates/PRODUCT-IDEATION-WORKBOOK.md` before asking Precode to update `PRODUCT.md`, draft a PRD, propose beads, or code. Treat the workbook as a thinking space, not authority.

Use a founder-friendly question budget during early intake: after at most three high-level product or business questions, produce a short `Product Brief` and one next best question. The Product Brief is evidence only and should include:

- product idea
- intended user
- painful before moment
- better after moment
- current workaround or evidence
- assumptions
- not-yet list
- smallest useful version
- next best question

Early questions should ask about the user, pain, before/after moment, current workaround, evidence, business constraint, scope boundary, and what not to build yet. Do not ask the builder to decide architecture, module boundaries, test strategy, owner files, acceptance matrices, or system behavior unless a concrete risk has already surfaced.

If the idea sounds exciting but weakly evidenced, too broad, paid, market-facing, or solution-first, run Product Discovery Validation before drafting a PRD. The output should be a short Discovery Summary with the target user, current workaround, strongest evidence, weakest assumption, smallest non-code learning step, and advisory `proceed | pause | narrow | kill` recommendation.

If discovery recommends `pause`, `narrow`, or `kill`, do not draft requirements yet. Return the Discovery Summary, name what evidence or narrowing is needed, and remind the builder that discovery is evidence only, not product approval or task activation.

If the target project has a `PRODUCT.md`, load it when the idea is product-facing or could change product direction. Use it to check fit, name product drift, and avoid suggestions that contradict current non-goals.

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

- Product Brief or idea summary
- target user
- product-constitution fit or gap
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

## Stage 3: Alignment

Use alignment before writing the PRD when the idea is vague, source-heavy, user-facing, risky, or likely to hide product or implementation assumptions.

The goal is a shared design concept, not an early plan. The agent should interview the builder one question at a time, walk dependencies in a sensible order, and provide a recommended answer with each question so the builder can accept, reject, or adjust quickly.

For non-technical builders, keep the first alignment pass conversational and product-facing. Ask at most three high-level questions before summarizing progress as a Product Brief. Translate technical implications yourself after the builder confirms the product story.

Good alignment questions can change:

- user problem or audience
- before/after moment
- goals, non-goals, or appetite
- current workaround, evidence, or demand signal
- business constraint, trust concern, or sensitive-surface approval gate
- first useful vertical slice
- shared domain language, aliases, or terms to avoid

Later technical questions can change data, architecture, module boundary, testing strategy, manual QA expectation, or owner-file impact. Ask those only after product alignment is stable or when a surfaced risk would make the Product Brief misleading.

Stop alignment when the remaining questions would only add polish, implementation trivia, or low-risk preferences that can be deferred to bead execution.

Preserve the alignment output as source evidence. Summarize the stable decisions, rejected options, open questions, and stale or discarded assumptions into the PRD shard. Do not treat the raw conversation as authority.

## Stage 3a: Shared-Language Check

Before writing the PRD, pause when the idea contains domain terms the builder keeps explaining, terms that appear under multiple names, or labels that will affect UI, tests, code, or module boundaries.

Use the Ubiquitous Language Protocol to capture:

- terms introduced or reused
- aliases the agent should understand
- avoid or confusing terms
- source pointers
- UI/code/test examples when useful
- stale vocabulary from old PRDs, issues, transcripts, or generated summaries

The output can become a PRD `Domain Language` section or a proposed `project_glossary` memory card after review. It does not become active memory.

## Stage 4: PRFAQ-Lite

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

If PRFAQ-lite changes product-level strategy, users, non-goals, success signals, or design and voice direction, update `PRODUCT.md` after the builder reviews the change.

If PRFAQ-lite exposes weak problem evidence, no current workaround, no believable demand signal, or a first slice too large to learn from, return to Product Discovery Validation instead of polishing the PRD.

## Stage 5: Anti-Shallow Check

Before creating requirements, challenge the artifact.

Stop if the artifact:

- names a solution but not a user problem
- contains goals without non-goals
- lacks a before/after user moment
- contradicts `PRODUCT.md` without a reviewed product decision
- has requirements that cannot be verified
- says "simple" while touching auth, payments, data, uploads, external services, or destructive actions
- needs a route, schema, security, or architecture change with no owning authority file
- proposes more than one logical unit for the first bead
- relies on generated text that the user has not approved

If the artifact fails, keep shaping. Do not create implementation beads yet.

## Stage 6: Create Or Update The PRD Shard

Use `tasks/prds/PRD-000-template.md`.

Keep the builder-facing story at the top of the PRD: Product Brief, problem, user moment, destination, goals, non-goals, and risks in plain English. Dense requirement IDs, acceptance checks, architecture impact, module/interface candidates, and agent context are agent-facing translation layers. The agent should draft those from the aligned product story instead of testing the builder on technical vocabulary.

The PRD shard owns:

- alignment summary
- source inputs summary
- domain language summary
- destination statement
- product-constitution fit or gap
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
- completed journey history after the feature has drifted

Move those facts to their owning files and leave pointers in the PRD.

## Stage 7: Context And Architecture Check

Load `PRODUCT.md` when the PRD might change:

- product promise
- target users or jobs
- strategy or non-goals
- current bets
- success signals
- design or voice direction

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
- Module boundary: which interface, behavior contract, and test boundary should the human own before delegating internals?

Do not create diagrams or architecture docs unless they clarify a real decision.

## Stage 8: Product Definition Gate

A PRD can move to `approved` only when:

- the user problem is clear
- discovery evidence is summarized or explicitly skipped with a reason when worth-building uncertainty was material
- goals and non-goals are explicit
- product-constitution fit has been checked when relevant
- requirement IDs are stable
- every requirement has an acceptance oracle
- sensitive surfaces have approval gates
- implementation-changing open questions are resolved or marked non-blocking
- project-context and authority impacts are known
- the first bead can be one logical unit

If the PRD is not ready, set status to `needs_info` and name the exact question or evidence needed.

## Stage 9: Derive Beads

Derive beads from approved PRD requirements.

Load `tasks/reference/DECOMPOSITION-PROTOCOL.md` before turning PRD requirements into candidate beads.

Each bead proposal must include:

- requirement IDs
- one primary authority file
- done-when target
- delegation mode
- test strategy
- review context
- files likely in play
- checks
- manual verification
- stop conditions

Prefer the smallest valuable change that preserves quality. For user-facing work, prefer a vertical journey unit that crosses enough layers to produce observable feedback instead of a horizontal schema-only, backend-only, frontend-only, or tests-later slice. Move edge cases, polish, and uncertain follow-ups into later beads instead of widening the first bead.

If the work fails the Bead Decomposition Test, mark it `not a bead yet` and return to source intake, PRD shaping, decision logging, architecture/security/API/schema clarification, or an unblocker bead.

## Stage 10: Handoff To Execution

Before implementation begins:

- compile stable requirements into `FEATURES.md`
- create or update candidate beads
- update `PRODUCT.md` only if the approved PRD changed product-level promise, users, strategy, current bets, success signals, or design and voice direction
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
