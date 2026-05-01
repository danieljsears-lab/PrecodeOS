# Precode OS — Planning Protocol
<!-- ANCHOR: planning-protocol -->

> AUTHORITY: Experiment and rollout planning brief format for uncertain product bets, metric-backed hypotheses, exposure plans, and kill criteria.
> NOT_AUTHORITY: Feature scope, final decisions, active task selection, schema definitions, route structure, generated progress, or implementation status.
> LOAD_WHEN: Planning a product experiment, rollout, ambiguous feature bet, or user-facing behavior change whose success needs measurement.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-04-26

## Purpose

Use this protocol when the work is not merely implementation, but a product bet that needs measurable validation.

This file keeps planning disciplined without turning `FEATURES.md`, `DECISIONS.md`, or `tasks/todo.md` into experiment logs.

## Planning Brief Template

### Problem

Two sentences max. Data-backed. Name the observed pain, constraint, or opportunity.

### Hypothesis

What you believe will happen and why.

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

## Rule Of Use

- If a bead has `Verification Type: experiment`, `rollout`, or `planning brief`, it must reference this protocol.
- The four planning sections may live in the bead or in the bead's primary authority file.
- Once the experiment produces a hard decision, record the decision in `DECISIONS.md`; do not keep the decision only in the planning brief.
