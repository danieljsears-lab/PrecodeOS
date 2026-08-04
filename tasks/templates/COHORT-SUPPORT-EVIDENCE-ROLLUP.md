# Cohort/Support Evidence Rollup
<!-- ANCHOR: cohort-support-evidence-rollup -->

> AUTHORITY: Reusable public-safe template for summarizing repeated patterns across explicit cohort/support usage-evidence packets.
> NOT_AUTHORITY: Product validation, adoption proof, support case records, grading policy, contributor scoring, productivity ranking, roadmap selection, task selection, PRD approval, bead activation, implementation acceptance, telemetry authorization, external submission, generated proof, or maintainer review.
> LOAD_WHEN: A support helper, instructor, or maintainer has multiple reviewed Builder Completion Evidence Packets or Sanitized Submitted Evidence Packets and needs a compact pattern review.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-08-04

## Purpose

Use this rollup only after explicit packet files exist.

The rollup helps compare repeated setup, docs, prompt, support-intervention, and builder-control signals without turning cohort or support evidence into analytics, grading, adoption proof, support records, or automatic roadmap direction.

You may copy summarized output from:

```bash
python3 scripts/cohort-support-evidence-rollup.py --packet <packet-file>
```

or, through the optional local facade:

```bash
precode cohort-support-rollup --packet <packet-file>
```

Use the setup-specific lens only when the review is about setup/support friction after fast verified setup, setup diagnosis, or support refresh sessions:

```bash
python3 scripts/cohort-support-evidence-rollup.py --setup-friction --packet <packet-file>
precode cohort-support-rollup --setup-friction --packet <packet-file>
```

The helper reads only packet files named with `--packet` or `--glob`. It does not scan the repo by default, write this template, submit evidence, create issues, collect telemetry, store identity, score people, approve work, or mutate external systems.

## Rollup

Rollup date:

Prepared by:

Packet files reviewed:

Packet volume: `sufficient for pattern review | unknown / insufficient packet volume`

### Repeated Patterns

- Setup or refresh friction:
- Setup source/target clarity:
- Setup target kind:
- Missing reusable setup support files:
- Setup approval latency or blocker:
- Setup command sequence confusion:
- Setup validation failure:
- Prepared support artifact used:
- Setup next safe route:
- Confusing docs, prompts, commands, or templates:
- Support intervention types:
- What Precode helped builders control:
- What remained unclear or too heavy:
- Checks or generated evidence reviewed:

### Evidence Gaps

- Unknown because not logged:
- Packet fields missing or too sparse:
- Redaction questions:
- Evidence that should not be interpreted yet:

### Interpretation Notes

- What this evidence may support:
- What this evidence does not prove:
- Potential owner surfaces for reviewed follow-up:
- Next safe maintainer/support action:

## Boundary

This rollup is source evidence only. It does not prove adoption, validate a product, create support case records, grade builders, score contributors, rank productivity, select roadmap work, approve PRDs, activate beads, accept implementation, authorize telemetry, submit evidence, or replace maintainer review.
