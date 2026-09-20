---
prd_id: PRD-052
status: approved
owner: Dan Sears / Recode
created: 2026-09-20
last_updated: 2026-09-20
risk_level: low
feature_link: Ambient Engineering Judgment Defaults
features_status: not compiled
related_prds:
  - PRD-036
  - PRD-038
  - PRD-039
  - PRD-040
---

# PRD-052 -- Ambient Engineering Judgment Defaults
<!-- ANCHOR: prd-052-ambient-engineering-judgment-defaults -->

> AUTHORITY: Public requirements for integrating a small host-neutral engineering judgment default into existing PrecodeOS routing and prompt surfaces.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, implementation approval, review acceptance, release approval, quality scoring, certification, application-code analysis, checker-gate authority, skill registry behavior, or autonomous execution approval.
> LOAD_WHEN: Reviewing or validating the ambient Engineering Judgment Defaults integration.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-09-20

## Summary

PrecodeOS already owns a thin Engineering Quality floor and risk-specific protocols. This slice makes the existing judgment easier for beginners and host agents to discover without adding a new skill, stage, router, checker, or active-memory layer.

## Contract

For software-building or software-changing requests, agents should keep visible as appropriate to the risk:

- intended outcome and smallest useful change
- owner surface for behavior, state, data, configuration, or provider calls
- narrowest proof path
- sensitive or approval-sensitive risk triggers
- existing protocol route when a trigger appears
- material uncertainty and stop conditions
- human approval for consequential decisions

Low-risk work may apply the defaults silently. Meaningful shared-surface work may show the compact Engineering Quality floor. High-risk work stops and routes to the existing owner protocol.

## Non-Goals

- no new active-memory file, skill registry, command, checker, score, verdict, certification, or application-code analyzer
- no required stage for every bead and no duplicate owner protocol
- no task selection, PRD approval, bead activation, implementation approval, review acceptance, release approval, or external mutation

## Acceptance

- Engineering Quality Standards owns the canonical defaults and boundaries.
- Agent Routing and Workflow Selection point to the defaults without taking ownership of engineering-quality policy.
- Prompt Patterns provides one beginner-readable copyable invocation.
- User Guide explains the behavior without creating a new route.
- Static checks confirm authority, no-certification, no-approval, and no-new-machinery wording.
- Public generated documentation remains synchronized with canonical Markdown.

## Validation

Review these scenarios: tiny copy/styling work, local behavior change, shared component/API change, sensitive or deployment work, broad build request, and unclear post-change proof. Confirm that only the relevant existing protocol is invoked and that low-risk work is not expanded into ceremony.
