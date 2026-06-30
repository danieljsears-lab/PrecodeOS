# PrecodeOS -- Workflow Selection Protocol
<!-- ANCHOR: workflow-selection-protocol -->

> AUTHORITY: Workflow-selection guidance for choosing the next Precode planning, execution, review, unblocker, repair, or prompt-playbook path before work starts.
> NOT_AUTHORITY: Active memory, product decisions, approved requirements, task selection, bead activation, implementation plans, generated progress state, or external mutations.
> LOAD_WHEN: Deciding which Precode workflow to use for a rough idea, local source material, PRD work, bead proposal, blocked task, review, closeout, or state repair.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.22
Last updated: 2026-06-30

## Purpose

Workflow selection helps a user or agent choose the right Precode path before starting work.

Use this protocol when the next step is unclear, when too many protocols could apply, or when an agent may be jumping from idea to implementation too quickly.

For a rough idea, do not present Product Discovery Interview, Product Conviction Packet, Precode Idea Coach, and First PRD Walkthrough as peers. The user-facing route is First PRD Walkthrough. Use Product Discovery Validation only when worth-building uncertainty is the specific blocker, and use the workbook, coach, Product Brief, Conviction Packet, Local Source Intake, and PRD shaping as ordered steps inside the rough-idea path.

First-product spine: `Idea -> Brief -> Packet -> Intake -> PRD -> Bead -> Proof -> Review -> Close`. Workflow selection should preserve the order: Local Source Intake before PRD shaping, human PRD approval before decomposition or bead activation, recorded proof before review, and review before closeout or transition approval.

After the first product slice, repeated work can orient through the every-bead rhythm before choosing a workflow: `Active -> Changed -> Proven -> Parked -> Approval -> Next`. This is a human-facing checklist over existing sources: active bead and `tasks/todo.md` for active work, changed-file summary and Closeout Evidence for changed work, recorded checks and manual verification for proof, Candidate Queue or explicit defer/kill destination for parked intent, review decision and transition proposal for approval, and session start, Workflow Selection, `next-step.py`, or transition proposal for next guidance. The rhythm does not choose tasks, rank candidates, approve PRDs, activate beads, accept review, approve transition, or create generated report authority.

When a user wants to develop an idea into future candidate work or turn a selected candidate into an implementation plan, use the Plan Mode Candidate Craft Loop: `Idea -> Plan Mode -> Candidate Queue -> Plan Mode -> Implementation Plan -> Approved Bead -> Build`. Plan Mode is required before developing a Candidate Queue entry and again before developing an implementation plan. In Codex, use `/plan`; in Claude Code, use Plan Mode; in other agents, use an equivalent read-only planning mode. This loop does not create a new workflow authority, approve PRDs, rank Candidate Queue items for implementation, activate beads, update `tasks/todo.md`, authorize implementation, or code.

Keep student-facing workflow selection subordinate to the document-role split: README is the public compass, Guided Setup is setup-only, Daily Cockpit is the operating home, User Guide is the annex, How-To is the educational bridge, Troubleshooting is symptom lookup, Ask Precode and Artifact Chooser are conditional helpers, and Release Readiness is release-prep rather than deployment automation.

If the user asks for the Workflow Selection Skill, a "Precode skill", or a "skill-style workflow," use `tasks/reference/SKILL-PLAYBOOK-PROTOCOL.md` to keep the skill as a read-only prompt playbook. Stable documentation questions should route to Ask Precode. Current-state or next-work questions should route through Workflow Selection, Session Start, Troubleshooting, or the relevant owner workflow.

Active memory remains exactly:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

## Workflow Decision Path

When broad durable intent is present, check whether a reviewed Goal Frame exists before choosing a workflow:

```text
broad user intent -> Goal Frame proposal/reaffirmation -> workflow selection -> intake / PRD / decomposition / bead / review
```

Goal Frames are advisory orientation only. A stale, missing, or conflicting Goal Frame should trigger a reaffirmation prompt before workflow guidance.

Choose the workflow that matches the current situation:

