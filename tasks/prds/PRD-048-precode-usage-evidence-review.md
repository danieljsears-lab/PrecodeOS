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
Document version: v0.1.2
Last updated: 2026-08-04

## Summary

PrecodeOS should learn from usage without turning itself into an analytics product.

The first requirement slice defined local, submitted, and networked usage-evidence boundaries before any collector implementation. The Local Opt-In Usage Evidence Review follow-on adds `scripts/usage-evidence-review.py` plus transparent `precode usage-evidence-review` and `precodeos usage-evidence-review` delegation so maintainers and support helpers can inspect safe local evidence without writing a report or submitting telemetry. The Sanitized Submitted Evidence Pack follow-on adds a dedicated packet template and local no-submit review helper so users, support helpers, instructors, or maintainers can review a packet before deliberate sharing. The Cohort/Support Evidence Rollup follow-on adds explicit packet-file aggregation by path or glob so repeated patterns can be reviewed without default scans, support records, analytics, grading, adoption proof, or roadmap selection. Outbound analytics remains deferred until consent, privacy, retention, hosting, endpoint ownership, and public documentation are approved separately.

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
- Customer FAQ: Does PrecodeOS send usage data automatically? No. The local review is opt-in, read-only, no-write, no-submit, and no-network; sharing is explicit.
- Internal FAQ: Does telemetry prove adoption? No. Usage evidence is source material until reviewed against quality, support, and ownership gates.
- Appetite: PRD, evidence taxonomy, local review script/facade delegation, packet fields, a dedicated submitted-packet template, a local no-submit packet review helper, explicit packet-file cohort/support rollup, protocol boundaries, and future-readiness gate only.
- Kill or pause criteria: stop if the work adds default outbound collection, hidden identity tracking, support case records, scoring, task authority, or generated proof.

## Problem

PrecodeOS has local evidence surfaces and public feedback intake, but needs a named local review for telemetry-adjacent usage evidence without crossing privacy, authority, or app-runtime boundaries.

Without a staged contract, future telemetry work could overfit to command counts, support vanity adoption metrics, or add outbound analytics before the package has earned that trust.

## User Moment

- Before: a maintainer or support helper can inspect scattered logs, support notes, issue reports, and cohort packets, but "usage telemetry" has no safe package meaning.
- After: PrecodeOS has a ranked, evidence-only path: local review first through `scripts/usage-evidence-review.py`, explicit sanitized submission second, cohort/support rollup third, and outbound analytics only after readiness approval.
- Why now: alpha/beta learning, support friction, session-friction review, GitHub source intake, and spend import already exist as adjacent evidence lanes.

## Destination

- Destination statement: PrecodeOS defines usage learning as staged evidence capture that improves package maintenance and support without automatic instrumentation.
- Definition of done: PRD owner, local usage-evidence review script and transparent command delegation, submitted-packet template, local packet review helper, explicit packet-file cohort/support rollup helper/template, protocol/documentation boundary updates, cohort/support and GitHub intake alignment, PRD HTML cluster update, maintainer changelog, roadmap implemented history, roadmap journal coverage, and generated review surfaces are current.
- First useful vertical slice: no outbound collector or submitter; add the public requirement owner, safe local review, safe packet/evidence boundaries, dedicated submitted-packet template, local no-submit review helper, and explicit packet-file rollup.

## Goals

- Goal 1: Rank likely telemetry candidates by maintainer learning, support diagnosability, adoption proof, boundary risk, and cost.
- Goal 2: Implement local opt-in usage evidence review as a read-only generated-evidence command.
- Goal 3: Define explicit sanitized submission as the only V1 sharing path.
- Goal 4: Add lightweight cohort/support evidence fields for setup friction, confusing docs or prompts, support intervention type, and what Precode helped the user control.
- Goal 5: Defer outbound analytics behind a separate readiness gate.

## Non-Goals

- No default outbound telemetry, app analytics SDK, hosted event endpoint, dashboard, user identity store, raw transcript collection, app-data collection, install beacon, update beacon, usage leaderboard, contributor scoring, productivity ranking, support case database, automatic issue creation, automatic source promotion, generated proof, task selection, PRD approval, bead activation, implementation acceptance, registry behavior, optional-pack behavior, install/update behavior, release-channel behavior, package-manager behavior, or external mutation.
- No new command wrapper beyond transparent local delegation to usage-evidence helper scripts. Cohort/support rollup may use `precode` as a transparent local facade only; no npm rollup facade, outbound submitter, hosted endpoint, dashboard, or support database.
- No change to active memory.
- No claim that usage evidence proves product validation or beta readiness by itself.

