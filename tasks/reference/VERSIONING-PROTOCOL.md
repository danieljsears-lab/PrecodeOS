# Precode OS -- Versioning Protocol
<!-- ANCHOR: versioning-protocol -->

> AUTHORITY: Version metadata rules for Precode OS-owned authority docs, reference docs, templates, adapters, shims, maintained scripts, and workflow configuration.
> NOT_AUTHORITY: Active memory content, product decisions, task selection, bead state, generated report freshness, implementation status, or release management outside this repo.
> LOAD_WHEN: Adding, changing, reviewing, or auditing Precode OS-owned files that should carry visible version metadata.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.1
Last updated: 2026-05-07

## Purpose

Versioning makes Precode OS files easier to audit, teach, fork, and compare across projects.

Version metadata is descriptive. It does not make a file active memory, choose tasks, approve transitions, or replace the authority contract.

## Files That Must Be Versioned

Version these Precode OS-owned files:

- active memory: `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`
- root reference docs such as `README.md`, `PROJECT-CONTEXT.md`, `FEATURES.md`, `ARCHITECTURE.md`, `API.md`, `SECURITY.md`, and related OS-owned reference files
- task docs under `tasks/reference/`, `tasks/beads/`, and `tasks/prds/`
- adapters, shims, and mode docs under `adapters/`, `modes/`, and tool-discovery shim files
- maintained scripts under `scripts/`
- workflow configuration under `.github/workflows/`
- non-generated evidence taxonomy docs such as `logs/LOG-EVIDENCE-TAXONOMY.md`

## Generated Output Exclusions

Do not manually version generated outputs:

- `OS-HEALTH.md`
- `PROGRESS.md`
- generated markdown under `logs/`, except `logs/LOG-EVIDENCE-TAXONOMY.md`
- generated JSON and JSONL under `logs/`

Generated outputs use timestamps, authority demotion, and regeneration commands instead of manual document versions.

## Markdown Metadata

Markdown authority and reference files should include this block immediately after the authority contract:

```text
Creator: Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-04-26
```

Public explainer and user-guide files may use higher document versions and changelogs.

Smaller reference files do not need changelogs unless they are public-facing guides or long-form explainers.

## Script And Workflow Metadata

Maintained Python and shell scripts should include:

```text
# Version: v0.1.0
# Last updated: 2026-04-26
# Owner: Precode OS
```

GitHub workflow YAML should include the same comment block at the top.

## Update Rules

- Bump a file's version when the file's behavior, instructions, interface, schema, or public meaning changes.
- Small typo fixes may update only `Last updated`.
- New files start at `v0.1.0`.
- Generated files should not be manually bumped.
- Version metadata must not conflict with the authority contract.

## Advisory Check

`scripts/version-check.py` is advisory. It reports missing or malformed version metadata without mutating files.

Warnings are generated evidence only. They do not choose tasks, approve PRDs, activate beads, change bead state, or edit active memory.
