---
prd_id: PRD-048
status: approved
owner: Dan Sears / Recode
created: 2026-08-04
last_updated: 2026-08-04
risk_level: high
feature_link: Precode Usage Evidence Review
features_status: not compiled
related_prds:
  - PRD-027
  - PRD-032
---

# PRD-048 -- Precode Usage Evidence Review
<!-- ANCHOR: prd-048-precode-usage-evidence-review -->

> AUTHORITY: Public requirements for staged, evidence-only PrecodeOS usage learning, including local opt-in usage evidence review, explicit sanitized submission, cohort/support evidence fields, and deferred outbound analytics readiness.
> NOT_AUTHORITY: Active memory, product truth, user identity records, app analytics, automatic outbound telemetry, runtime instrumentation, hosted analytics infrastructure, task selection, roadmap approval, PRD approval, bead activation, implementation acceptance, support case records, contributor scoring, productivity ranking, generated proof, external mutation, registry behavior, optional-pack behavior, install/update behavior, release-channel behavior, package-manager behavior, or implementation status.
> LOAD_WHEN: Planning, implementing, reviewing, or supporting PrecodeOS usage evidence, telemetry-adjacent evidence capture, sanitized evidence packets, cohort/support evidence rollups, or future analytics readiness.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-08-04

## Summary

PrecodeOS should learn from usage without turning itself into an analytics product.

The first useful slice is a local, opt-in usage evidence review built from safe repo evidence. Users or support helpers may explicitly submit sanitized packets or GitHub issues when they choose. Outbound analytics remains deferred until consent, privacy, retention, hosting, endpoint ownership, and public documentation are approved separately.

## Source Inputs

- Source type: maintainer plan and package-boundary review
- Source references:
  - `tasks/prds/PRD-027-session-friction-review.md`
  - `tasks/prds/PRD-032-github-collaboration-hub.md`
  - `tasks/reference/EXTENSION-PROTOCOL.md`
  - `tasks/reference/TOOL-EXECUTION-PROTOCOL.md`
  - `tasks/reference/SCHEDULED-AUDIT-PROTOCOL.md`
  - `SECURITY.md`
- Stable facts:
  - Session Friction Review is local, read-only, and explicitly not telemetry.
  - GitHub feedback and package-bug issues are source evidence only.
  - Scheduled audits may dry-run spend telemetry import and read local logs, but must not mutate work or external systems.
  - Existing agent spend import handles cost/token telemetry, not product usage analytics.
- Assumptions:
  - Maintainer learning is the primary goal, support diagnosability is second, and adoption proof is third.
  - Local opt-in evidence should precede explicit submission, and explicit submission should precede any networked analytics.
- Privacy or secrets redactions:
  - Usage evidence must not include secrets, credentials, private raw transcripts, dashboard values, app data, customer records, sensitive personal data, user identity records, contributor scoring, productivity ranking, or long raw command output.

## PRFAQ-Lite

- Press-release claim: PrecodeOS can learn where users lose orientation without collecting hidden analytics.
- Customer problem: support and maintainer feedback can stay anecdotal unless safe local evidence and submitted packets have a common shape.
- Customer FAQ: Does PrecodeOS send usage data automatically? No. V1 is local and opt-in; sharing is explicit.
- Internal FAQ: Does telemetry prove adoption? No. Usage evidence is source material until reviewed against quality, support, and ownership gates.
- Appetite: PRD, evidence taxonomy, packet fields, protocol boundaries, and future-readiness gate only.
- Kill or pause criteria: stop if the work adds default outbound collection, hidden identity tracking, support case records, scoring, task authority, or generated proof.

## Problem

PrecodeOS has local evidence surfaces and public feedback intake, but no named shape for reviewing telemetry-adjacent usage evidence without crossing privacy, authority, or app-runtime boundaries.

Without a staged contract, future telemetry work could overfit to command counts, support vanity adoption metrics, or add outbound analytics before the package has earned that trust.

## User Moment

- Before: a maintainer or support helper can inspect scattered logs, support notes, issue reports, and cohort packets, but "usage telemetry" has no safe package meaning.
- After: PrecodeOS has a ranked, evidence-only path: local review first, explicit sanitized submission second, cohort/support rollup third, and outbound analytics only after readiness approval.
- Why now: alpha/beta learning, support friction, session-friction review, GitHub source intake, and spend import already exist as adjacent evidence lanes.

## Destination

- Destination statement: PrecodeOS defines usage learning as staged evidence capture that improves package maintenance and support without automatic instrumentation.
- Definition of done: PRD owner, protocol/documentation boundary updates, cohort/support packet fields, PRD HTML cluster update, maintainer changelog, roadmap implemented history, roadmap journal coverage, and generated review surfaces are current.
- First useful vertical slice: no new collector yet; add the public requirement owner and safe packet/evidence boundaries before implementation.

## Goals