## Ranked Candidate Set

| Rank | Candidate | Disposition | Reason |
|---:|---|---|---|
| 1 | Local Opt-In Usage Evidence Review | Implemented local review surface | Best fit for package maintenance and support diagnosis with no network dependency. |
| 2 | Sanitized Submitted Evidence Pack | Recommended companion surface | Lets users or support helpers share reviewed evidence deliberately through GitHub feedback, package-bug intake, cohort packets, or private maintainer channels. |
| 3 | Cohort/Support Evidence Rollup | Implemented packet-file rollup surface | Extends existing Discovery, Scope, Ownership, and Proof gates with lightweight friction and support signals. |
| 4 | Tool Execution Ledger v2 / Agent Spend Hardening | Narrow follow-up | Useful for cost/tool history, but too narrow to answer broader orientation and support questions alone. |
| 5 | GitHub Source-Intake Rollups | Later after issue volume exists | Helpful only after real public feedback and package-bug evidence accumulates. |
| 6 | Outbound Opt-In Analytics | Deferred readiness gate | Requires consent, privacy policy, retention, endpoint ownership, hosting, security review, and public docs. |
| 7 | Implicit or Default Outbound Telemetry | Rejected | Conflicts with repo-native human control and package trust. |

## Requirements

| ID | Requirement | Priority | Notes |
|---|---|---:|---|
| `PRD-048-FR01` | Define usage evidence as staged local, submitted, and networked layers. | P0 | Networked remains deferred. |
| `PRD-048-FR02` | Local usage evidence review must be opt-in, read-only, and built only from safe local Precode evidence. | P0 | Implemented by `scripts/usage-evidence-review.py` and transparent facades. |
| `PRD-048-FR03` | Local review must report unknowns explicitly when signals are absent. | P0 | Missing evidence is unknown, not zero. |
| `PRD-048-FR04` | Sanitized submitted evidence packets must require explicit user/support review before sharing. | P0 | GitHub issues are allowed source-intake routes. |
| `PRD-048-FR05` | Cohort/support completion evidence must include lightweight setup, docs/prompt, support-intervention, and control-value fields. | P0 | Extends existing packet without making it a grading rubric. |
| `PRD-048-FR06` | Outbound opt-in analytics must stay deferred until a separate readiness gate defines consent, privacy, retention, hosting, endpoint ownership, security review, and public documentation. | P0 | No endpoint or SDK in this slice. |
| `PRD-048-FR07` | Protocols, support docs, package inventory, maintainer changelog, roadmap history, roadmap journal, and generated PRD/docs/roadmap HTML must reflect the evidence-only boundary. | P1 | Maintainer follow-through. |
| `PRD-048-FR08` | Sanitized submitted evidence must have a dedicated public packet template and local no-submit review helper. | P0 | The helper prints templates or advisory review warnings only. |
| `PRD-048-FR09` | GitHub feedback and package-bug intake may accept reviewed sanitized packet excerpts, but no command may submit them automatically. | P0 | External submission remains a user action. |
| `PRD-048-FR10` | Cohort/support rollups must aggregate only explicit packet files supplied by path or glob, and must report sparse evidence as unknown rather than as no friction. | P0 | No default repo scan, support database, grading, adoption proof, or roadmap selection. |

## Local Review Shape

Run `python3 scripts/usage-evidence-review.py`, `python3 scripts/precode_cli.py usage-evidence-review`, or `npx @precodeos/precodeos usage-evidence-review` when a maintainer, support helper, or user explicitly wants local usage-learning evidence.

The local opt-in review summarizes:

- workflow moments used
- setup and refresh friction
- repeated command or tool friction
- stale evidence patterns
- recovery triggers
- docs, prompts, templates, or protocols referenced when safely known through generated summaries or findings
- local check and generated-report freshness signals
- agent spend import presence, with missing spend marked unknown
- scheduled-audit presence
- Session Friction Review finding categories

The review reports missing ledgers as `unknown_because_not_logged`; absence is unknown, not zero usage. It prints plain text or JSON only and does not write `logs/usage-evidence-review.*`.

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

Use `tasks/templates/SANITIZED-SUBMITTED-EVIDENCE-PACKET.md` as the dedicated public packet template when the evidence will be shared outside a normal cohort completion packet. A user or helper may run `python3 scripts/sanitized-evidence-pack.py --template` to print the shape or `python3 scripts/sanitized-evidence-pack.py --review <packet-file>` to check for missing fields, redaction notes, destination selection, explicit unknowns, and sensitive-looking terms before sharing.

