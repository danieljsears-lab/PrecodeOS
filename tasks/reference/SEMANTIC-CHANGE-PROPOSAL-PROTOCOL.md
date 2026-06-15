# PrecodeOS -- Semantic Change Proposal Protocol
<!-- ANCHOR: semantic-change-proposal-protocol -->

> AUTHORITY: Semantic-change proposal triggers, required proposal fields, maintainer review outcomes, and non-authority boundaries for trust-affecting PrecodeOS package changes.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, generated progress state, implementation acceptance, package release approval, or contributor governance rights.
> LOAD_WHEN: Proposing or reviewing a PrecodeOS package change that may alter active memory, authority ownership, generated-output demotion, package install/update boundaries, governance or contribution semantics, or beginner-facing safety language.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.1
Last updated: 2026-06-15

## Purpose

Some PrecodeOS changes alter what the package means, not just what a file says.

Use this protocol when a maintainer or contributor is proposing a change that could shift Precode's trust boundaries, authority model, or safety posture. The goal is to make the semantic change visible before implementation or merge, without creating normal-user ceremony or a new approval engine.

The proposal is review evidence only. It does not approve the change, activate work, accept implementation, publish a package release, or replace maintainer judgment.

## Trigger The Gate

Use a Semantic Change Proposal before changing:

- active-memory membership, loading rules, or precedence
- authority contracts, owner-file responsibility, or promotion paths
- generated-output demotion rules, generated authority-map surface classes, or generated report behavior that could be mistaken for authority
- package install, update, setup, bootstrap, release-channel, rollback, or package-manager boundaries
- governance, contribution, trademark, license, provenance, public-positioning, or official-project identity semantics
- beginner-facing safety language, approval gates, stop conditions, destructive-action guidance, external-mutation guidance, or sensitive-surface guidance
- command-wrapper, optional-pack, adapter, skill-playbook, integration, or registry behavior that could create hidden authority

If the change is small but touches one of these boundaries, use the proposal. Small wording changes can still alter package meaning.

## Do Not Trigger The Gate

Do not require this protocol for:

- typo fixes that do not change meaning
- formatting-only edits
- generated-output refreshes from unchanged source Markdown
- narrow doc discoverability links that do not alter authority, approval, setup, release, or safety meaning
- ordinary bead implementation inside an already approved package path
- candidate roadmap notes that do not change public package behavior

If uncertain, write a short proposal instead of guessing. The proposal can conclude that the change is non-semantic.

## Proposal Fields

A Semantic Change Proposal must include:

```text
Semantic boundary changed:
Affected owner files:
Current authority:
Proposed change:
Preserved non-authority boundaries:
Validation evidence:
Docs/protocol/inventory follow-through:
Rollback or reversal path:
Maintainer decision state:
```

Use plain language. The proposal should be short enough to review before implementation.

## Field Guidance

`Semantic boundary changed` names the package meaning at risk, such as active memory, generated-output demotion, setup mutation, release authority, maintainer review, or beginner safety.

`Affected owner files` lists the public files, protocols, docs, scripts, generated surfaces, maintainer files, or metadata that need to stay consistent.

`Current authority` names the file or protocol that currently owns the behavior. If no owner exists, say so directly.

`Proposed change` states what meaning will change for users, contributors, maintainers, or agents.

`Preserved non-authority boundaries` names what the change must not do, such as approving PRDs, activating beads, choosing tasks, mutating external systems, adding active memory, creating release authority, or making generated reports authoritative.

`Validation evidence` lists the static checks, freshness checks, manual review steps, or source comparisons needed before confidence is warranted.

`Docs/protocol/inventory follow-through` names public docs, protocols, package inventory entries, generated authority-map impact, generated docs HTML, roadmap history, and maintainer changelog entries that must be updated if the change lands.

`Rollback or reversal path` explains how the package meaning can be restored if the change creates confusion.

`Maintainer decision state` is one of:

- `proposed`
- `approved to implement`
- `needs revision`
- `rejected`
- `implemented`

Only the maintainer can move a trust-affecting semantic change out of `proposed`.

## Review Outcomes

Maintainer review should return one of:

- `approved to implement`: the semantic risk is understood and follow-through is clear
- `needs revision`: the proposal is missing owner files, preserved boundaries, validation, or rollback
- `split`: the proposal combines semantic changes that need separate review
- `non-semantic`: the change can proceed through ordinary contribution review
- `rejected`: the change weakens package trust or violates project direction

These outcomes guide contribution review only. They do not approve code, accept implementation, publish releases, or activate Precode work.

## Stop Conditions

Stop before implementation or merge when:

- no owner file can be named for the current behavior
- active-memory, authority, generated-output, install/update, release, or safety meaning is changing without a proposal
- generated reports, exported text, scripts, skills, adapters, or external systems appear to be making decisions
- the proposal depends on private maintainer files as public package authority
- validation or docs/protocol/inventory follow-through is missing
- rollback or reversal is unclear for a trust-affecting change

## Relationship To Other Protocols

Use `tasks/reference/EXTENSION-PROTOCOL.md` when the change adds or reviews an extension, adapter, protocol, skill playbook, importer, audit, generated report, or external integration.

Use `tasks/reference/TOOL-EXECUTION-PROTOCOL.md` when the change affects command execution, tool logging, external systems, destructive commands, or approval gates.

Use `tasks/reference/SKILL-PLAYBOOK-PROTOCOL.md` when the change packages a named host-agent prompt playbook.

Use `tasks/reference/RELEASE-READINESS-PROTOCOL.md` for user-project shipping decisions. This protocol does not deploy, publish, approve release, roll back, or mutate external systems.

## Maintainer Checklist

Before landing a semantic change:

- confirm the current owner file and proposed owner file are clear
- confirm active memory remains unchanged unless the proposal explicitly changes the kernel
- confirm generated outputs remain evidence only
- confirm no new command, wrapper, registry, optional pack, installer, or package-manager behavior is introduced by implication
- update affected docs, protocols, package inventory, generated reading surfaces, roadmap history, and `_maintainer/CHANGELOG.md` when public package files change
- run the relevant static checks and freshness checks
