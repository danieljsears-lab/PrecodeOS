#!/usr/bin/env node
// Version: v0.1.3
// Last updated: 2026-07-31
// Owner: PrecodeOS
// Created by Dan Sears / Recode.
// SPDX-License-Identifier: Apache-2.0
import { fileURLToPath } from "node:url";
import { dirname, resolve } from "node:path";
import { spawnSync } from "node:child_process";

const BIN_DIR = dirname(fileURLToPath(import.meta.url));
const PACKAGE_ROOT = resolve(BIN_DIR, "..");
const BOUNDARY_NOTE =
  "precodeos is an optional npm entry for PrecodeOS setup, fast verified setup, upgrade, update-plan previews, " +
  "approved SP-ID or UP-ID copy delegation, and local usage-evidence review. It delegates to Python scripts; " +
  "preview and review output, including updater compatibility policy metadata, is generated evidence only.";

function usage() {
  return `Usage:
  precodeos setup-preview --target <target-project-root> [--json]
  precodeos fast-setup-preview --target <target-project-root> [--json]
  precodeos fast-setup-apply --target <target-project-root> --approve-action <SP-ID|UP-ID> [--approve-action <SP-ID|UP-ID> ...] [--json]
  precodeos upgrade-preview --target <existing-precode-root> [--json]
  precodeos update-plan-preview --target <existing-precode-root> [--json]
  precodeos apply-package-owned --target <existing-precode-root> --approve-action <UP-ID> [--approve-action <UP-ID> ...] [--json]
  precodeos usage-evidence-review [--json]

Boundary:
  Preview commands are read-only by default. Fast setup apply delegates only explicitly
  approved current SP-ID or UP-ID copy actions to the Python source of truth.
  Apply-package-owned remains the existing explicit approved package-owned UP-ID delegation.
  No postinstall behavior, dirty-file overwrite, owner-file adaptation, hook installation,
  CI mutation, app commands, app-code edits, executable release-channel behavior, package-manager
  updates, npm registry lookup, dist-tag resolution, broad npm updater behavior, rollback automation,
  telemetry collection, evidence submission, issue creation, task selection, PRD approval, or bead activation.
`;
}

function parseArgs(argv) {
  const [command, ...rest] = argv;
  if (!command || command === "--help" || command === "-h" || command === "help") {
    return { command: "help", target: "", json: false };
  }
  if (!["setup-preview", "fast-setup-preview", "fast-setup-apply", "upgrade-preview", "update-plan-preview", "apply-package-owned", "usage-evidence-review"].includes(command)) {
    throw new Error(`unknown command: ${command}`);
  }
  let target = "";
  let json = false;
  const approveActions = [];
  for (let index = 0; index < rest.length; index += 1) {
    const value = rest[index];
    if (value === "--target") {
      target = rest[index + 1] || "";
      index += 1;
    } else if (value === "--json") {
      json = true;
    } else if (value === "--approve-action") {
      const action = rest[index + 1] || "";
      if (!action) {
        throw new Error("--approve-action requires <UP-ID>");
      }
      approveActions.push(action);
      index += 1;
    } else {
      throw new Error(`unknown argument: ${value}`);
    }
  }
  if (command !== "usage-evidence-review" && !target) {
    throw new Error(`${command} requires --target <target-project-root>`);
  }
  if (!["fast-setup-apply", "apply-package-owned"].includes(command) && approveActions.length > 0) {
    throw new Error("--approve-action is only valid with fast-setup-apply or apply-package-owned");
  }
  if (command === "fast-setup-apply" && approveActions.length === 0) {
    throw new Error("fast-setup-apply requires at least one --approve-action <SP-ID|UP-ID>");
  }
  if (command === "apply-package-owned" && approveActions.length === 0) {
    throw new Error("apply-package-owned requires at least one --approve-action <UP-ID>");
  }
  return { command, target, json, approveActions };
}

function commandFor(parsed) {
  if (parsed.command === "usage-evidence-review") {
    const command = ["python3", "scripts/usage-evidence-review.py"];
    if (parsed.json) {
      command.push("--json");
    }
    return command;
  }
  const command = [
    "python3",
    "scripts/bootstrap-check.py",
    "--source",
    PACKAGE_ROOT,
    "--target",
    parsed.target,
  ];
  if (parsed.command === "setup-preview") {
    command.push("--supervised-setup-plan");
  } else if (parsed.command === "fast-setup-preview") {
    command.push("--fast-verified-setup-preview");
  } else if (parsed.command === "fast-setup-apply") {
    command.push("--fast-verified-setup-apply");
    for (const action of parsed.approveActions) {
      command.push("--approve-action", action);
    }
  } else if (parsed.command === "upgrade-preview") {
    command.push("--upgrade-preview");
  } else if (parsed.command === "update-plan-preview") {
    command.push("--update-plan-preview");
  } else if (parsed.command === "apply-package-owned") {
    command.push("--upgrade-preview", "--apply-upgrade-preview");
    for (const action of parsed.approveActions) {
      command.push("--approve-action", action);
    }
  }
  if (parsed.json) {
    command.push("--json");
  }
  return command;
}

function shellQuote(value) {
  if (/^[A-Za-z0-9_./:@%+=,-]+$/.test(value)) {
    return value;
  }
  return `'${value.replaceAll("'", "'\\''")}'`;
}

function main() {
  let parsed;
  try {
    parsed = parseArgs(process.argv.slice(2));
  } catch (error) {
    console.error(`precodeos: ${error.message}`);
    console.error(usage());
    return 2;
  }
  if (parsed.command === "help") {
    console.log(usage());
    return 0;
  }
  const command = commandFor(parsed);
  console.log(BOUNDARY_NOTE);
  console.log(`Underlying command: ${command.map(shellQuote).join(" ")}`);
  const result = spawnSync(command[0], command.slice(1), {
    cwd: PACKAGE_ROOT,
    env: process.env,
    stdio: "inherit",
  });
  if (result.error) {
    console.error(`precodeos: ${result.error.message}`);
    return 1;
  }
  return result.status ?? 1;
}

process.exitCode = main();