The helper is local advisory review only. It must not write packet files, submit to GitHub, create issues, call hosted endpoints, collect telemetry, store identity records, create support records, score contributors, rank productivity, approve owner-file promotion, choose roadmap work, approve PRDs, activate beads, accept implementation, or create generated proof.

## Cohort/Support Evidence Rollup Shape

Run `python3 scripts/cohort-support-evidence-rollup.py --packet <packet-file>`, `python3 scripts/cohort-support-evidence-rollup.py --glob "<packet-glob>"`, or `precode cohort-support-rollup --packet <packet-file>` only after explicit Builder Completion Evidence Packet or Sanitized Submitted Evidence Packet files exist.

The rollup reads only packet files named with `--packet` or `--glob`; it performs no default repo scan. It reports packet count, packet-volume status, target context counts, setup or refresh friction presence, confusing docs/prompts/commands/templates presence, support intervention type counts, control-value notes presence, unclear/heavy notes presence, checks reviewed presence, explicit unknowns, redaction notes, capped source refs, and sensitive-looking term warnings.

If fewer than three packet files are supplied, the rollup reports `unknown_insufficient_packet_volume`; sparse evidence is unknown, not no friction. Source refs cite file paths and line labels only, not full raw packet content.

The rollup is source evidence only. It must not write rollup files, submit evidence, create issues, call hosted endpoints, collect telemetry, store identity records, create support records, grade builders, score contributors, rank productivity, prove adoption, validate the product, approve owner-file promotion, choose roadmap work, approve PRDs, activate beads, accept implementation, or create generated proof.

## Acceptance Criteria

| Requirement | Acceptance check | Evidence |
|---|---|---|
| `PRD-048-FR01` / `PRD-048-FR06` | Public source distinguishes local, submitted, and deferred networked layers. | Source review. |
| `PRD-048-FR02` / `PRD-048-FR03` | Local review is read-only, opt-in, local-first, and names unknowns. | `python3 scripts/usage-evidence-review.py --self-test` and JSON/plain review. |
| `PRD-048-FR04` | Submitted packet is explicit, sanitized, and evidence-only. | PRD/support/template review. |
| `PRD-048-FR05` | Completion packet includes lightweight usage/support fields without becoming a rubric or support case record. | Template review. |
| `PRD-048-FR07` | Protocols, inventory, changelog, roadmap, journal, generated PRD/docs/roadmap surfaces are current. | Validation commands. |
| `PRD-048-FR08` | Dedicated submitted-packet template and local helper exist; helper has template, review, JSON, and self-test modes with no-write/no-submit boundaries. | `python3 scripts/sanitized-evidence-pack.py --self-test`. |
| `PRD-048-FR09` | GitHub intake wording routes reviewed sanitized packet excerpts as source evidence only and keeps submission manual. | Source review and GitHub importer self-test. |
| `PRD-048-FR10` | Rollup helper and template exist; helper requires explicit `--packet` or `--glob`, has JSON/self-test modes, reports sparse volume as unknown, and keeps no-write/no-submit boundaries. | `python3 scripts/cohort-support-evidence-rollup.py --self-test` and `precode cohort-support-rollup --dry-run --packet <packet-file>`. |

## Risk And Permission Model

- Stop if the work adds default outbound network calls, endpoint configuration, identity tracking, raw transcript handling, app-data collection, support case records, scoring, hidden submission, automatic issue creation, or automatic source promotion.
- Stop if generated usage evidence is treated as adoption proof, product validation, support approval, task selection, PRD approval, bead activation, implementation acceptance, roadmap approval, or release approval.
- Any future outbound analytics requires a separate high-risk PRD or semantic-change proposal, security/privacy review, consent language, retention rules, public documentation, and explicit maintainer approval.

## Module / Interface Candidates

