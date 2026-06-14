# Student Experience Ingestion Packet
<!-- ANCHOR: student-experience-ingestion-packet -->

> AUTHORITY: Student-facing template for packaging an approved bootcamp PRD input and Experience design artifacts before Claude Code creates a bounded Precode bead.
> NOT_AUTHORITY: Product approval, PRD approval, active task selection, implementation plan, bead activation, generated progress state, or permission to code.
> LOAD_WHEN: A bootcamp student has shaped an idea, created a visual core-spine experience in Claude Design, Ember UI Builder, or an equivalent AI-assisted UI/UX canvas, and is ready to hand context to Claude Code.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.4
Last updated: 2026-06-14

## Purpose

Use this packet after idea shaping, approved PRD-like input, and Experience design, before Claude Code starts implementation. A raw Product Brief or Conviction Packet is not enough for this step until it has gone through Local Source Intake and the bootcamp has approved the PRD-like input for Experience work.

The packet combines:

- the student-approved bootcamp PRD or PRD-like input from the first product-shaping step
- the Experience artifacts created in Claude Design, Ember UI Builder, or another AI-assisted UI/UX canvas
- the core workflow spine that should become the first coded experience
- target-user or customer feedback gathered before coding, when available

The packet helps Claude Code create one bounded Precode bead for the core spine. It does not authorize coding by itself.

Claude Code should not infer missing scope from an incomplete packet. If the handoff checklist below is incomplete, Claude should ask for the missing information and stop before creating a bead.

## Flow

```text
Student Idea-to-MVE or bootcamp PRD input
  -> design-tool brief from this packet
  -> Experience design canvas
  -> Core Spine Gate
  -> target-user feedback when feasible
  -> Student Experience Ingestion Packet
  -> Claude Code creates one Precode bead
  -> student approves the bead
  -> coding begins
  -> prototype demo and Experience review evidence
```

Support engineers may help set up the local environment and scaffold in parallel. They do not own product direction, PRD decisions, Experience artifacts, acceptance, or scope.

## Complete Before Claude Code Handoff

Before pasting this packet into Claude Code, make sure these items are filled in. If one is unknown, write `unknown` and explain what decision or evidence is missing.

- [ ] Approved bootcamp PRD or PRD-like input is named or linked.
- [ ] Design-tool brief or source notes used for the Experience artifact are included or summarized.
- [ ] Experience design tool and artifact links, paths, screenshots, or pasted summaries are included.
- [ ] Target user, problem, promise, and minimum value moment are written in plain language.
- [ ] Core spine trigger, first action, key steps, and completion moment are named.
- [ ] Included screens and states are named, including any loading, error, success, and mobile states that matter for the first coded version.
- [ ] First coded core-spine scope is separated from explicit not-yet scope.
- [ ] Open questions, risks, or sensitive surfaces are named, or marked `none known`.
- [ ] Feedback status is recorded, even if feedback is not available yet.
- [ ] Core Spine Gate status is recorded as `met`, `needs work`, or `blocked`.

Claude Code handoff rule: incomplete required fields block bead creation. Claude may ask for missing information, but it must not create a bead, update `tasks/todo.md`, activate work, or code from an incomplete packet.

## Design Canvas Input Prompt

Use this after the bootcamp PRD input is approved and before opening Claude Design, Ember UI Builder, or another AI-assisted design canvas. The goal is a rough core-spine artifact, not polished screens or extra features.

```text
Turn these idea-shaping notes and reference images into a design-tool brief.

Focus on the minimum workflow that gives the target user value.

Include:
- target user
- problem
- promise
- core workflow spine
- minimum value moment
- visual or brand references
- workflow references
- what to copy conceptually from the references
- what not to build yet

Do not add secondary features, dashboards, admin tools, or future platform ideas unless they are required for the core spine.
```

## Core Spine Review Prompt

Use this after the first rough Experience artifact exists.

```text
Review this design for core spine strength.

Can a target user complete the primary workflow and receive the minimum value?

Tell me:
- what works
- what is missing
- what is overbuilt
- what is confusing
- what should move to not-yet
- what feedback I should get from a target user before coding

Judge usefulness and clarity first, not polish.
```

## Core Spine Gate

Complete this gate before Claude Code creates or proposes a core-spine bead. This is a lightweight readiness check, not professional UX review and not product approval.

- Target user can be named in one sentence: `met | needs work | blocked`
- Trigger and first action are visible: `met | needs work | blocked`
- Key steps lead to the minimum value moment: `met | needs work | blocked`
- Feedback or confidence cues are visible enough for a first coded version: `met | needs work | blocked`
- Completion moment and return path are named: `met | needs work | blocked`
- Not-yet scope is explicit: `met | needs work | blocked`

