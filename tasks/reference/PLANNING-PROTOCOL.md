# PrecodeOS — Planning Protocol
<!-- ANCHOR: planning-protocol -->

> AUTHORITY: Experiment and rollout planning brief format for uncertain product bets, metric-backed hypotheses, exposure plans, and kill criteria.
> NOT_AUTHORITY: Feature scope, final decisions, active task selection, schema definitions, route structure, generated progress, or implementation status.
> LOAD_WHEN: Planning a product experiment, rollout, ambiguous feature bet, or user-facing behavior change whose success needs measurement.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.2
Last updated: 2026-06-23

## Purpose

Use this protocol when the work is not merely implementation, but a product bet that needs measurable validation.

This file keeps planning disciplined without turning `FEATURES.md`, `DECISIONS.md`, or `tasks/todo.md` into experiment logs.

Use Product Discovery Validation or Candidate Queue review before this protocol when the work is still a hunch, weak assumption, or untested hypothesis. Use this protocol only when the hypothesis is ready for metric-backed exposure, monitoring, and kill criteria.

## Planning Brief Template

### Problem

Two sentences max. Data-backed. Name the observed pain, constraint, or opportunity.

### Hypothesis

State the experiment hypothesis, not just a hunch:

- User or situation:
- Pain or current workaround:
- Expected behavior or change:
- Supporting evidence:
- Weakest assumption:
- Falsifier or what would change our mind:

If those fields are unknown, route back to Product Discovery Validation, Local Source Intake, Candidate Queue review, or a smallest learning step before planning a rollout.

### Success Metrics

Specific thresholds, not vibes.

Examples:
- Notification mute rate drops >=15% versus control.
- Registration completion rate increases from 62% to >=70%.
- Race director listing completion time drops >=20%.

### Rollout

Exposure percentage, duration, monitoring plan, and kill criteria.

Example:
- Start at 10% of eligible traffic for 7 days.
- Expand to 50% only if no severity-1 support tickets occur and conversion is non-negative versus control.
- Kill if checkout completion drops >=3%, support tickets rise >=10%, or error rate exceeds 1%.

### Learning Review

After the planned exposure or learning step, summarize the review before promoting any conclusion:

- Hypothesis review status: `untested | tested | narrowed | killed | promoted | stale | not applicable`
- Learning outcome:
- Evidence reviewed:
- Stale or untested signals:
- Decision needed:
- Recommended next Precode workflow:

Use `tasks/reference/HYPOTHESIS-REVIEW-PROTOCOL.md` when the user asks what was learned or whether the hypothesis should proceed, narrow, pause, die, or move into an owner file. If the experiment produces a hard product, technical, rollout, or operating decision, record it in `DECISIONS.md`; do not keep the decision only in the planning brief.

## Rule Of Use

- If a bead has `Verification Type: experiment`, `rollout`, or `planning brief`, it must reference this protocol.
- The four planning sections may live in the bead or in the bead's primary authority file.
- Once the experiment produces a hard decision, record the decision in `DECISIONS.md`; do not keep the decision only in the planning brief.
- A planning brief does not approve a PRD, activate beads, select tasks, or make generated metrics authoritative by itself.
