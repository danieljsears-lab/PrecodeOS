# Builder Completion Evidence Packet
<!-- ANCHOR: builder-completion-evidence-packet -->

> AUTHORITY: Reusable builder-facing template for capturing lightweight cohort completion evidence across Discovery, Scope, Ownership, and Proof gates.
> NOT_AUTHORITY: Product decisions, grading policy, PRD approval, implementation acceptance, active task selection, user validation, instructor judgment, support case records, or generated progress state.
> LOAD_WHEN: A builder, instructor, mentor, or support engineer needs a short public-safe completion snapshot for a cohort, workshop, demo, or prototype handoff.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.1
Last updated: 2026-06-14

## Purpose

Use this packet when a builder is finishing, demoing, or handing off a prototype in a guided cohort.

The packet helps the builder, instructor, and support engineer see the same progress snapshot without inventing a new format. It is evidence, not authority. It does not prove the idea is validated, approve a PRD, accept implementation work, or replace builder-owned product decisions.

Keep it short. Good evidence can come from normal cohort work: builder checkouts, instructor notes, support unblocking notes, prototype demos, recorded checks, screenshots, or final reflections.

## Safety Rules

Do not paste:

- secrets, tokens, passwords, API keys, or credentials
- dashboard values, billing details, payment data, or private customer data
- private raw transcripts unless everyone involved is comfortable sharing them
- sensitive personal data
- production configuration values

Use safe placeholders when needed:

```text
The app uses authentication, but no keys, dashboard values, or private account data are included here.
```

## Packet

Builder:

Project or prototype name:

Date:

Instructor or reviewer:

Support engineer, if involved:

Prototype link, repo, screen recording, or demo notes:

### One-Sentence Summary

What did you build, for whom, and what useful moment does it support?

-

### Gate 1: Discovery

Can the builder explain the problem, user, current workaround or evidence, and weakest assumption in plain language?

- Intended user:
- Painful before moment:
- Current workaround or evidence:
- Weakest assumption:
- Discovery evidence used:

Gate status: `met | needs work | blocked`

### Gate 2: Scope

Can the builder name the first useful slice and at least one explicit non-goal?

- First useful slice:
- What this version does:
- Non-goals or not-yet items:
- Scope tradeoff the builder chose:

Gate status: `met | needs work | blocked`

### Gate 3: Ownership

Did instructors coach and support engineers unblock while the builder owned product choices, approvals, acceptance, and risk decisions?

- Product decisions the builder made:
- Approvals or acceptance calls the builder made:
- Instructor help received:
- Support engineer help received:
- Risk, privacy, auth, payment, deployment, or data decisions the builder owned:

Gate status: `met | needs work | blocked`

### Gate 4: Proof

Was the prototype demoed or verified, and can the builder explain what evidence supports continuing, narrowing, pausing, or changing direction?

- What was demoed or verified:
- How it was checked:
- Minimum value moment observed:
- Target-user or reviewer feedback:
- What worked:
- What did not work or remains uncertain:
- What changed because of feedback:
- Evidence supporting the next direction:

Recommended next direction: `continue | narrow | pause | change direction`

Gate status: `met | needs work | blocked`

### Experience Review Notes

Use this section when the project used a Builder Experience Ingestion Packet or visual Experience artifacts.

- Core Spine Gate status before coding: `met | needs work | blocked | not used`
- Experience artifact or packet used:
- Prototype demo evidence:
- Did the demo show the minimum value moment? `yes | no | unclear`
- Feedback still needed:

These notes are evidence only. They do not accept implementation work, approve product changes, or replace the normal Precode review decision.

## Completion Snapshot

Overall packet status: `complete | incomplete | blocked`

Strongest evidence:

-

Biggest remaining uncertainty:

-

Next safe step:

-

Builder acceptance note:

```text
I understand what this prototype does and does not prove. I own the product decisions, scope choices, acceptance call, and next direction described in this packet.
```
