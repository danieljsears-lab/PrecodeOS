# PrecodeOS -- Workflow Selection Protocol
<!-- ANCHOR: workflow-selection-protocol -->

> AUTHORITY: Workflow-selection guidance for choosing the next Precode planning, execution, review, unblocker, repair, or prompt-playbook path before work starts.
> NOT_AUTHORITY: Active memory, product decisions, approved requirements, task selection, bead activation, implementation plans, generated progress state, or external mutations.
> LOAD_WHEN: Deciding which Precode workflow to use for a rough idea, local source material, PRD work, bead proposal, blocked task, review, closeout, or state repair.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.13
Last updated: 2026-06-21

## Purpose

Workflow selection helps a user or agent choose the right Precode path before starting work.

Use this protocol when the next step is unclear, when too many protocols could apply, or when an agent may be jumping from idea to implementation too quickly.

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
| User asks for a product roadmap, backlog-like list, parked ideas, future candidate review, or candidate ranking without active work | Candidate Queue Protocol | `CANDIDATE-QUEUE.md` entry or Candidate Queue review |
| First-time non-technical builder has a rough idea before repo setup | Product Ideation Workbook or Product Conviction Packet Skill | Product Brief, then Conviction Packet evidence |
| Reviewed Conviction Packet is ready to enter Precode | Local Source Intake | reviewed source summary and next safe Precode workflow |
| PrecodeOS adoption target already has app code, docs, CI, product history, or active work | Existing Repo Intake | read-only repo intake evidence and setup/adaptation path |
| Broad, risky, market-facing, paid, evidence-poor, or solution-first product idea where worth-building is uncertain | Product Discovery Interview Skill / Product Discovery Validation | Discovery Summary with `proceed | pause | narrow | kill` recommendation |
| Rough idea, scattered notes, screenshots, research, chat summary, or issue export | Local Source Intake | reviewed source summary |
| Shaped idea that still needs product clarity | Idea-to-PRD / PRFAQ-lite | PRD shard draft |
| Approved PRD with stable requirement IDs and no material architecture risk | Decomposition Protocol | candidate bead proposals |
| Approved PRD with auth, data, API, integration, dependency, migration, workflow, or multi-system risk | Architecture Shaping Protocol | Architecture Brief evidence before bead proposals |
| High-risk, uncertain, or challenge-worthy idea | PRFAQ/challenge planning bead | questions, risk notes, or narrowed proposal |
| User is unsure whether accessibility review is needed for a bead, review, or release candidate | Accessibility Advisor Fit Interview | recommendation to invoke advisor, not needed, or defer |
| Bug, refactor, setup, review, external integration, manual dashboard work, or blocked work | matching bead template | narrow bead proposal |
| Completed, messy, or disputed work | review, closeout, state repair, or unblocker flow | recorded evidence, review decision, or repair bead |
| User asks for Workflow Selection Skill or another current-state skill-style workflow | Skill Playbook Protocol plus the owner workflow | read-only prompt-playbook output |

If no row fits, stop and name what is missing: source evidence, product definition, authority owner, decomposition, verification path, approval gate, or state repair.

If the workflow involves sensitive, external, destructive, or `bounded-afk` execution, the next bead proposal should include a Run Contract or explicitly explain why one is not needed. Use plain output language: Allowed actions, Proof needed, Approval required before, and Stop if.

Use Product Discovery Interview Skill with `tasks/reference/PRODUCT-DISCOVERY-VALIDATION-PROTOCOL.md` before PRD shaping when the main uncertainty is whether the user problem, current workaround, demand signal, alternative, or smallest learning step is real enough to justify product definition. Its Discovery Summary is evidence only; it may recommend `proceed`, `pause`, `narrow`, or `kill`, but it does not approve a PRD, activate beads, choose work, or rewrite owner files.

Do not route a Conviction Packet directly to PRD drafting unless Local Source Intake has summarized the packet and the builder has reviewed the intake. The packet is pre-PRD evidence, not approval to define requirements or code.

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

Use `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md` when the correct workflow is checkpoint, session close, review, handoff, or transition proposal.

Use `tasks/reference/CANDIDATE-QUEUE-PROTOCOL.md` when the user needs a human-maintained place to capture multiple intents before they are ready for intake, discovery, PRD shaping, or decomposition. Candidate Queue review may rank candidates for review, but it must not choose next work or authorize implementation.

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
