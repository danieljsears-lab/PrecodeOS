# Precode PRD Shards
<!-- ANCHOR: prd-shards -->

> AUTHORITY: PRD shard directory rules, PRD states, PRD ID format, and the relationship between PRDs, `FEATURES.md`, and execution beads.
> NOT_AUTHORITY: Active task selection, route structure, schema field definitions, pricing decisions, or implementation status.
> LOAD_WHEN: Creating, reviewing, approving, or backfilling a product definition before execution beads are created.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.12
Last updated: 2026-06-23

## Purpose

This folder holds product definition shards.

A PRD shard is the durable destination document between an idea and implementation. It captures alignment/grilling results, domain language when terms matter, user problem, requirement IDs, acceptance oracles, risks, architecture-shaping evidence when risk-triggered, module/interface candidates, and journey bead proposals before an AI coding agent starts building.

When a PRD starts from `CANDIDATE-QUEUE.md`, cite the originating Candidate Queue ID in `Source Inputs`. If reviewed shaping mattered, also cite product-value rating, themes, and near-bead sketch IDs such as `CQ-001-short-name-S01`. Queue IDs and sketch IDs preserve source traceability only; a Candidate Queue citation does not approve the PRD, choose work, reserve bead IDs, or authorize implementation. Final bead IDs are assigned only when actual bead files are created.

`PRODUCT.md` is the builder-facing product constitution. Use it during PRD creation, review, approval, and amendment to check product promise, users, strategy, non-goals, current bets, success signals, and design or voice. It does not replace PRD shards or approve features.

`FEATURES.md` remains the compiled feature and functional-requirement inventory. PRD shards own the deeper requirement definition that feeds that inventory.

`tasks/prds-html/` holds generated static HTML review pages for non-template PRD shards. The HTML pages improve scanability and source navigation, and may include an export-only Acceptance Oracle Matrix cockpit that produces proposed Markdown for manual application. They are generated output. They do not approve PRDs, activate beads, choose tasks, accept implementation, write Markdown, persist browser edits, or become source truth.

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
- `Source Inputs`
- `Alignment / Grilling Summary`
- `Domain Language`
- `PRFAQ-Lite`
- `Problem`
- `User Moment`
- `Destination`
- `Product Constitution Fit`
- `Users`
- `Goals`
- `Non-Goals`
- `Requirements`
- `Acceptance Oracle Matrix`
- `Risk And Permission Model`
- `Architecture / Project Context Impact`
- `Module / Interface Candidates`
- `Agent Context Contract`
- `Anti-Shallow Checks`
- `Bead Proposals`
- `Compilation Notes`
- `Open Questions`
- `Approval`

Use `PRD-000-template.md` when creating a new shard.

## Operating Rules

- Every feature needs at least one PRD shard before coding begins.
- Ceremony is adaptive by risk. A low-risk UI copy change can have a short shard; auth, payments, data, uploads, external tools, or ambiguous workflows need a fuller shard.
- Alignment/grilling is expected for fuzzy, source-heavy, risky, or user-facing ideas before requirements are finalized.
- Domain language is expected when terms, aliases, avoid words, UI labels, tests, docs, support language, or module/interface names affect the feature. If the terms should survive beyond the PRD, propose a reviewed `project_glossary` card with source pointers, examples, freshness, and promotion owner when applicable; glossary memory remains evidence only.
- Architecture Shaping evidence is expected before bead proposals when an approved PRD touches auth, data models, APIs, integrations, dependencies, migrations, external services, multi-step workflows, or multi-system changes. If skipped, record the low-risk reason in the PRD architecture-impact section or bead notes.
- Frontmatter carries the structured PRD metadata; the section body carries the human-readable product definition.
- Check `PRODUCT.md` when feature work may affect product promise, users, strategy, non-goals, current bets, success signals, or design and voice.
- Requirement IDs are stable and granular. Use IDs such as `PRD-002-FR01`, `PRD-002-UX01`, `PRD-002-SEC01`, and `PRD-002-NFR01`.
- Acceptance Oracle Matrix expected behavior may use optional EARS-style wording such as `WHEN [condition/event] THE SYSTEM SHALL [expected behavior]` when it improves clarity. This is writing guidance only, not required PRD structure, schema enforcement, generated proof, PRD approval, implementation acceptance, or a reason to reject clear non-EARS acceptance criteria.
- Acceptance Oracle Matrix rows may include evidence lane, recorded source or evidence location, and what the proof does not cover when requirement-to-proof drift would matter. This is advisory traceability only; matrix text, generated tests, generated properties, screenshots, browser notes, AI critique, external status summaries, and generated reports are not proof without recorded checks, structured manual verification, Closeout Evidence, accepted review, or promoted follow-up evidence.
- `FEATURES.md` compiles approved PRD shards into feature inventory and functional requirements. It should not become the deep PRD itself.
- `scripts/prd-html.py` may regenerate `tasks/prds-html/*.html` from PRD shards. Generated pages may export proposed Acceptance Oracle Matrix Markdown, but canonical source changes still happen manually in `tasks/prds/*.md`. Run `python3 scripts/prd-html.py --check` when PRD source or PRD review-surface behavior changes.
- Beads cite the parent PRD and requirement IDs they implement. New bead proposals should include delegation mode, test strategy, and review context when relevant.
- Candidate Queue IDs may be included as source context in PRDs and bead proposals, but final bead IDs are assigned only when actual bead files are created.
- If a PRD changes after implementation starts, add an amendment note to the PRD and create follow-up beads rather than silently widening the active bead.
- Completed PRDs, old alignment transcripts, and closed source issues are historical evidence when current code or owner files have moved on.
- Product decisions discovered during PRD work move to `DECISIONS.md` when they become hard decisions.
- Schema, route, API, security, frontend, and acceptance details still belong to their existing authority files. PRDs may point to those files, but must not replace them.
