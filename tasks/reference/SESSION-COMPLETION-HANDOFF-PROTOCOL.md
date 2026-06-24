# PrecodeOS -- Session Completion And Handoff Protocol
<!-- ANCHOR: session-completion-handoff-protocol -->

> AUTHORITY: Session completion, bead closeout, review, transition proposal, transition approval, and agent handoff rules for PrecodeOS.
> NOT_AUTHORITY: Active memory expansion, product decisions, task selection, automatic review acceptance, automatic bead activation, generated progress state, or external mutations.
> LOAD_WHEN: Closing a session, checking whether a bead is ready for review, preparing an agent handoff, reviewing completion evidence, or deciding whether a transition proposal is safe to approve.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.16
Last updated: 2026-06-24

## Purpose

Completion and handoff keep the end of a session as structured as the start.

This protocol distinguishes orientation, evidence, review, and activation so a finished-sounding agent response does not become automatic task completion.

Active memory remains exactly:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

## Lifecycle Actions

| Action | May do | Must not do |
|---|---|---|
| Checkpoint | validate memory, summarize current bead, log checkpoint, refresh health | accept work, approve transition, start another bead |
| Session close | refresh closeout, record validation, assess promotion, log close, update learning diary | approve review, activate next bead, rewrite product scope |
| Bead closeout | record checks, result, manual verification, changed files, drift, lesson, follow-up, blocked escape | replace review decision or user approval |
| Review | decide `accepted`, `revise`, `split`, or `blocked` | bypass missing evidence or sensitive approval gates |
| Transition proposal | show whether the compiled readiness model permits a next bead | mutate bead state or `tasks/todo.md` |
| Transition approval | after user approval, move the current bead to `done` and the next bead to `in_progress` | run without explicit approval |
| Handoff | orient another agent with a Context Pack and generated-report warning | choose tasks, approve transitions, or activate work |

Review-intent phrases are review requests. If the active bead is still `in_progress` and the user asks "do you accept these changes?", "is this accepted?", "can I accept this?", or equivalent acceptance-review wording, the agent must switch the active bead to `review` first, present the Review / Acceptance output, and wait for a review decision. That wording must not mark the bead `done`, approve the review decision, approve transition, or activate the next bead.

## Required Completion Fields

Closeout Evidence should include:

- recorded checks
- Ralph attempt summary when the bead used Ralph
- result
- manual verification
- files changed
- next bead
- review decision
- drift observed
- lesson to promote
- prototype decision when the bead is exploratory: keep, revise, rebuild, discard, split, or promote learning to PRD/decision
- follow-up bead needed
- blocked escape
- evidence source
- allowed actions and proof needed when the bead has a Run Contract
- release-readiness note when the completed work may affect users, production, deployment, external services, docs needed for use, or post-release support
- accessibility advisory when the Accessibility Advisor was invoked, an owner file required it, or the review/release decision explicitly depends on it
- reference follow-through when public package files, protocols, docs, PRDs, beads, scripts, generated reading surfaces, or maintainer-roadmap work may require public reference-document or maintainer-history updates
- build attribution when accountability, teammate work, handoff, fresh-context review, or future traceability matters: human contributor, contributor role, agent/tool surface, attribution reviewer, and attribution uncertainty

For medium/high-risk code-changing beads, prefer a fresh-context review. The implementing context may be near its reasoning limit, so review should reload active memory, the bead, primary authority, parent PRD when relevant, and the diff or evidence from a clean context before acceptance.

Use `review_context` in bead frontmatter:

- `same_session_ok` — narrow low-risk work can be reviewed in the same session
- `fresh_context_recommended` — code-changing or medium-risk work should be reviewed after a context reset or handoff
- `fresh_context_required` — high-risk, sensitive, broad, or architecture-shaping work must be reviewed in a fresh context before acceptance

Manual verification should follow `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md` when it applies.

Release-relevant closeout should also follow `tasks/reference/RELEASE-READINESS-PROTOCOL.md`. The closeout should name changed behavior, affected users, smoke evidence, browser or manual verification, docs freshness, rollback or blocked escape, known uncertainty, post-release follow-up, and approval still required before any release action.

When release confidence depends on proving a requirement or behavior being shipped, or a non-functional expectation, closeout should also name the verification and release evidence path: requirement or behavior proven, evidence lane, recorded source, smoke path and result, docs/support freshness, rollback or blocked escape, approvals still required, decision state, and remaining uncertainty. Missing traceability means the work still needs evidence; it does not approve release, accept implementation, or make checker output proof.

When non-release acceptance confidence depends on a specific requirement ID, bug behavior, or acceptance criterion, closeout should include a compact requirement-to-proof trace: requirement, bug behavior, or acceptance criterion; evidence lane; recorded source; what this proves; what this does not prove; and remaining uncertainty. Missing traceability is a review concern only when the proof claim matters to acceptance confidence. It does not approve or reject work by itself, and it must not turn generated tests, generated properties, trace tables, screenshots, browser notes, AI critique, external status summaries, or generated reports into proof without recorded evidence or structured manual verification.

Accessibility advisory closeout is opt-in. Do not add it to every UI/interface bead by default. When invoked, record invocation decision, target, automated check evidence, manual review notes, unresolved findings, and acceptance risk. If the Accessibility Advisor Fit Interview recommends `not needed` or `defer`, record that decision only when it affects review, handoff, or release confidence.

Reference follow-through closeout is required when public package source changes may affect docs, protocols, package inventory, navigation indexes, generated HTML freshness, or maintainer-local public-package history. Record `Reference follow-through: resolved`, `deferred`, or `not applicable`, followed by the shortest useful reason. Public package source changes should review `_maintainer/CHANGELOG.md`; maintainer roadmap and roadmap-journal review is expected only when the bead, PRD, or closeout names roadmap or roadmap-candidate work. Generated HTML should be refreshed or checked from canonical Markdown; do not hand-edit generated reading surfaces as authority.

