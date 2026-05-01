# Precode PRD Shards
<!-- ANCHOR: prd-shards -->

> AUTHORITY: PRD shard directory rules, PRD states, PRD ID format, and the relationship between PRDs, `FEATURES.md`, and execution beads.
> NOT_AUTHORITY: Active task selection, route structure, schema field definitions, pricing decisions, or implementation status.
> LOAD_WHEN: Creating, reviewing, approving, or backfilling a product definition before execution beads are created.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-04-26

## Purpose

This folder holds product definition shards.

A PRD shard is the durable definition gate between an idea and implementation. It captures the user problem, requirement IDs, acceptance oracles, risks, and bead proposals before an AI coding agent starts building.

`FEATURES.md` remains the compiled feature and functional-requirement inventory. PRD shards own the deeper requirement definition that feeds that inventory.

## File Naming

Use this pattern:

```text
PRD-###-short-name.md
```

Examples:

```text
PRD-001-auth-role-onboarding.md
PRD-002-race-discovery-search.md
PRD-003-registration-flow.md
```

Keep IDs stable. Do not renumber PRDs after beads or feature requirements reference them.

## PRD States

- `draft` — definition is being shaped.
- `needs_info` — blocked on a product decision, risk answer, or missing evidence.
- `approved` — clear enough to compile into `FEATURES.md` and split into beads.
- `superseded` — replaced by another PRD shard or hard decision.

Only an `approved` PRD may be used as the source for new implementation beads.

## Required Frontmatter Keys

- `prd_id`
- `status`
- `owner`
- `risk_level`
- `feature_link`
- `features_status`
- `related_prds`

Use frontmatter for the highest-churn PRD metadata so PRD state can compile cleanly into `FEATURES.md` and bead planning without turning the whole shard into machine-targeted prose.

## Required PRD Sections

- `State`
- `Feature Link`
- `Problem`
- `Users`
- `Goals`
- `Non-Goals`
- `Requirements`
- `Acceptance Oracle Matrix`
- `Risk And Permission Model`
- `Agent Context Contract`
- `Bead Proposals`
- `Compilation Notes`
- `Open Questions`
- `Approval`

Use `PRD-000-template.md` when creating a new shard.

## Operating Rules

- Every feature needs at least one PRD shard before coding begins.
- Ceremony is adaptive by risk. A low-risk UI copy change can have a short shard; auth, payments, data, uploads, external tools, or ambiguous workflows need a fuller shard.
- Frontmatter carries the structured PRD metadata; the section body carries the human-readable product definition.
- Requirement IDs are stable and granular. Use IDs such as `PRD-002-FR01`, `PRD-002-UX01`, `PRD-002-SEC01`, and `PRD-002-NFR01`.
- `FEATURES.md` compiles approved PRD shards into feature inventory and functional requirements. It should not become the deep PRD itself.
- Beads cite the parent PRD and requirement IDs they implement.
- If a PRD changes after implementation starts, add an amendment note to the PRD and create follow-up beads rather than silently widening the active bead.
- Product decisions discovered during PRD work move to `DECISIONS.md` when they become hard decisions.
- Schema, route, API, security, frontend, and acceptance details still belong to their existing authority files. PRDs may point to those files, but must not replace them.