- Goal 1: Rank likely telemetry candidates by maintainer learning, support diagnosability, adoption proof, boundary risk, and cost.
- Goal 2: Define local opt-in usage evidence review as the recommended next implementation candidate.
- Goal 3: Define explicit sanitized submission as the only V1 sharing path.
- Goal 4: Add lightweight cohort/support evidence fields for setup friction, confusing docs or prompts, support intervention type, and what Precode helped the user control.
- Goal 5: Defer outbound analytics behind a separate readiness gate.

## Non-Goals

- No default outbound telemetry, app analytics SDK, hosted event endpoint, dashboard, user identity store, raw transcript collection, app-data collection, install beacon, update beacon, usage leaderboard, contributor scoring, productivity ranking, support case database, automatic issue creation, automatic source promotion, generated proof, task selection, PRD approval, bead activation, implementation acceptance, registry behavior, optional-pack behavior, install/update behavior, release-channel behavior, package-manager behavior, or external mutation.
- No new command wrapper in this PRD.
- No change to active memory.
- No claim that usage evidence proves product validation or beta readiness by itself.

## Ranked Candidate Set

| Rank | Candidate | Disposition | Reason |
|---:|---|---|---|
| 1 | Local Opt-In Usage Evidence Review | Recommended next implementation candidate | Best fit for package maintenance and support diagnosis with no network dependency. |
| 2 | Sanitized Submitted Evidence Pack | Recommended companion surface | Lets users or support helpers share reviewed evidence deliberately through GitHub feedback, package-bug intake, cohort packets, or private maintainer channels. |
| 3 | Cohort/Support Evidence Rollup | Recommended adoption-proof support | Extends existing Discovery, Scope, Ownership, and Proof gates with lightweight friction and support signals. |
| 4 | Tool Execution Ledger v2 / Agent Spend Hardening | Narrow follow-up | Useful for cost/tool history, but too narrow to answer broader orientation and support questions alone. |
| 5 | GitHub Source-Intake Rollups | Later after issue volume exists | Helpful only after real public feedback and package-bug evidence accumulates. |
| 6 | Outbound Opt-In Analytics | Deferred readiness gate | Requires consent, privacy policy, retention, endpoint ownership, hosting, security review, and public docs. |
| 7 | Implicit or Default Outbound Telemetry | Rejected | Conflicts with repo-native human control and package trust. |

## Requirements

| ID | Requirement | Priority | Notes |
|---|---|---:|---|
| `PRD-048-FR01` | Define usage evidence as staged local, submitted, and networked layers. | P0 | Networked remains deferred. |
| `PRD-048-FR02` | Local usage evidence review must be opt-in, read-only, and built only from safe local Precode evidence. | P0 | Candidate future script/check work. |
| `PRD-048-FR03` | Local review must report unknowns explicitly when signals are absent. | P0 | Missing evidence is unknown, not zero. |
| `PRD-048-FR04` | Sanitized submitted evidence packets must require explicit user/support review before sharing. | P0 | GitHub issues are allowed source-intake routes. |
| `PRD-048-FR05` | Cohort/support completion evidence must include lightweight setup, docs/prompt, support-intervention, and control-value fields. | P0 | Extends existing packet without making it a grading rubric. |
| `PRD-048-FR06` | Outbound opt-in analytics must stay deferred until a separate readiness gate defines consent, privacy, retention, hosting, endpoint ownership, security review, and public documentation. | P0 | No endpoint or SDK in this slice. |
| `PRD-048-FR07` | Protocols, support docs, package inventory, maintainer changelog, roadmap history, roadmap journal, and generated PRD/docs/roadmap HTML must reflect the evidence-only boundary. | P1 | Maintainer follow-through. |

## Future Local Review Shape

A future local opt-in review may summarize:

- workflow moments used
- setup and refresh friction
- repeated command or tool friction
- stale evidence patterns
- recovery triggers
- docs, prompts, templates, or protocols referenced when safely known
- local check and generated-report freshness signals
- agent spend import presence, with missing spend marked unknown
- GitHub source-intake presence when explicitly imported

It must not summarize raw private transcripts, app logs, dashboard values, secrets, app analytics, production data, user identity, customer records, support case records, contributor scoring, productivity ranking, or raw long command output.

## Sanitized Evidence Packet Shape

Use this shape when a user, support engineer, instructor, or maintainer chooses to share usage evidence:

```text
Usage evidence purpose:
PrecodeOS version or package source, if known:
Target context: new project | existing project | cohort | support | maintainer review
Workflow moments used:
Setup or refresh friction:
Confusing docs, prompts, commands, or templates:
Support intervention type:
What Precode helped the user control:
What remained unclear or too heavy:
Checks or generated evidence reviewed:
Unknown because not logged:
Redactions performed:
Submitted through: GitHub feedback | package-bug issue | cohort packet | private maintainer channel
```

This packet is source evidence only. It does not choose roadmap direction, approve PRDs, activate beads, accept implementation, prove adoption, create support records, or authorize follow-up work.

## Acceptance Criteria