Small team closeout should also follow `tasks/reference/TEAM-COLLABORATION-PROTOCOL.md` when a teammate branch/worktree is involved. The contributor closeout should name the branch or worktree, assigned bead, coordinator or reviewer, files changed, checks, manual verification, owner-file impacts, conflicts with integration state, stale re-entry risks, and whether the next action is continue, review, split, block, or coordinator merge/re-entry review. `python3 scripts/team-collaboration-check.py` may provide preview evidence for these fields, but generated preview output is not acceptance, merge approval, or owner-file promotion.

Build attribution closeout should name who contributed the work, their role, which agent/tool surface assisted when known, who reviewed the attribution, and what uncertainty remains. `python3 scripts/build-attribution-ledger.py` and `logs/build-attribution-ledger.md/json` may summarize this evidence, but the generated ledger is not task authority, implementation acceptance, merge approval, release approval, contributor scoring, blame assignment, telemetry, or a registry.

Follow-up candidates from closeout should be routed to one of: `CANDIDATE-QUEUE.md`, PRD amendment, `DECISIONS.md`, authority-file update, explicit defer/kill note, or a candidate bead proposal after decomposition review. Do not hide follow-up work in `tasks/todo.md`, and do not treat a Candidate Queue entry as the next active bead.

For exploratory prototype beads, closeout must separate what the prototype demonstrated from what remains unproven. Record the prototype decision as `keep`, `revise`, `rebuild`, `discard`, `split`, or `promote learning to PRD/decision`, with the shortest useful reason. Keeping the prototype still needs review and acceptance; discarding or rebuilding it should preserve the learning and route follow-up through PRD amendment, Plan Loop, Hypothesis Review / Learning Loop, Candidate Queue, a decision, or candidate-bead decomposition.

When completed work later needs to be undone or superseded, use the Implemented Bead Reversal Workflow in `tasks/prds/PRD-023-implemented-bead-reversal-workflow.md`. The original bead remains `done` historical evidence. The reversal work must be a separate normal bead with its own primary authority, files in play, checks, manual verification, closeout, review decision, and generated journal entry.

Reversal closeout should name:

- Superseded bead
- Reversal target
- Reversal reason
- Preserved behavior
- Reversal proof
- Approvals still required

Do not reopen a `done` bead, delete evidence, rewrite transition logs, treat Git revert alone as proof, or use generated reports as reversal authority.

## Required Handoff Context Pack

A handoff should be able to explain:

- active bead
- state
- done-when
- primary authority
- files in play
- out of scope
- checks
- allowed actions and proof needed when the bead has a Run Contract
- stop conditions
- open questions
- latest evidence
- latest Ralph attempt decision when Ralph was used
- release-readiness status when the bead may ship to users
- verification and release evidence status when release confidence depends on traceable proof
- reversal target, reversal reason, preserved behavior, and reversal proof when the bead reverses already-implemented work
- teammate role, branch/worktree, coordinator, integration target, and merge/re-entry status when the Small Team Collaboration Lane applies
- blockers
- next safe action
- generated-report warning

The handoff packet is orientation only. The next agent still starts from active memory, the active bead, and the primary authority file.

For teammate handoff, generated handoff packets, team collaboration preview output, PR notes, branch status, and chat summaries remain orientation evidence. They do not approve merge, accept work, activate another bead, or promote teammate findings into owner files.

## Decision Outcomes

Use these outcomes at completion time:

- `continue`: keep working inside the active bead
- `close`: stop the session with current state recorded
- `review`: ask for evidence and acceptance review; review request wording must switch the active bead to `review` first when the bead is still `in_progress`
- `split`: create or propose a narrower follow-up bead
- `block`: mark missing input or blocker clearly
- `manual_testing`: wait for manual verification
- `transition_proposal`: show the next bead proposal without activation
- `transition_approval`: user explicitly approves `python3 scripts/bead-transition.py --approve`
- `handoff`: orient another agent without task activation

## Advisory Check

`scripts/completion-check.py` is advisory. It may warn about missing recorded checks, vague manual verification, invalid review decisions, unsafe next-bead references, follow-up work without a destination, vague handback, stale session close evidence, missing handoff Context Pack fields, transition eligibility that still needs user approval, blocked work without a clear escape path, or reference follow-through that needs review.

Reference follow-through warnings are closeout-readiness evidence. They may name impacted surface families, expected public reference-document checks, generated HTML freshness checks, maintainer changelog review, and roadmap/journal review when applicable. They do not update owner files, approve maintainer history, accept implementation, block or approve transition by themselves, or make generated output authoritative.

Ralph attempt evidence may support closeout and handoff, especially after repeated validator failures. It does not replace review acceptance, transition approval, or manual verification when those are required.

session-friction findings from `python3 scripts/session-friction-check.py` may support closeout and handoff review when repeated tool failures, stale evidence, generated-refresh gaps, or memory/context pressure affected the session. They are review input only: do not promote memory, edit owner files, do not approve commands, accept implementation, approve transition, or treat `logs/session-friction-review.json` as proof.

Session freshness is phase-aware. Evidence newer than the latest session close is reported as `open` detail while a bead is `in_progress`; it becomes a `stale` warning when the bead is in a close-oriented state such as `needs_info`, `manual_testing`, `review`, or `done`. A session close at or after the latest recorded check is `current`; a bead without recorded checks is `no-recorded-checks`.

Warnings are generated evidence only. They do not accept work, approve transitions, activate beads, change bead state, or rewrite active memory.