| Current situation | Recommended workflow | Next artifact |
|---|---|---|
| User asks a stable PrecodeOS documentation question or asks where to find guidance | Ask Precode Docs Skill | cited docs/protocol answer |
| User asks for a product roadmap, backlog-like list, parked ideas, future candidate review, candidate ranking, product-value rating, theme grouping, or near-bead sketching without active work | Candidate Queue Protocol | `CANDIDATE-QUEUE.md` entry, Candidate Queue review, or approved `scripts/candidate-queue.py` preview/apply action |
| User asks to develop an idea or feature angle into future candidate work before implementation | Plan Mode Candidate Craft Loop | Plan Packet first, then reviewed Candidate Queue entry only if the user approves candidate capture |
| First-time non-technical builder has a rough idea before repo setup or asks for First PRD Walkthrough | First PRD Walkthrough | Product Brief, then reviewed Conviction Packet evidence with Local Source Intake readiness self-check, then reviewed intake summary before PRD shaping |
| Reviewed Conviction Packet is ready to enter Precode | Local Source Intake | reviewed source summary and next safe Precode workflow |
| PrecodeOS adoption target already has app code, docs, CI, product history, or active work | Existing Repo Intake | read-only repo intake evidence and setup/adaptation path |
| Broad, risky, market-facing, paid, evidence-poor, or solution-first idea where worth-building uncertainty blocks the First PRD path | Product Discovery Validation inside or before First PRD Walkthrough | Discovery Summary with `proceed | pause | narrow | kill` recommendation |
| Scattered notes, screenshots, research, chat summary, or issue export for an existing Precode project | Local Source Intake | reviewed source summary |
| User explicitly asks to explore a feature angle after intake or PRD shaping but before committing to PRD amendment, Architecture Shaping, Decomposition, candidate bead proposal, or activation | Plan Loop in Plan Mode | Plan Packet |
| User selects a Candidate Queue entry and asks for an implementation plan | Plan Mode Candidate Craft Loop, then the owner workflow | Implementation plan draft only; no activation before PRD/authority/decomposition approval |
| Shaped idea that still needs product clarity | Idea-to-PRD / PRFAQ-lite | PRD shard draft |
| Approved PRD with stable requirement IDs and no material architecture risk | Decomposition Protocol | candidate bead proposals |
| Approved PRD with auth, data, API, integration, dependency, migration, workflow, or multi-system risk | Architecture Shaping Protocol | Architecture Brief evidence before bead proposals |
| High-risk, uncertain, or challenge-worthy idea | PRFAQ/challenge planning bead | questions, risk notes, or narrowed proposal |
| User is unsure whether accessibility review is needed for a bead, review, or release candidate | Accessibility Advisor Fit Interview | recommendation to invoke advisor, not needed, or defer |
| Bug, refactor, setup, review, external integration, manual dashboard work, or blocked work | matching bead template | narrow bead proposal |
| Completed, messy, or disputed work | review, closeout, state repair, or unblocker flow | recorded evidence, review decision, or repair bead |
| User asks for Workflow Selection Skill or another current-state skill-style workflow | Skill Playbook Protocol plus the owner workflow | read-only prompt-playbook output |

When the recommended workflow is a bead proposal, use the bead kind menu in `tasks/beads/BEAD-SCHEMA.md` to explain the work shape in beginner-readable terms: intake, shaping, implementation, repair, refactor, setup/integration, unblocker, or review. The menu is guidance only. It does not choose work, approve PRDs, activate beads, add new schema authority, or override the Bead Decomposition Test.

If no row fits, stop and name what is missing: source evidence, product definition, authority owner, decomposition, verification path, approval gate, or state repair.

If the workflow involves sensitive, external, destructive, or `bounded-afk` execution, the next bead proposal should include a Run Contract or explicitly explain why one is not needed. Use plain output language: Allowed actions, Proof needed, Approval required before, and Stop if.

Use Product Discovery Interview Skill with `tasks/reference/PRODUCT-DISCOVERY-VALIDATION-PROTOCOL.md` before PRD shaping when the main uncertainty is whether the user problem, current workaround, demand signal, alternative, or smallest learning step is real enough to justify product definition. Its Discovery Summary is evidence only; it may recommend `proceed`, `pause`, `narrow`, or `kill`, but it does not approve a PRD, activate beads, choose work, or rewrite owner files.

Do not route a Conviction Packet directly to PRD drafting unless Local Source Intake has summarized the reviewed packet and the builder has reviewed the intake. Before intake, the packet should pass only a compact self-check for user, painful moment, current workaround or evidence, hypothesis or learning target, strongest evidence, weakest assumption, first slice, not-yet scope, sensitive surfaces, and next safe Precode path. That self-check is advisory; it is not PRD approval, owner-file promotion, task selection, bead activation, or coding permission.

First PRD Walkthrough is the beginner-facing name for this rough-idea-to-PRD-readiness route. Product Ideation Workbook, Precode Idea Coach, Product Brief, Challenge And Clarity, Conviction Packet, Local Source Intake, and PRD shaping are steps inside that route, not competing commands for the same moment. It does not create a new workflow authority, approve PRDs, compile features, create or activate beads, choose tasks, create a roadmap or backlog, mutate owner files, or authorize implementation.

Use `tasks/reference/EXISTING-REPO-INTAKE-PROTOCOL.md` after Bootstrap Confidence and before setup mutation when adopting PrecodeOS into an existing app. Its report is evidence only; it does not approve copying, owner-file adaptation, check execution, PRD approval, bead activation, or app-code edits.

## Workflow Selection Output

When asked to choose a workflow, return:

