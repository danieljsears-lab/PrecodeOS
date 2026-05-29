# Project Evidence Guide
<!-- ANCHOR: project-evidence-guide -->

> AUTHORITY: User guidance for storing raw project evidence such as notes, documents, screenshots, research, and links in a target project.
> NOT_AUTHORITY: Active memory, product truth, PRD approval, task selection, implementation instructions, package authority, generated evidence truth, or permission to code.
> LOAD_WHEN: A user asks where to put reference files, notes, documents, screenshots, research, design exports, or other raw source material for a PrecodeOS project.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-05-29

## Purpose

Use `project-evidence/` for raw source material that belongs to this project but has not become Precode authority.

Good examples:

- notes and markdown drafts
- documents and handoff files
- screenshots, sketches, wireframes, and design exports
- research notes, quotes, and issue exports
- links or short link lists for external material

This folder is project-owned. It is not active memory, not a PrecodeOS package authority folder, not task approval, and not permission for an agent to start coding.

## Suggested Organization

Optional subfolders can help keep the project readable:

- `notes/`
- `documents/`
- `screenshots/`
- `research/`
- `links/`

These subfolders are suggestions, not a required schema. Use names that make sense for the project.

## Evidence Rule

Raw files in `project-evidence/` are evidence, not authority.

If evidence conflicts with `PRODUCT.md`, `DECISIONS.md`, an approved PRD, the active bead, or another Precode owner file, the owner file wins until the user reviews and approves an update.

To use material from this folder, ask the agent to run Local Source Intake. The agent may inspect and summarize explicitly named files read-only, then propose stable conclusions, conflicts, open questions, and likely owner files.

## Git And Privacy

Each project decides whether to track or ignore `project-evidence/`.

Before committing files from this folder, review them for private or sensitive material. Screenshots, documents, customer notes, transcripts, dashboard values, credentials, personal information, and paid research can become visible to collaborators or public repositories if committed.

Do not store secrets, API keys, passwords, credentials, private keys, or environment files here.

## Copyable Prompt

```text
Use Local Source Intake on these project evidence files:

- project-evidence/[path]

Treat them as evidence, not authority. Inspect them read-only. Summarize stable facts, assumptions, conflicts, privacy redactions, open questions, candidate requirements, likely owner files, and the next safe Precode action.

Do not update authority files, approve a PRD, activate a bead, or write code until I review the intake summary.
```
