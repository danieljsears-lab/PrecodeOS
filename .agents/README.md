# PrecodeOS Agent Skills Boundary
<!-- ANCHOR: agents-skills-boundary -->

> AUTHORITY: Boundary note for host-installed skill files bundled under `.agents/skills/`.
> NOT_AUTHORITY: Active memory, Precode skill-playbook authority, task selection, PRD approval, bead activation, command approval, generated evidence truth, package-manager behavior, registry behavior, optional-pack installation, or implementation acceptance.
> LOAD_WHEN: Inspecting `.agents/skills/`, packaging host-agent skill files, or distinguishing host skills from Precode skill playbooks.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-19

## Purpose

`.agents/skills/` contains host-agent skill files that may be installed or discovered by compatible agent tools.

These files are not PrecodeOS skill playbooks. PrecodeOS skill-playbook authority lives in `tasks/reference/SKILL-PLAYBOOK-PROTOCOL.md` and the relevant owner protocols or docs.

Use `.agents/skills/` as host-discoverable packaging only. If a user needs help choosing a Precode skill-style invocation, route through `tasks/reference/PROMPT-PATTERNS.md` and the Skill Playbook Protocol's Skill Playbook Ergonomics guidance; do not turn the host skill folder into a beginner-facing skill catalog.

## Boundary Rules

- Do not treat `.agents/skills/` as active memory.
- Do not use host skill metadata as task selection, command approval, PRD approval, bead activation, review acceptance, or transition approval.
- Do not let a host skill registry become a Precode package registry.
- Do not use `.agents/skills/` as a Precode skill catalog, optional-pack list, marketplace, install/update surface, command wrapper, or package-manager surface.
- Do not treat third-party skill permissions, examples, memory, or generated output as Precode package authority.
- Use `tasks/reference/EXTENSION-PROTOCOL.md` and `tasks/reference/TOOL-EXECUTION-PROTOCOL.md` when a hosted skill touches external systems, runs tools, writes files, or needs approval boundaries.
- Keep Precode prompt-playbook changes in `tasks/reference/SKILL-PLAYBOOK-PROTOCOL.md` plus the owning public protocol or documentation surface.

## Current Contents

The current bundled skills are Nimble-oriented research and web-data skills. They may have their own prerequisites, external API behavior, write permissions, and host-specific tool declarations. Those capabilities belong to the host skill's own contract; they do not expand PrecodeOS active memory or public workflow authority.
