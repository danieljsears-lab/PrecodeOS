#!/usr/bin/env node
// Version: v0.1.0
// Last updated: 2026-07-24
// Owner: PrecodeOS
// Created by Dan Sears / Recode.
// SPDX-License-Identifier: Apache-2.0
import { fileURLToPath } from "node:url";
import { dirname, resolve } from "node:path";
import { spawnSync } from "node:child_process";

const BIN_DIR = dirname(fileURLToPath(import.meta.url));
const PACKAGE_ROOT = resolve(BIN_DIR, "..");
const BOUNDARY_NOTE =
  "precodeos is an optional npm entry for read-only PrecodeOS setup and upgrade previews. " +
  "It delegates to scripts/bootstrap-check.py; preview output is generated evidence only.";

function usage() {
  return `Usage:
  precodeos setup-preview --target <target-project-root> [--json]
  precodeos upgrade-preview --target <existing-precode-root> [--json]

Boundary:
  No postinstall behavior, target mutation, owner-file adaptation, hook installation,
  CI mutation, app commands, app-code edits, release-channel semantics, package-manager
  updates, rollback automation, task selection, PRD approval, or bead activation.
`;
}

function parseArgs(argv) {
  const [command, ...rest] = argv;
  if (!command || command === "--help" || command === "-h" || command === "help") {
    return { command: "help", target: "", json: false };
  }
  if (!["setup-preview", "upgrade-preview"].includes(command)) {
    throw new Error(`unknown command: ${command}`);
  }
  let target = "";
  let json = false;
  for (let index = 0; index < rest.length; index += 1) {
    const value = rest[index];
    if (value === "--target") {
      target = rest[index + 1] || "";
      index += 1;
    } else if (value === "--json") {
      json = true;
    } else {
      throw new Error(`unknown argument: ${value}`);
    }
  }
  if (!target) {
    throw new Error(`${command} requires --target <target-project-root>`);
  }
  return { command, target, json };
}

function commandFor(parsed) {
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
  } else if (parsed.command === "upgrade-preview") {
    command.push("--upgrade-preview");
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
