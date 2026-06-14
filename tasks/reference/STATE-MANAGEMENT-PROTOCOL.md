# PrecodeOS -- State Management Protocol
<!-- ANCHOR: state-management-protocol -->

> AUTHORITY: Memory and state ownership, precedence rules, open-question ownership, generated-state freshness expectations, recovery workflow, and log/archive guidance for PrecodeOS.
> NOT_AUTHORITY: Active memory expansion, task selection, product decisions, implementation plans, generated progress state, or automatic bead transitions.
> LOAD_WHEN: Repairing state drift, reviewing state integrity, changing state schemas, investigating stale generated reports, or deciding which file owns a state fact.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.5
Last updated: 2026-06-14

## Purpose

State management keeps Precode useful without turning every useful file into active memory.

Active memory remains exactly:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

Everything else is either durable reference, durable task state, historical evidence, or generated summary.

Use `tasks/reference/INTENT-ORCHESTRATION-PROTOCOL.md` when state drift involves changed intent, unclear promotion from idea to PRD to bead, or follow-up work with no owner.

## State Ownership

| Layer | Owns | Does not own |
|---|---|---|
| Active memory | session entrypoint, hard decisions, current bead pointer | full history, generated summaries, broad project docs |
| Bead frontmatter | machine-readable bead state | narrative explanation |
| Bead sections | human execution contract and closeout | global product decisions |
| Bead Run Contract | risk-triggered allowed actions, proof needed, approval gates, and expiration | active memory, automatic command approval, or broader scope than the bead |
| PRDs and `FEATURES.md` | approved product definition and requirement inventory | active task selection |
| Goal Frames inside owner files | reviewed durable orientation for workflow selection | backlog, roadmap, implementation plan, approval, or active task |
| Reference docs | durable protocols and ownership rules | active execution state |
| JSON/JSONL logs | append-only historical evidence | instructions or task selection |
| Generated reports | compiled snapshots and warnings | authority, planning, or next-task decisions |

## Precedence Rules

- Frontmatter is canonical for machine state.
- Sections are canonical for the human-readable task contract.
- `tasks/todo.md` is the current pointer and current execution view.
- Bead files are the durable execution contracts.
- Bead Run Contract sections are canonical for risk-triggered execution policy when present.
- JSON/JSONL logs are historical evidence.
- Generated files are compiled snapshots only.
- `logs/run-contract.json` and `logs/run-contract.yaml` are generated execution profiles, not authority.
- `logs/ralph-attempts.jsonl` and `logs/ralph-summary.md` are generated Ralph attempt evidence, not review acceptance, command approval, task selection, or transition approval.
- `logs/work-graph.json` and `logs/work-graph.md` are generated relationship evidence, not task selection, transition approval, active memory, or a second tracker.
- Goal Frames inside owner files are advisory orientation. If stale or conflicting, they require reaffirmation before they guide workflow selection.
- If generated output conflicts with active memory or a bead, inspect the source file and regenerate the output.

## Open Question Ownership

- `DECISIONS.md`: hard unresolved product, technical, or operating-system decisions.
- PRD shard: product-definition questions.
- Bead: execution blockers for that bead.
- `tasks/todo.md`: only current execution blockers.
- Generated reports: summaries of missing or stale questions only.

Do not keep long-term decisions only in `tasks/todo.md`.

## Freshness Expectations

Generated reports should be refreshed after:

- recorded checks
- bead closeout updates
- bead transitions
- bead dependency, PRD, primary-authority, files-in-play, follow-up, or transition-proposal edits
- session start, checkpoint, handoff, or close events
- scheduled audits
- edits to authority contracts or reference protocols

Stale generated output is not wrong authority. It is a signal to regenerate before reviewing.

## Recovery Workflow

Use `tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md` when state repair needs to decide between review, closeout, unblocker, PRD amendment, bead split, or generated-report refresh.

Use `tasks/reference/LONG-HORIZON-PLANNING-PROTOCOL.md` when state repair discovers future or deferred work that should be summarized but not moved into active memory.

Use `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md` when state repair affects closeout, handoff, review decision, or transition readiness.

Use `tasks/reference/GOAL-FRAME-PROTOCOL.md` when state repair finds stale durable intent, a Goal Frame that looks like a task list, or generated next-step guidance relying on unreaffirmed direction.

When state looks inconsistent:

1. Load active memory only.
2. Identify the current bead from `tasks/todo.md`.
3. Compare todo frontmatter and sections with the bead frontmatter and sections.
4. Repair the canonical source, not the generated report.
5. Regenerate OS Health and scheduled audit output.
6. Run `bash scripts/validate-memory.sh`.
7. Record validation through `bash scripts/record-check.sh -- bash scripts/validate-memory.sh`.
8. Do not proceed to implementation until state is coherent enough to explain.

## Log And Archive Guidance

Raw JSONL logs are append-only evidence.

Generated summaries may be regenerated. They must not replace raw evidence when acceptance depends on the original command output, transition row, spend row, or audit row.

When logs become too large, archive old raw evidence under a clearly named archive location and keep generated summaries demoted. Archive policy must not rewrite active memory.

## State Integrity Checks

`scripts/state-check.py` is advisory. It may warn about todo/bead drift, stale generated reports, vague open questions, generated report demotion gaps, and active-memory drift.

Warnings are generated evidence only. They do not choose the next task or approve a transition.
