# Precode OS — Product Constitution Template
<!-- ANCHOR: product-constitution -->

> AUTHORITY: Builder-facing product constitution, product promise, users and jobs, strategy and non-goals, current product bets, success signals, and design or voice pointers for the target project.
> NOT_AUTHORITY: Active memory, active task selection, feature approval, detailed feature requirements, route structure, schema field definitions, implementation plans, execution status, pricing decisions, or generated progress state.
> LOAD_WHEN: Starting product planning, shaping or approving a PRD shard, checking whether a new idea fits the product, reviewing product drift, or onboarding a builder to the product's current direction.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.1
Last updated: 2026-05-08

## Purpose

`PRODUCT.md` is the living product constitution.

It helps a non-technical builder and an AI coding agent stay aligned on what the product is, who it serves, what matters now, and what should not drift.

This file is reference only. It is not active memory.

Active memory remains exactly:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

Use this file to orient product planning. Do not use it to approve work, activate beads, or replace feature PRDs.

## How To Use This File

Load this file when:

- a rough idea needs product framing
- a PRD is being created, reviewed, approved, or amended
- an agent needs to check whether a suggestion fits the product direction
- strategy, users, success signals, design direction, or non-goals may have changed

Do not load this file when:

- the active bead is narrow and its primary authority is sufficient
- the question belongs in `PROJECT-CONTEXT.md`, `ARCHITECTURE.md`, `API.md`, `DATA-MODELS.md`, `SECURITY.md`, or another specific authority file
- the agent is only running checks, recording evidence, or closing an already-scoped bead

## Product Promise

Answer in plain language.

- Product:
- Who it is for:
- What it helps them do:
- Why this matters:
- One-sentence promise:

## Users And Jobs

Name the people and jobs that should shape product judgment.

| User or role | Job to be done | Pain or constraint | Language they use |
|---|---|---|---|
| Primary user |  |  |  |

## Strategy And Non-Goals

Keep this section short and sharp. It protects against agent drift.

- North star:
- Current product thesis:
- Explicit non-bets:
- Things agents should not suggest by default:
- Product decisions to preserve:

Product decisions that are hard decisions belong in `DECISIONS.md`. Link them here instead of duplicating the full decision.

## Current Bets

Use this as product orientation, not active task selection.

| Bet or theme | State | Source PRD or feature link | Notes |
|---|---|---|---|
|  | exploring |  |  |

Allowed states:

- `exploring`
- `drafting_prd`
- `approved`
- `building`
- `shipped`
- `paused`
- `deferred`

Active work is controlled by `tasks/todo.md`, not this table.

## Goal Frame

Use this only when a product-level arc needs durable orientation before workflow selection. See `tasks/reference/GOAL-FRAME-PROTOCOL.md`.

- Status: `draft`
- Last reaffirmed:
- Owner file: `PRODUCT.md`
- Horizon: `product`
- Workflow guidance:
- Goal:
- Why now:
- Success signal:
- Out of scope:
- Approval gates:
- Reaffirmation trigger:

## Success Signals

Define what good looks like without forcing every idea into a metric dashboard.

- North-star signal:
- Supporting signals:
- Qualitative evidence:
- Good enough for now:
- Signals that would change direction:

Feature-level acceptance criteria belong in PRD shards and `ACCEPTANCE.md`.

## Design And Voice Links

Capture enough taste and interface direction to prevent generic output.

- Design principles:
- Voice and tone:
- Accessibility or usability expectations:
- Design files, screenshots, or references:
- Components, tokens, or patterns:
- Things the product should not feel like:

Implementation conventions and design-system mechanics belong in `PROJECT-CONTEXT.md`, `CODEBASE-GUIDE.md`, or the target project's design authority file.

## Linked Owner Files

Use links instead of copying deep detail into this file.

- Feature inventory: `FEATURES.md`
- Product decisions: `DECISIONS.md`
- Technical project constitution: `PROJECT-CONTEXT.md`
- Feature PRDs: `tasks/prds/`
- Acceptance criteria: `ACCEPTANCE.md`
- Architecture: `ARCHITECTURE.md`
- API boundaries: `API.md`
- Data models: `DATA-MODELS.md`
- Security and privacy: `SECURITY.md`

## Living Update Check

At session close, PRD approval, or PRD amendment, ask:

- Did the product promise change?
- Did the target user or job change?
- Did a non-goal become a goal, or a goal become a non-goal?
- Did a current bet change state?
- Did success signals change?
- Did design or voice direction change?

If yes, update this file or link to the owner file where the durable fact belongs.

Do not update this file from generated reports, chat summaries, screenshots, or imported notes until the builder has reviewed the conclusion.
