# Precode OS -- Scheduled Audit
<!-- ANCHOR: scheduled-audit -->

> AUTHORITY: Generated scheduled audit snapshot for Precode OS local and external status checks.
> NOT_AUTHORITY: Active memory, task selection, product decisions, implementation plans, bead state, external system mutation, or generated progress state.
> LOAD_WHEN: Reviewing scheduled audit findings; never as active session memory.
> CLASS: generated
>
> Generated from `scripts/scheduled-audit.py`.
> Do not use this file as active memory or as a task plan.

Generated at: `2026-04-28T18:19:09.587242+00:00`

## Reading Rule

This audit is evidence only. A user must promote findings into the correct Precode owner file or approve a follow-up bead before anything changes.

## Local Audits

- **Health Refresh Audit**: `pass` - OS health refresh completed
- **Memory Validation Audit**: `pass` - `bash scripts/validate-memory.sh` exited 0
- **Learning Diary Refresh Audit**: `pass` - learning diary refreshed without appending a fake session
- **Spend Telemetry Audit**: `pass` - 0 spend entries; known tokens 0; known spend $0.0000
- **Stale Bead Audit**: `pass` - active bead has recorded evidence or is not stale by first-pass criteria
- **Closeout Completeness Audit**: `warning` - manual verification is missing; review decision is not accepted; next bead safety is not evaluated
- **Generated Reports Demotion Audit**: `pass` - generated reports are demoted
- **Blocked Work Audit**: `pass` - no blocked beads found
- **Verification Quality Audit**: `warning` - manual verification is missing, pending, or does not use the stable format; review decision is not accepted
- **Decomposition Quality Audit**: `warning` - multiple apparent authority surfaces may be involved: ['PROJECT-CONTEXT.md']
- **State Integrity Audit**: `warning` - generated report may be stale relative to latest evidence: logs/scheduled-audit.md
- **Intent Orchestration Audit**: `warning` - tasks/todo.md Next Up contains work-like intent; confirm it is only a queue and not active work
- **Tool Execution Audit**: `pass` - no first-pass tool execution warnings
- **Workflow Planning Audit**: `pass` - no first-pass workflow planning warnings
- **Long-Horizon Planning Audit**: `pass` - no first-pass long-horizon planning warnings
- **Completion And Handoff Audit**: `warning` - manual verification is missing or vague; review decision is missing or invalid; active bead has recorded evidence newer than the latest session close
- **System Design Pattern Audit**: `pass` - no first-pass system design pattern warnings
- **Filesystem Memory Audit**: `pass` - 0 reviewed memory card(s); generated index remains evidence only
- **File Inventory Audit**: `pass` - 59 docs, 39 scripts, and 24 generated outputs inventoried

## External Audits

- **GitHub Repository Audit**: `not_configured` - not a git checkout or .git directory is unavailable
- **CI Status Audit**: `not_configured` - requires git checkout and configured provider
- **Deployment Status Audit**: `not_configured` - no deployment provider audit configured
- **Issue Tracker Audit**: `not_configured` - no issue tracker audit configured
- **Dependency/Security Advisory Audit**: `not_configured` - no read-only dependency or advisory source configured
- **Error Monitoring / Observability Audit**: `not_configured` - no monitoring provider audit configured
- **Uptime / Endpoint Audit**: `not_configured` - no safe health URL configured
- **External Dashboard Setup Audit**: `not_configured` - manual dashboard setup status should be documented in PROJECT-CONTEXT.md when needed

## Warnings

- manual verification is missing
- review decision is not accepted
- next bead safety is not evaluated
- manual verification is missing, pending, or does not use the stable format
- review decision is not accepted
- multiple apparent authority surfaces may be involved: ['PROJECT-CONTEXT.md']
- generated report may be stale relative to latest evidence: logs/scheduled-audit.md
- tasks/todo.md Next Up contains work-like intent; confirm it is only a queue and not active work
- manual verification is missing or vague
- review decision is missing or invalid
- active bead has recorded evidence newer than the latest session close

## Human Review Prompts

- Review warnings before accepting or promoting any bead.
- If a finding matters, move it into the owning Precode file or create a proposed follow-up bead.
- Do not continue work from this generated audit alone; start from active memory and the active bead.