| Requirement | Acceptance check | Evidence |
|---|---|---|
| `PRD-048-FR01` / `PRD-048-FR06` | Public source distinguishes local, submitted, and deferred networked layers. | Source review. |
| `PRD-048-FR02` / `PRD-048-FR03` | Future local review shape is read-only, opt-in, local-first, and names unknowns. | PRD and protocol review. |
| `PRD-048-FR04` | Submitted packet is explicit, sanitized, and evidence-only. | PRD/support/template review. |
| `PRD-048-FR05` | Completion packet includes lightweight usage/support fields without becoming a rubric or support case record. | Template review. |
| `PRD-048-FR07` | Protocols, inventory, changelog, roadmap, journal, generated PRD/docs/roadmap surfaces are current. | Validation commands. |

## Risk And Permission Model

- Stop if the work adds default outbound network calls, endpoint configuration, identity tracking, raw transcript handling, app-data collection, support case records, scoring, hidden submission, automatic issue creation, or automatic source promotion.
- Stop if generated usage evidence is treated as adoption proof, product validation, support approval, task selection, PRD approval, bead activation, implementation acceptance, roadmap approval, or release approval.
- Any future outbound analytics requires a separate high-risk PRD or semantic-change proposal, security/privacy review, consent language, retention rules, public documentation, and explicit maintainer approval.

## Module / Interface Candidates

| Candidate module or boundary | Public interface / caller expectation | Behavior contract | Test boundary | Owner file |
|---|---|---|---|---|
| Future local usage evidence review | `scripts/*usage*` or existing scheduled-audit/session-friction surfaces after separate approval. | Read-only local evidence summary, opt-in, no network. | Self-test plus no-write default check. | This PRD and Tool Execution Protocol. |
| Submitted usage evidence packet | Completion packet, GitHub feedback/package-bug issue, or private maintainer channel. | Explicitly reviewed sanitized source evidence only. | Source/template review. | This PRD and GitHub Collaboration Hub. |
| Cohort/support rollup | Builder Completion Evidence Packet. | Lightweight adoption/support signals without grading, support database, or product validation proof. | Template review. | This PRD and alpha/beta evidence plan. |
| Future outbound analytics readiness | Deferred PRD or semantic-change proposal. | No implementation until consent, privacy, hosting, endpoint, security, retention, and docs are approved. | Future security/privacy validation. | This PRD as readiness gate source. |

## Agent Context Contract

- Primary authority file: `tasks/prds/PRD-048-precode-usage-evidence-review.md`
- Owner protocols:
  - `tasks/reference/EXTENSION-PROTOCOL.md`
  - `tasks/reference/TOOL-EXECUTION-PROTOCOL.md`
  - `tasks/reference/SCHEDULED-AUDIT-PROTOCOL.md`
- Related public references:
  - `tasks/prds/PRD-027-session-friction-review.md`
  - `tasks/prds/PRD-032-github-collaboration-hub.md`
  - `docs/PRECODE-SUPPORT-RUNBOOK.md`
  - `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`
  - `SECURITY.md`
  - `tasks/templates/BUILDER-COMPLETION-EVIDENCE-PACKET.md`
- Files or folders out of scope:
  - active memory
  - user app code
  - analytics SDKs
  - hosted endpoints
  - public issue mutation
  - support case databases
  - package-manager files
  - command wrappers

## Required Validation

```bash
python3 scripts/session-friction-check.py --self-test
python3 scripts/file-inventory.py --check
python3 scripts/public-repo-check.py
python3 scripts/package-knowledge-lint.py --check
python3 scripts/prd-html.py --check
python3 _maintainer/scripts/docs-html.py --check
python3 _maintainer/scripts/roadmap-html.py --check
bash scripts/validate-memory.sh
git diff --check
```

## Anti-Shallow Checks

- If evidence leaves the local repo without explicit user review and submission, it violates this PRD.
- If command counts are treated as adoption proof, it violates this PRD.
- If cohort/support evidence becomes a grading rubric, support database, or product-validation claim, it violates this PRD.
- If outbound analytics is implemented before privacy, consent, retention, hosting, endpoint ownership, security review, and public docs are approved, it violates this PRD.
- If generated usage review output creates tasks or promotes source conclusions automatically, it violates this PRD.

## Candidate Bead Proposal

| Bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Validation |
|---|---|---|---|---|---|---|---|
| `B048-precode-usage-evidence-review` | `PRD-048-FR01` through `PRD-048-FR07` | Usage evidence PRD owner, local/submitted/networked boundary wording, sanitized packet shape, cohort/support fields, protocol/docs/inventory updates, maintainer changelog, roadmap history, and generated docs/PRD/roadmap HTML are implemented and validated. | `human_in_loop` | `static_and_fixture` | `same_session_ok` | `tasks/prds/PRD-048-precode-usage-evidence-review.md` | session-friction self-test, package/docs/PRD/roadmap checks |

## Approval

- Approval state: approved by maintainer implementation request on 2026-08-04.
