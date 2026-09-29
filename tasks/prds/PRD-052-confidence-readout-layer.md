---
prd_id: PRD-052
status: approved
owner: Dan Sears / Recode
created: 2026-09-29
last_updated: 2026-09-29
risk_level: low
feature_link: Confidence Readout Layer
features_status: not compiled
related_prds:
  - PRD-038
  - PRD-039
  - PRD-049
---

# PRD-052 -- Confidence Readout Layer
<!-- ANCHOR: prd-052-confidence-readout-layer -->

> AUTHORITY: Public requirements for translating existing Product Code Quality Snapshot evidence into plain-language human review cues.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, implementation acceptance, review approval, release approval, code-quality scoring, certification, generated proof, checker-gate authority, linter/test replacement, app-code analysis, or external mutation.
> LOAD_WHEN: Planning, implementing, reviewing, or validating the Confidence Readout Layer.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-09-29

## Summary

The Confidence Readout Layer translates the existing Product Code Quality Snapshot into a beginner-legible review conversation. Each cue states what was observed, what it may indicate, what remains uncertain, and what a human should ask or inspect next.

The layer is advisory evidence interpretation. It does not calculate confidence, judge code quality, or turn missing evidence into a positive result.

## Requirements

| ID | Requirement | Priority |
|---|---|---:|
| `PRD-052-FR01` | The active-bead snapshot exposes a confidence readout without removing or renaming existing snapshot fields. | P0 |
| `PRD-052-FR02` | Every readout row contains `observed`, `interpretation`, `uncertainty`, and `human_action`. | P0 |
| `PRD-052-FR03` | Missing, unavailable, or insufficient evidence is stated as unknown or insufficient; it is never treated as healthy. | P0 |
| `PRD-052-FR04` | The readout uses existing snapshot evidence only and does not run checks, parse application code, or calculate quality metrics. | P0 |
| `PRD-052-FR05` | Protocol and prompt guidance presents the readout as optional human-review support after evidence gathering. | P1 |
| `PRD-052-FR06` | Self-test and clarity coverage protect advisory-only, non-authoritative, no-score, and no-certification boundaries. | P1 |

## Acceptance Criteria

- `python3 scripts/product-code-quality-snapshot.py --self-test` verifies readout fields, insufficient-evidence handling, and non-authority boundaries.
- `python3 scripts/product-code-quality-snapshot.py --active-bead --json` preserves existing fields and emits `confidence_readout`.
- Plain output labels each row as Observed, Interpretation, Uncertainty, and Human action.
- No readout path runs linters, tests, typechecks, package managers, fixers, or app code.
- No public guidance describes the readout as a score, verdict, certificate, gate, approval, or proof of healthy code.

## Boundaries

The Product Code Quality Snapshot remains the owner surface. The readout may translate scope alignment, changed-file shape, repo-shape warnings, and missing-proof evidence into human questions. It cannot select work, activate beads, approve implementation, accept review, approve release, create generated proof, or replace project checks and human judgment.

Behavioral history signals, language-aware analysis, indentation complexity, and production-readiness concerns remain separate work and are not included in this slice.

## Candidate Bead Proposal

| Bead | Requirement IDs | Done when | Delegation mode | Test strategy | Primary authority | Validation |
|---|---|---|---|---|---|---|
| `B052-confidence-readout-layer` | `PRD-052-FR01` through `PRD-052-FR06` | Snapshot readout, protocol/prompt guidance, clarity coverage, maintainer closeout, and generated surfaces are implemented and checked. | `human_in_loop` | `static_only` | `tasks/prds/PRD-052-confidence-readout-layer.md` | snapshot self-test, clarity scenario, package/docs/PRD/roadmap checks |
