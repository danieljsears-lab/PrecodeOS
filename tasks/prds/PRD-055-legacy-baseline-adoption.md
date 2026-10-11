---
prd_id: PRD-055
status: approved
owner: Dan Sears / Recode
created: 2026-10-02
last_updated: 2026-10-02
risk_level: high
feature_link: Legacy Package Baseline Adoption
features_status: not compiled
related_prds:
  - PRD-016
  - PRD-041
---

Creator: Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-10-11

# PRD-055 -- Legacy Package Baseline Adoption
<!-- ANCHOR: prd-055-legacy-baseline-adoption -->

> AUTHORITY: Public requirements for supervised first-baseline adoption on older PrecodeOS installs.
> NOT_AUTHORITY: Historical proof, automatic migration, update permission, package-manager behavior, rollback automation, or approval of target changes.
> LOAD_WHEN: Reviewing or validating a missing-baseline path for an older PrecodeOS install.
> CLASS: prd

## Intent

Older installs created before persistent package baselines need a truthful path to establish present-state provenance without treating Git cleanliness or byte comparison as historical proof.

## Requirements

| Requirement | Behavior | Priority |
|---|---|---:|
| PRD-055-FR01 | Preview classifies every existing package-owned target path as current, missing, dirty, or eligible for explicit present-state adoption. | P0 |
| PRD-055-FR02 | Preview is read-only and generated output is evidence, not permission. | P0 |
| PRD-055-FR03 | Apply requires explicit approval for the complete eligible package-file set and a non-trivial operator attestation. | P0 |
| PRD-055-FR04 | Apply revalidates target hashes before writing `.precode/package-baseline.json` and records the attestation as adoption metadata. | P0 |
| PRD-055-FR05 | Missing, dirty, changed-after-preview, and ambiguous paths remain blocked; no automatic inference is permitted. | P0 |

The attestation accepts the inspected present state only. It does not establish that the older install was historically pristine.