| Candidate module or boundary | Public interface / caller expectation | Behavior contract | Test boundary | Owner file |
|---|---|---|---|---|
| Local usage evidence review | `scripts/usage-evidence-review.py`, `precode usage-evidence-review`, and `precodeos usage-evidence-review`. | Read-only local evidence summary, opt-in, no-write, no-submit, no network, explicit unknowns. | Self-test plus JSON/plain no-write review. | This PRD and Tool Execution Protocol. |
| Submitted usage evidence packet | `tasks/templates/SANITIZED-SUBMITTED-EVIDENCE-PACKET.md`, `scripts/sanitized-evidence-pack.py`, completion packet, GitHub feedback/package-bug issue, or private maintainer channel. | Explicitly reviewed sanitized source evidence only; helper reviews locally and never submits. | Self-test plus source/template review. | This PRD and GitHub Collaboration Hub. |
| Cohort/support rollup | `scripts/cohort-support-evidence-rollup.py`, `precode cohort-support-rollup`, `tasks/templates/COHORT-SUPPORT-EVIDENCE-ROLLUP.md`, Builder Completion Evidence Packet, and Sanitized Submitted Evidence Packet. | Explicit packet-file aggregation only; no default scan, support database, grading, adoption proof, product validation proof, or roadmap selection. | Self-test plus source/template review. | This PRD and alpha/beta evidence plan. |
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
  - `tasks/templates/SANITIZED-SUBMITTED-EVIDENCE-PACKET.md`
  - `scripts/usage-evidence-review.py`
  - `scripts/sanitized-evidence-pack.py`
  - `tasks/templates/COHORT-SUPPORT-EVIDENCE-ROLLUP.md`
  - `scripts/cohort-support-evidence-rollup.py`
- Files or folders out of scope:
  - active memory
  - user app code
  - analytics SDKs
  - hosted endpoints
  - public issue mutation
  - support case databases
  - package-manager files
  - new command wrappers beyond transparent local delegation to usage-evidence helper scripts

## Required Validation

```bash
python3 scripts/usage-evidence-review.py --self-test
python3 scripts/usage-evidence-review.py --json
python3 scripts/precode_cli.py usage-evidence-review --dry-run
python3 scripts/precode_cli.py usage-evidence-review --json
node bin/precodeos.mjs usage-evidence-review --json
python3 scripts/sanitized-evidence-pack.py --self-test
python3 scripts/cohort-support-evidence-rollup.py --self-test
python3 scripts/precode_cli.py cohort-support-rollup --dry-run --packet tasks/templates/SANITIZED-SUBMITTED-EVIDENCE-PACKET.md
python3 scripts/import-github-sources.py --self-test
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
- If `scripts/sanitized-evidence-pack.py` adds submit, issue-creation, endpoint, write-evidence, support-record, identity, scoring, or roadmap-promotion behavior, it violates this PRD.
- If `scripts/cohort-support-evidence-rollup.py` scans the repo by default, writes rollup files, accepts raw transcripts as inputs, creates support records, grades builders, scores contributors, treats sparse packets as no friction, or chooses roadmap work, it violates this PRD.

## Candidate Bead Proposal

| Bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Validation |
|---|---|---|---|---|---|---|---|
| `B048-precode-usage-evidence-review` | `PRD-048-FR01` through `PRD-048-FR07` | Usage evidence PRD owner, local/submitted/networked boundary wording, local usage-evidence review script and transparent facades, sanitized packet shape, cohort/support fields, protocol/docs/inventory updates, maintainer changelog, roadmap history, and generated docs/PRD/roadmap HTML are implemented and validated. | `human_in_loop` | `static_and_fixture` | `same_session_ok` | `tasks/prds/PRD-048-precode-usage-evidence-review.md` | usage-evidence self-test, session-friction self-test, package/docs/PRD/roadmap checks |
| `B048-sanitized-submitted-evidence-pack` | `PRD-048-FR04`, `PRD-048-FR07`, `PRD-048-FR08`, `PRD-048-FR09` | Dedicated submitted-packet template, local no-submit helper, GitHub intake alignment, support/template/protocol/docs/inventory updates, maintainer changelog, roadmap history, roadmap journal, and generated docs/PRD/roadmap HTML are implemented and validated. | `human_in_loop` | `static_and_fixture` | `same_session_ok` | `tasks/prds/PRD-048-precode-usage-evidence-review.md` | sanitized evidence helper self-test, GitHub importer self-test, package/docs/PRD/roadmap checks |
| `B048-cohort-support-evidence-rollup` | `PRD-048-FR05`, `PRD-048-FR07`, `PRD-048-FR10` | Packet-file rollup helper, rollup template, local `precode` facade, support/template/protocol/docs/inventory updates, maintainer changelog, roadmap history, roadmap journal, and generated docs/PRD/roadmap HTML are implemented and validated. | `human_in_loop` | `static_and_fixture` | `same_session_ok` | `tasks/prds/PRD-048-precode-usage-evidence-review.md` | cohort/support rollup self-test, facade dry-run, package/docs/PRD/roadmap checks |

## Approval

- Approval state: approved by maintainer implementation request on 2026-08-04.
