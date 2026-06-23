---
bead_id: B001
status: review
execution_mode: builder
bead_kind: planning
primary_authority: tasks/reference/UBIQUITOUS-LANGUAGE-PROTOCOL.md
depends_on:
  - B000
parent_prd: none
requirement_ids: []
files_in_play:
  - tasks/reference/UBIQUITOUS-LANGUAGE-PROTOCOL.md
  - tasks/reference/MEMORY-PROTOCOL.md
  - tasks/reference/PROMPT-PATTERNS.md
  - tasks/reference/PRD-PROTOCOL.md
  - tasks/prds/PRD-SHARD-SCHEMA.md
  - memory/cards/MEMORY-CARD-FORMAT.md
  - memory/cards/MEMORY-CARD-template.md
  - scripts/os_compiler.py
  - scripts/memory-check.py
  - scripts/precode_outputs.py
  - scripts/clarity-scenario-check.py
  - docs/PRECODE-USER-GUIDE.md
  - docs/HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md
  - docs/PRECODE-ARCHITECTURE-OVERVIEW.md
  - docs/PRECODE-PACKAGE-FILE-INVENTORY.md
  - docs-html
  - _maintainer/CHANGELOG.md
  - _maintainer/PRECODE-ROADMAP.md
  - _maintainer/PRECODE-ROADMAP-JOURNAL.md
  - _maintainer/PRECODE-ROADMAP.html
checks:
  - python3 scripts/memory-check.py --self-test
  - python3 scripts/clarity-scenario-check.py
  - python3 scripts/docs-html.py --check
  - python3 _maintainer/scripts/roadmap-html.py --check
  - python3 scripts/file-inventory.py --check
verification_type:
  - static
  - manual
delegation_mode: human_in_loop
test_strategy: characterization
review_context: same_session_ok
complexity: standard
required_planning_depth: brief
autonomy_level: supervised
---

# B001 - Ubiquitous Language / Glossary Hardening
<!-- ANCHOR: b001-ubiquitous-language-glossary-hardening -->

> AUTHORITY: Package-maintenance bead for hardening PrecodeOS glossary and shared-language guidance.
> NOT_AUTHORITY: Active memory, product decisions, PRD approval, bead activation, generated progress, owner-file promotion, or implementation acceptance.
> LOAD_WHEN: Implementing the maintainer roadmap candidate named `Ubiquitous Language / Glossary Hardening`.
> CLASS: active-task

Creator: Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-23

## State

- ID: `B001`
- Status: `review`
- Execution mode: `builder`
- Bead kind: `planning`

## Primary Authority

- `tasks/reference/UBIQUITOUS-LANGUAGE-PROTOCOL.md`

## Depends On

- `B000`

## Parent PRD

- none

## Requirement IDs

- none

## Objective

Harden the existing ubiquitous-language and project-glossary workflow so reviewed glossary cards, PRD Domain Language, naming review, memory search, and generated memory indexes use one consistent evidence-only contract.

## Done When

- The Ubiquitous Language Protocol defines the glossary review shape, stale/superseded handling, promotion owner expectations, and naming-review flow.
- The Memory Protocol and memory card template/format describe the same `project_glossary` shape and evidence-only promotion rules.
- Existing memory scripts warn on weak glossary cards, preserve selective recall behavior, and surface glossary terms clearly in generated memory indexes.
- Public docs and prompt surfaces point users to the hardened workflow without creating a new command, registry, backend, active-memory file, or automatic promotion path.
- Maintainer changelog, roadmap, roadmap journal, generated docs HTML, and private roadmap HTML are refreshed as needed.

## Files In Play

- `tasks/reference/UBIQUITOUS-LANGUAGE-PROTOCOL.md`
- `tasks/reference/MEMORY-PROTOCOL.md`
- `tasks/reference/PROMPT-PATTERNS.md`
- `tasks/reference/PRD-PROTOCOL.md`
- `tasks/prds/PRD-SHARD-SCHEMA.md`
- `memory/cards/MEMORY-CARD-FORMAT.md`
- `memory/cards/MEMORY-CARD-template.md`
- `scripts/os_compiler.py`
- `scripts/memory-check.py`
- `scripts/precode_outputs.py`
- `scripts/clarity-scenario-check.py`
- `docs/PRECODE-USER-GUIDE.md`
- `docs/HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md`
- `docs/PRECODE-ARCHITECTURE-OVERVIEW.md`
- `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`
- `docs-html`
- `_maintainer/CHANGELOG.md`
- `_maintainer/PRECODE-ROADMAP.md`
- `_maintainer/PRECODE-ROADMAP-JOURNAL.md`
- `_maintainer/PRECODE-ROADMAP.html`

## Checks

- `python3 scripts/memory-check.py --self-test`
- `python3 scripts/clarity-scenario-check.py`
- `python3 scripts/docs-html.py --check`
- `python3 _maintainer/scripts/roadmap-html.py --check`
- `python3 scripts/file-inventory.py --check`

## Verification Type

- static
- manual

## Delegation Mode

- `human_in_loop`

## Test Strategy

- `characterization`

## Review Context

- `same_session_ok`

## Stop If

- Glossary cards start replacing active memory, current code, active beads, approved PRDs, or owner files.
- The implementation implies automatic owner-file promotion, task selection, PRD approval, bead activation, or review acceptance.
- The implementation needs a new registry, backend, command wrapper, optional pack, package-manager behavior, or external mutation.
- Existing dirty Candidate Queue or Plan Loop work would need to be reverted or overwritten.

## Closeout Evidence

- Checks run: `python3 scripts/memory-check.py --self-test` -> pass; `python3 scripts/clarity-scenario-check.py` -> pass with 133 scenarios; `python3 scripts/docs-html.py --check` -> pass; `python3 _maintainer/scripts/roadmap-html.py --check` -> pass; `python3 scripts/file-inventory.py --check` -> pass.
- Evidence source: direct local command output in this implementation session.
- Result: implemented as a package-maintenance hardening pass.
- Manual verification: Who checked: Codex. What was checked: reviewed glossary protocol, memory protocol, card format/template, memory script changes, generated memory-index rendering, public guidance, package inventory, maintainer changelog, roadmap/journal history, and generated docs/roadmap freshness. Environment: local repository root `/Users/danielsears/Projects/precode-os` on 2026-06-23. Result: pass. Remaining uncertainty: existing unrelated Candidate Queue, Plan Loop, and Hypothesis work remains in the dirty worktree and was preserved rather than separated.
- Files changed: glossary protocol, memory protocol, memory card template/format, memory compiler/search/render scripts, prompt/PRD/user/architecture/package docs, generated docs HTML, maintainer roadmap/journal/changelog, and this bead.
- Next bead: none
- Review decision: pending maintainer review; this bead is not activated by its existence.
- Drift observed: none in the glossary scope; unrelated dirty work was preserved.
- Lesson to promote: none
- Follow-up bead needed: not needed unless real glossary/naming drift shows the prompt/protocol/checker surface is insufficient.
- Blocked escape: not needed.
- Reference follow-through: resolved; public docs, protocol surfaces, package inventory, generated docs HTML, maintainer changelog, roadmap, roadmap journal, and private roadmap HTML were reviewed or refreshed.

## Handback

- Package-maintenance bead created for the glossary hardening candidate.
- Do not treat this bead file as active without an explicit transition approval in a normal Precode session.
