# Student Experience Ingestion Packet
<!-- ANCHOR: student-experience-ingestion-packet -->

> AUTHORITY: Student-facing template for packaging an approved bootcamp PRD input and Experience design artifacts before Claude Code creates a bounded Precode bead.
> NOT_AUTHORITY: Product approval, PRD approval, active task selection, implementation plan, bead activation, generated progress state, or permission to code.
> LOAD_WHEN: A bootcamp student has shaped an idea, created a visual core-spine experience in Claude Design, Ember UI Builder, or an equivalent AI-assisted UI/UX canvas, and is ready to hand context to Claude Code.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-05-30

## Purpose

Use this packet after idea shaping and Experience design, before Claude Code starts implementation.

The packet combines:

- the student-approved bootcamp PRD or PRD-like input from the first product-shaping step
- the Experience artifacts created in Claude Design, Ember UI Builder, or another AI-assisted UI/UX canvas
- the core workflow spine that should become the first coded experience
- target-user or customer feedback gathered before coding, when available

The packet helps Claude Code create one bounded Precode bead for the core spine. It does not authorize coding by itself.

## Flow

```text
Student Idea-to-MVE or bootcamp PRD input
  -> Experience design canvas
  -> core spine review
  -> target-user feedback when feasible
  -> Student Experience Ingestion Packet
  -> Claude Code creates one Precode bead
  -> student approves the bead
  -> coding begins
```

Support engineers may help set up the local environment and scaffold in parallel. They do not own product direction, PRD decisions, Experience artifacts, acceptance, or scope.

## Design Canvas Input Prompt

Use this before opening Claude Design, Ember UI Builder, or another AI-assisted design canvas.

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

## Packet

### Source Inputs

Approved bootcamp PRD or PRD-like input:

- 

Idea-shaping or workbook source:

- 

Experience design tool used:

- `Claude Design | Ember UI Builder | other:`

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

Feedback still needed after coded prototype:

- 

## Claude Code Handoff Prompt

Paste this into Claude Code with the completed packet.

```text
Use this approved bootcamp PRD input and Student Experience Ingestion Packet to create one Precode bead for the core spine implementation.

Summarize:
- the core scope
- the minimum value moment
- files likely in play
- acceptance checks for the main workflow
- key screen states
- responsive behavior to verify
- manual verification steps
- stop conditions
- what is explicitly not included

Preserve the approved PRD intent and Experience core spine.

Do not code until I approve the bead.
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