Gate status: `met | needs work | blocked`

If the Core Spine Gate is `needs work` or `blocked`, revise the Experience artifact or packet before asking Claude Code to create a bead.

## Target-User Feedback Prompt

Use this before coding when a target user, customer, peer user, instructor, or domain-informed reviewer is available.

```text
Create five lightweight feedback questions for a target user reviewing this rough core spine.

Focus on whether they understand:
- who this is for
- what problem it helps with
- what they should do first
- where the value moment happens
- what feels confusing, untrustworthy, or unnecessary

Keep the questions short enough for a 10-minute conversation.
```

Feedback is evidence, not automatic authority. If feedback changes scope, route the change through Local Source Intake, PRD amendment, a candidate bead, or completion evidence before implementation changes.

## Packet

### Source Inputs

Approved bootcamp PRD or PRD-like input:

- 

Idea-shaping or workbook source:

- 

Experience design tool used:

- `Claude Design | Ember UI Builder | other:`

Design-tool brief used:

- 

Experience artifacts:

- 

Reference images, apps, sites, or workflow examples:

- 

### Product Context

Target user:

- 

Problem:

- 

Promise:

- 

Minimum value moment:

- 

Success signal:

- 

### Core Spine

Trigger:

- 

First action:

- 

Key steps:

- 

Feedback or confidence cues:

- 

Completion moment:

- 

Return path:

- 

### Screens And States

Screens or surfaces included:

- 

States included:

- `first-run | empty | loading | error | success | disabled | mobile | other:`

States not yet designed:

- 

Responsive or accessibility notes:

- 

### Design Direction

Brand, voice, or tone notes:

- 

Visual references to follow:

- 

Visual references to avoid:

- 

Design-system or component notes:

- 

### Scope

Included in the first coded core spine:

- 

Explicitly not included yet:

- 

Open questions:

- 

Risks or sensitive surfaces:

- 

### Feedback

Feedback gathered before coding:

- 

Who gave feedback:

- 

What changed because of feedback:

- 

Feedback not used yet and why:

- 

Feedback still needed after coded prototype:

- 

### Experience Review And Demo Evidence

Use this after the first coded prototype exists. Demo notes, screenshots, and feedback help decide the next safe step, but they do not accept the bead, approve a PRD, or prove validation by themselves.

Prototype or demo link, recording, screenshots, or notes:

- 

Minimum value moment demoed:

- 

What worked:

- 

What did not work or remains uncertain:

- 

What changed because of prototype feedback:

- 

Recommended next direction:

- `continue | narrow | pause | change direction`

Completion evidence packet needed:

- `yes | no | unknown`

## Claude Code Handoff Prompt

Paste this into Claude Code with the completed packet.

```text
Use this approved bootcamp PRD input and Student Experience Ingestion Packet to create one Precode bead for the core spine implementation.

First inspect the "Complete Before Claude Code Handoff" checklist and the packet fields.

If any required field is missing, ambiguous, or marked unknown in a way that changes implementation scope, ask me for the missing information and stop. Do not create a bead yet.

If this packet has a formal Precode PRD shard in tasks/prds/, you may draft one ready candidate bead file for the core spine. Do not update tasks/todo.md, activate the bead, or code.

If this packet only has a bootcamp-approved PRD-like input and no formal Precode PRD shard, produce a candidate bead proposal only and stop. Tell me that normal Precode intake or PRD promotion is required before activation.

In the candidate bead or proposal, summarize:
- the core scope
- the minimum value moment
- Core Spine Gate status
- files likely in play
- acceptance checks for the main workflow
- key screen states
- responsive behavior to verify
- feedback gathered before coding
- manual verification steps
- stop conditions
- what is explicitly not included

Preserve the approved PRD intent and Experience core spine.

Do not code until I approve the bead through the normal Precode workflow.
```

## Support Engineer Readiness Prompt

Use this when support is helping with environment or scaffold readiness.

```text
Check that the student's local environment and scaffold are ready for Claude Code implementation.

Do not change product scope, PRD direction, Experience artifacts, acceptance, or design direction.

Report:
- setup status
- scaffold status
- blockers
- exact next technical unblock
- anything the student must decide before implementation
```

## Guardrail Reminder

This packet is context for bead creation. It is not product approval, not a task list, not bead activation, and not permission to code.

Target-user feedback, demo notes, and Experience review notes are evidence. They do not override approved PRDs, owner files, active beads, recorded checks, or human review decisions.
