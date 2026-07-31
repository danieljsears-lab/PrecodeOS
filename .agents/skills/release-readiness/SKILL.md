---
name: release-readiness
description: |
  Use this skill when a PrecodeOS user asks for Release Readiness Skill,
  release readiness, release-prep help, shipping evidence, a release-candidate
  evidence review, or whether completed or nearly completed work is ready for a
  human release decision.

  This is a read-only host-discoverable packaging surface for the PrecodeOS
  Release Readiness Skill. It prepares release evidence and approval questions
  only. It does not approve release, deploy, promote, roll back, merge, mutate
  GitHub or providers, run migrations, create generated proof, create command
  wrappers, create optional packs, create registries, add release-channel
  behavior, or add package-manager behavior.
allowed-tools:
  - Read
  - Grep
  - Glob
metadata:
  author: Dan Sears / Recode
  version: 0.1.0
---

# Release Readiness Skill

User request: $ARGUMENTS

## Contract

Treat this skill as host-discoverable packaging only. PrecodeOS skill-playbook
authority lives in `tasks/reference/SKILL-PLAYBOOK-PROTOCOL.md`, and release
authority lives in `tasks/reference/RELEASE-READINESS-PROTOCOL.md`.

Load the smallest relevant set of canonical sources:

- `tasks/reference/RELEASE-READINESS-PROTOCOL.md`
- `tasks/reference/SKILL-PLAYBOOK-PROTOCOL.md`
- `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md` when proof tiers or sensitive gates matter
- `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md` when Closeout Evidence or review state matters
- active memory, active bead, primary authority, recorded checks, Closeout Evidence, release-readiness notes, Release Candidate Evidence Profile, and verification/release evidence when present

Generated reports, screenshots, browser notes, GitHub status, dashboards, and
release notes are review input only unless they have been recorded through the
normal evidence path. `ready for human release decision` is not release
approval.

## Return Shape

Return exactly:

```text
Release situation:
Evidence recorded:
Evidence still missing:
Smoke/manual/browser verification:
Rollback or blocked escape:
Approvals still required:
Decision-state recommendation:
Stop condition:
```

Use only these decision-state recommendations when applicable:

- `candidate`
- `needs evidence`
- `blocked`
- `ready for human release decision`

## Forbidden Actions

Do not edit files, deploy, release, promote, roll back, merge, migrate, change
dashboards, change secrets, mutate GitHub resources, mutate providers or
external systems, approve review, accept implementation, activate the next bead,
run mutating commands, create generated proof, certify production readiness,
certify compliance, create provider checklists, create command wrappers, create
registries, create optional packs, add release-channel behavior, add
package-manager behavior, or treat skill output as authority.
