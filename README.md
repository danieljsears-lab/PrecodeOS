# PrecodeOS
<!-- ANCHOR: readme -->

[![Precode Validate](https://github.com/danieljsears-lab/PrecodeOS/actions/workflows/precode-validate.yml/badge.svg)](https://github.com/danieljsears-lab/PrecodeOS/actions/workflows/precode-validate.yml)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)

PrecodeOS is a repo-native Builder OS for AI coding agents that keeps intent, scope, approval, proof, and recovery visible inside the project.

It is for builders who want the speed of AI coding without handing the project over to the agent. PrecodeOS helps you know where you are, what happens next, what needs approval, what has been proven, and when to stop.

> AUTHORITY: Public GitHub landing page, beginner-first orientation, quickstart, and curated navigation for PrecodeOS.
> NOT_AUTHORITY: Active memory, product decisions, feature requirements, route structure, schema definitions, generated progress, task selection, or implementation acceptance.
> LOAD_WHEN: First opening the public repository, evaluating PrecodeOS, navigating major docs, or adapting PrecodeOS into a target project.
> CLASS: reference

## What It Is

PrecodeOS lives inside a project folder as readable Markdown files plus small validation scripts.

It gives AI-assisted work a shared operating model:

- tiny active memory
- one current task
- clear owner files for product and project truth
- optional discovery before PRD work
- small execution beads for build work
- recorded checks before acceptance
- human approval before task transitions
- recovery paths when state, scope, or proof feels wrong

The technical shorthand is: repo-native, markdown-canonical, script-enforced, and built to prevent quiet drift.

## Why It Matters

AI coding agents can move faster than a builder can understand, verify, and recover from. PrecodeOS keeps the project human-owned by making intent, scope, approval, proof, and recovery visible inside the repo.

That is the line PrecodeOS holds: the agent can inspect, draft, implement, explain, and propose, but the builder still owns direction, risk, approval, and acceptance.

## Start Here

If you are new to PrecodeOS, start with the Builder OS map:

- [`PRECODE-OS-README.md`](PRECODE-OS-README.md) explains the six rooms of PrecodeOS: Orient, Decide, Plan, Build, Prove, and Recover.

Then choose the guide that matches your role:

- New builder: [`HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md`](HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md)
- Day-to-day operator: [`PRECODE-USER-GUIDE.md`](PRECODE-USER-GUIDE.md)
- Claude Code student or bootcamp user: [`CLAUDE-CODE-FIELD-GUIDE.md`](CLAUDE-CODE-FIELD-GUIDE.md)
- Technical reviewer: [`PRECODE-ARCHITECTURE-OVERVIEW.md`](PRECODE-ARCHITECTURE-OVERVIEW.md)
- File-level navigator: [`PRECODE-FILE-INVENTORY.md`](PRECODE-FILE-INVENTORY.md)

## Quickstart

Clone the public repository and run the first memory check:

```bash
git clone https://github.com/danieljsears-lab/PrecodeOS.git
cd PrecodeOS
bash scripts/validate-memory.sh
```

To adapt PrecodeOS into a target project, start with these files:

- `PRODUCT.md` for the product promise, users, strategy, bets, success signals, and voice.
- `PROJECT-CONTEXT.md` for stack, app directory, conventions, checks, and integration boundaries.
- `DECISIONS.md` for hard decisions and open questions.
- `tasks/todo.md` for the active work pointer.

Do not add more active-memory files. If a topic needs durable detail, give it a clear owner file or use the existing reference map.

## How PrecodeOS Works

PrecodeOS keeps three files as active memory:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

Everything else is reference, template, evidence, adapter, archive, or generated output.

Normal work follows a simple path:

```text
orient -> decide -> plan -> build -> prove -> recover when needed
```

For implementation work, PrecodeOS uses beads: small execution contracts that name the current task, primary authority, files in play, checks, stop conditions, and proof needed.

For evidence, use recorded checks:

```bash
bash scripts/record-check.sh -- <command>
```

Generated reports such as `OS-HEALTH.md`, `PRECODE-HELP.md`, `PROGRESS.md`, and files under `logs/` are evidence only. They do not choose tasks, approve work, or replace owner files.

## Docs Map

| Need | Go to |
|---|---|
| Understand the Builder OS model | [`PRECODE-OS-README.md`](PRECODE-OS-README.md) |
| Learn how ideas become software with PrecodeOS | [`HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md`](HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md) |
| Operate a PrecodeOS repo day to day | [`PRECODE-USER-GUIDE.md`](PRECODE-USER-GUIDE.md) |
| Use Claude Code with PrecodeOS | [`CLAUDE-CODE-FIELD-GUIDE.md`](CLAUDE-CODE-FIELD-GUIDE.md) |
| Review architecture and trust boundaries | [`PRECODE-ARCHITECTURE-OVERVIEW.md`](PRECODE-ARCHITECTURE-OVERVIEW.md) |
| Find every file, protocol, script, and relationship | [`PRECODE-FILE-INVENTORY.md`](PRECODE-FILE-INVENTORY.md) |
| Contribute safely | [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| Understand governance | [`GOVERNANCE.md`](GOVERNANCE.md) |
| Use the name or describe a fork | [`TRADEMARK.md`](TRADEMARK.md) |

## For Reviewers And Contributors

PrecodeOS is designed to be inspectable:

- Markdown files hold human-readable authority.
- Scripts validate memory, version metadata, file inventory, public-repo hygiene, files in play, and completion evidence.
- GitHub Actions runs read-only validation on pushes and pull requests.
- Contribution policy is inbound = Apache-2.0.
- Maintainer review is required for governance, trademark, licensing, public positioning, active memory, core workflow semantics, generated-output demotion, and beginner-facing safety language.

Useful reviewer commands:

```bash
bash scripts/validate-memory.sh
python3 scripts/version-check.py
python3 scripts/file-inventory.py --check
python3 scripts/public-repo-check.py
```

## License, Trademark, And Provenance

PrecodeOS is open source under the Apache License 2.0. See [`LICENSE`](LICENSE) for terms and [`NOTICE`](NOTICE) for creator attribution.

Created by Dan Sears / Recode. Canonical site: <https://www.precodeos.org>.

PrecodeOS(TM) and Precode(TM) are trademarks of Dan Sears / Recode. Apache-2.0 does not grant trademark rights or permission to present a fork, derivative, product, service, or organization as official PrecodeOS. See [`TRADEMARK.md`](TRADEMARK.md).

## Document Metadata

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.21
Last updated: 2026-05-14