- Current situation:
- Recommended workflow:
- Artifact to produce next:
- Required authority source:
- User approval needed:
- Run contract needed:
- Stop condition:
- Generated-report warning:

The output is guidance only. It does not approve a PRD, activate a bead, choose the next task, or rewrite owner files.

## Workflow Boundaries

- Local source summaries are evidence, not product authority.
- PRFAQ-lite and PRD drafts shape intent, but do not start implementation.
- Approved PRDs can propose beads, but do not activate them.
- Candidate beads must pass the Bead Decomposition Test before activation.
- Planning beads may produce planning artifacts, but should not edit app code.
- Execution beads may implement scoped work, but should not reshape product definition.
- Review and repair flows may identify follow-up work, but follow-up work becomes action only through the correct owner file or approved bead.
- Generated reports may warn about workflow drift, but must not drive task selection.

Use `tasks/reference/LONG-HORIZON-PLANNING-PROTOCOL.md` when workflow selection discovers future, deferred, blocked, follow-up, or PRD-approved work that should remain visible but non-active.

Use the Plan Mode Candidate Craft Loop when the user asks to develop candidate work or implementation-plan work from an idea, feature angle, or selected Candidate Queue entry. A Plan Packet, queue entry, or implementation plan is evidence only. It may recommend Product Discovery, Local Source Intake, PRD draft or amendment, owner-file update, Architecture Shaping, Decomposition, Candidate Queue, defer, kill, or stop, but it must not approve a PRD, create or activate beads, choose tasks, rank Candidate Queue items as implementation priority, update `tasks/todo.md`, become backlog authority, or authorize implementation.

Use Plan Loop when the user explicitly asks to explore a topic, implementation angle, feature slice, or unresolved choice before committing it to the next workflow. Use Plan Mode first when the host supports it. A Plan Packet is evidence only. It may recommend Product Discovery, PRD draft or amendment, owner-file update, Architecture Shaping, Decomposition, Candidate Queue, or stop, but it must not approve a PRD, create or activate beads, choose tasks, become backlog authority, or authorize implementation.

Use `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md` when the correct workflow is checkpoint, session close, review, handoff, or transition proposal.

Use the every-bead rhythm when the user needs a compact orientation across current work, changed behavior, proof, parked intent, approvals, and next prompt before selecting one of those workflows. If `Parked` implies future work, route to Candidate Queue, PRD amendment, decision, follow-up bead proposal, defer, or kill. If `Next` implies activation, stop and require an explicit transition proposal and user approval.

Use `tasks/reference/CANDIDATE-QUEUE-PROTOCOL.md` when the user needs a human-maintained place to capture multiple intents before they are ready for intake, discovery, PRD shaping, or decomposition. Candidate Queue review may rank candidates for review, assign product-value ratings, group themes, or sketch near-beads, but it must not choose next work or authorize implementation, approve PRDs, activate beads, mutate `tasks/todo.md`, or reserve `B###` IDs.

Use `tasks/reference/ARCHITECTURE-SHAPING-PROTOCOL.md` after PRD approval and before decomposition when workflow selection reveals auth, data model, API, integration, dependency, migration, external-service, multi-step workflow, or multi-system risk that a non-technical builder should approve or redirect before an AI coding agent derives beads.

Use `tasks/reference/SYSTEM-DESIGN-PATTERN-PROTOCOL.md` when Architecture Shaping or workflow selection reveals a feature that needs an external boundary, state flow, strategy-style rule boundary, auth/access boundary, audit trail, or a plain-English implementation-shape choice before coding.

Use `tasks/reference/GOAL-FRAME-PROTOCOL.md` when workflow selection needs durable direction but the direction should not become a backlog, roadmap, implementation plan, or active task.

Use the Accessibility Advisor Fit Interview when a user, owner file, review, or release-candidate decision raises accessibility uncertainty. The interview is opt-in and advisory. It recommends whether to invoke accessibility review for the specific bead or release candidate; it does not make accessibility review mandatory for every UI/interface change, prove accessibility, accept implementation, approve release, or claim legal compliance.

## Common Stop Conditions

Stop before work starts when:

- the problem is unclear
- no primary authority source is named
- product-feature work lacks an approved PRD or requirement IDs
- candidate work mixes planning and implementation
- the verification path is unknown
- a sensitive-surface approval gate is unresolved
- blocked work has no escape path
- generated reports or source summaries appear to be acting as authority

## Advisory Check

`scripts/workflow-check.py` is advisory. It may warn about wrong workflow fit, PRD approval gaps, approved PRDs without bead proposals, mixed planning and implementation, blocked work without an unblocker path, backlog-like active fields, or generated reports appearing to drive task selection.

Warnings are generated evidence only. They do not choose tasks, approve PRDs, activate beads, change bead state, or edit active memory.
