# Sanitized Submitted Evidence Packet
<!-- ANCHOR: sanitized-submitted-evidence-packet -->

> AUTHORITY: Reusable public-safe template for reviewing and sharing explicit sanitized PrecodeOS usage evidence.
> NOT_AUTHORITY: Product validation, adoption proof, support case records, telemetry authorization, roadmap selection, PRD approval, bead activation, implementation acceptance, task selection, generated proof, external submission, or maintainer review.
> LOAD_WHEN: A user, support engineer, instructor, or maintainer chooses to share reviewed usage evidence through GitHub feedback, a package-bug issue, a cohort packet, or a private maintainer channel.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-08-04

## Purpose

Use this packet when someone chooses to share PrecodeOS usage evidence after reviewing what is safe to include.

The packet helps keep submitted evidence consistent and redacted. It is source evidence only. It does not prove adoption, create a support record, choose roadmap work, approve a PRD, activate a bead, accept implementation, authorize telemetry, submit anything automatically, or replace maintainer review.

Before sharing, run or ask a helper to run:

```bash
python3 scripts/sanitized-evidence-pack.py --review <packet-file>
```

That helper is local and advisory. It prints warnings; it does not submit, store, score, approve, or mutate external systems.

## Safety Rules

Do not include:

- secrets, tokens, passwords, API keys, credentials, or private keys
- dashboard values, billing details, payment data, customer records, app data, or production configuration values
- raw private transcripts, long raw command output, app logs, or private support notes
- user identity records, sensitive personal data, contributor scoring, productivity ranking, or support case identifiers

Use short summaries and safe placeholders instead:

```text
Auth setup was confusing, but no provider keys, dashboard values, account IDs, or private app data are included.
```

## Pre-Submit Checklist

- Redactions reviewed: `yes | no`
- Submission destination chosen: `GitHub feedback | package-bug issue | cohort packet | private maintainer channel`
- Evidence-only limits understood: `yes | no`

## Packet

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

## Submission Boundary

Submit only after the person sharing the evidence has reviewed the packet and chosen the destination.

GitHub issue text, cohort packet notes, and private maintainer notes remain source evidence until a maintainer reviews and promotes stable conclusions into a Precode owner file, PRD, protocol, decision, or candidate bead.
