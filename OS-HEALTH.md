# Precode OS -- OS Health Report
<!-- ANCHOR: os-health -->

> AUTHORITY: Generated OS health snapshot, loop metrics, bead status, and recent check evidence for the Precode OS workspace.
> NOT_AUTHORITY: Active memory, product decisions, feature requirements, implementation plans, or task selection.
> LOAD_WHEN: Auditing Precode OS health, loop friction, check evidence, or blocked-bead status; never as active session memory.
> CLASS: generated
>
> Generated from `scripts/os-health.py`.
> Do not use this file as active memory.
> Working memory lives in `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`.

Generated at: `2026-04-28T18:19:09.063126+00:00`

## Summary

| Signal | Value |
| --- | --- |
| Health | needs attention |
| App directory | `app/` |
| Branch | `unknown` |
| Changed paths | 0 |
| Current bead | `tasks/beads/B000-install-precode-kernel.md` |
| Current bead status | `in_progress` |
| Latest validator evidence | pass (exit 0) |

## Bead Status

| Status | Count |
| --- | --- |
| `in_progress` | 1 |

## Active Bead Check Evidence

| Command | cwd | Status | Exit | Evidence |
| --- | --- | --- | --- | --- |
| `bash scripts/validate-memory.sh` | `.` | pass | 0 | `logs/check-output/20260428T181905Z-bash-scripts-validate-memory.sh.log` |

## Verification Quality

- Status: warning
- Known tiers: static
- Code-changing bead: False

- Warning: manual verification is missing, pending, or does not use the stable format
- Warning: review decision is not accepted

## Decomposition Quality

- Status: warning
- Bead kind: setup
- Files in play: 4
- Checks: 1

- Warning: multiple apparent authority surfaces may be involved: ['PROJECT-CONTEXT.md']

## State Integrity

- Status: warning
- In-progress beads: tasks/beads/B000-install-precode-kernel.md
- Latest event timestamp: 2026-04-28T18:19:05.893523+00:00

- Warning: generated report may be stale relative to latest evidence: logs/learning-diary.md
- Warning: generated report may be stale relative to latest evidence: logs/scheduled-audit.md

## Intent Orchestration

- Status: warning
- Lifecycle state: evidence_recorded
- Current PRD: not recorded
- Requirement IDs: none
- Recorded evidence rows: 37
- Pending approval: True

- Warning: tasks/todo.md Next Up contains work-like intent; confirm it is only a queue and not active work

## Workflow Planning

- Status: pass
- Current situation: planning
- Recommended workflow: planning
- Next artifact: source summary, PRD draft, challenge notes, or candidate bead proposal
- Required authority: tasks/reference/IDEA-TO-PRD-WORKFLOW.md
- User approval needed: not before continuing current approved bead

- No first-pass workflow planning warnings.

## Long-Horizon Planning

- Status: pass
- Approved PRDs: 0
- Ready beads: 0
- Blocked beads: 0
- Follow-up candidates: 0
- Dependency gaps: 0

- No first-pass long-horizon planning warnings.

## Completion And Handoff

- Status: warning
- Closeout status: incomplete
- Promotion status: blocked
- Manual verification: not recorded
- Review decision: not reviewed
- Next safe action: complete manual verification and review decision before transition

- Warning: manual verification is missing or vague
- Warning: review decision is missing or invalid
- Warning: active bead has recorded evidence newer than the latest session close

## System Design Pattern Guidance

- Status: pass
- Likely shape: existing project convention
- Recommended pattern: existing project convention
- Owner hints: PROJECT-CONTEXT.md, CODEBASE-GUIDE.md, active bead
- Warning count: 0
- Review prompt: Ask: Is this simple enough to build directly, or does it need an adapter, state flow, strategy boundary, access boundary, or audit trail?

- No first-pass system design pattern warnings.

## Filesystem Memory

- Status: pass
- Reviewed memory cards: 0
- Categories: none
- Promotion-needed cards: 0
- Stale or superseded cards: 0
- Review prompt: Search reviewed memory for relevant lessons, then return to active memory and the active bead before acting.

- No first-pass filesystem memory warnings.

## File Inventory

- Status: pass
- Canonical inventory: `PRECODE-FILE-INVENTORY.md`
- Documented docs: 59
- Scripts: 39
- Workflows: 1
- Generated outputs tracked: 24

- No first-pass file inventory warnings.

## Tool Execution

- Status: pass
- Tool-run entries: 0
- Active bead entries: 0
- Approval gaps: 0
- Destructive entries: 0
- Latest failure category: none

- No first-pass tool execution warnings.

## Compiled Readiness

- Promote current bead: blocked
- Blocker: manual verification is missing or still pending
- Blocker: current bead status must be review or done before promotion; found in_progress
- Blocker: review decision is not accepted
- Blocker: next bead is not named in Closeout Evidence or Handback

## Loop Metrics

| Metric | Value |
| --- | --- |
| Recorded checks | 37 |
| Passing checks | 37 |
| Failing checks | 0 |
| Tool runs | 0 |
| Session starts | 0 |
| Checkpoints | 0 |
| Session closes | 2 |
| Handoffs | 1 |
| Bead transitions | 0 |
| Event rows | 40 |
| Spend entries | 0 |
| Known spend | $0.0000 |
| Known tokens | 0 |
| Unknown token entries | 0 |
| Unknown cost entries | 0 |

## Spend Rollup

- Latest spend entry: none
- Known total tokens: 0
- Known total spend: $0.0000
- Unknown token entries: 0
- Unknown cost entries: 0

### By Agent

- No spend entries recorded.

### By Task

- No spend entries recorded.

## Generated Sidecars

- `logs/authority-map.json`
- `logs/adapter-index.json`
- `logs/shim-index.json`
- `logs/readiness.json`
- `logs/orchestration-map.json`
- `logs/workflow-map.json`
- `logs/long-horizon-map.json`
- `logs/handoff-packet.json`
- `logs/handoff-packet.md`
- `logs/memory-index.json`
- `logs/memory-index.md`
- `logs/file-inventory.json`
- `logs/os-events.jsonl`

## Learning Promotion Queue

- Drift observed: none recorded
- Lesson to promote: none
- Follow-up bead needed: not evaluated

## Blocked-Bead Escape Snapshot

- Manual verification: not recorded
- Next bead: not evaluated
- Blocked escape: not needed while status is `in_progress`
