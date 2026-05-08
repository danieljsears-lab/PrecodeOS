# Precode OS -- Tool Execution Protocol
<!-- ANCHOR: tool-execution-protocol -->

> AUTHORITY: Tool-call classes, command policy expectations, non-check tool logging, failure categories, external mutation rules, secret handling, and tool-execution advisory checks for Precode OS.
> NOT_AUTHORITY: Active memory expansion, task selection, product decisions, implementation plans, automatic command approval, generated progress state, or automatic bead transitions.
> LOAD_WHEN: Choosing, recording, reviewing, or approving tool calls; adding tool integrations; handling command failures; or distinguishing tool use from verification evidence.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.2
Last updated: 2026-05-06

## Purpose

Tool execution keeps Precode honest about what an agent actually ran.

A command can be useful without proving the work is done. Precode separates:

- tool use: an action happened
- verification evidence: a check proved something and was recorded
- user approval: a human approved a risky action

Active memory remains exactly:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

## Tool-Call Classes

Use these classes when describing important tool calls:

| Class | Meaning |
|---|---|
| `read_only` | Inspects local or external state without changing it. |
| `verification` | Runs a check intended to prove behavior or integrity. |
| `generated_refresh` | Refreshes generated reports or sidecars. |
| `local_mutation` | Changes local files, dependencies, state, generated artifacts, or repo configuration. |
| `external_mutation` | Changes GitHub, CI, deployments, dashboards, hosted services, issue trackers, or other external systems. |
| `destructive` | Deletes, resets, drops, force-pushes, rolls back, migrates destructively, or otherwise risks irreversible loss. |
| `secret_bearing` | Handles secrets, tokens, credentials, dashboard values, private exports, or sensitive raw output. |

## Command Policy In Beads

When a bead expects risky tools, the bead should name:

- allowed commands
- forbidden commands
- approval-required commands
- expected side effects
- rollback, cleanup, or blocked escape notes

Low-risk doc or validation beads can rely on the normal `Checks`, `Stop If`, and `Closeout Evidence` sections. Sensitive or external work should be explicit before the command runs.

## Evidence Distinction

`logs/check-results.jsonl` is the verification ledger. It records commands run through:

```text
bash scripts/record-check.sh -- <command>
```

`logs/tool-runs.jsonl` is a general tool-use ledger. It records important tool actions that may or may not be verification evidence.

A logged tool run does not count as a passing check unless it is also recorded through `record-check.sh` or accepted in Closeout Evidence with the required manual verification format.

Guardrail checks such as `python3 scripts/files-in-play-check.py`, `python3 scripts/bead-depth-check.py`, and `python3 scripts/next-step.py` are advisory evidence. They can warn, orient, or suggest a pause, but they do not approve commands, authorize out-of-scope edits, or replace explicit user approval for sensitive or external mutation.

`python3 scripts/files-in-play-check.py --command "<command summary>"` may classify a command as `continue`, `approval needed`, or `stop`. That classification is a beginner-facing stop sign, not permission. If it says approval is needed or stop, the agent must pause and ask for explicit user approval or a narrower path before running the command.

`python3 scripts/files-in-play-check.py --edit-lock` is also advisory. It compares current changed paths with the active bead's `files_in_play` and generated-output exceptions. It does not create a filesystem lock, approve edits, or replace human review.

## Failure Categories

Use these categories for failed or blocked tool runs:

- `code_failure`
- `unavailable_command`
- `missing_dependency`
- `missing_credentials`
- `network_unavailable`
- `permission_or_sandbox_blocked`
- `user_approval_required`
- `destructive_action_blocked`
- `unknown`

Unknown is acceptable only when the failure cannot be classified yet.

## External Mutation Rules

External mutations require all of these:

- an approved bead names the external system
- the exact action or command is in scope
- the expected effect is clear
- the rollback or undo path is named, or the reason rollback is impossible is recorded
- the user approves the manual gate
- post-action evidence is recorded

Scheduled audits, importers, generated reports, and advisory checks must remain read-only.

## Secret Handling

Never store secrets, tokens, credentials, dashboard values, private keys, raw private transcripts, or sensitive raw command output in `logs/tool-runs.jsonl`.

If a tool touches secrets, log only that the action was `secret_bearing`, whether it was approved, and where safe redacted evidence lives.

## Logging Tool Runs

Use:

```text
bash scripts/log-tool-run.sh --tool <tool> --class <class> --status <pass|fail|blocked> --command "<summary>"
```

Use `--dry-run` before writing when checking the shape.

Prefer concise command summaries over raw shell with secrets or private paths. Use `output_ref` only for safe, redacted artifacts.

## Advisory Check

`scripts/tool-execution-check.py` is advisory. It may warn about approval gaps, destructive actions, missing failure categories, vague checks, generated refresh without verification evidence, or stale command evidence.

Warnings are generated evidence only. They do not approve tool calls, select tasks, or replace user judgment.
