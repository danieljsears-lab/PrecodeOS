import { existsSync } from "node:fs";

const requiredDocs = [
  "docs/PRECODE-USER-GUIDE.md",
  "docs/CLAUDE-CODE-FIELD-GUIDE.md",
  "docs/PRECODE-TROUBLESHOOTING.md",
  "docs/PRECODE-GUIDED-SETUP.md",
  "docs/HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md",
  "FULL-LOOP-WORKSHEET.md",
];

const missing = requiredDocs.filter((path) => !existsSync(path));

if (missing.length > 0) {
  console.error(`Missing demo reference docs: ${missing.join(", ")}`);
  process.exit(1);
}

console.log("Docs check passed: PrecodeOS reference docs and the full loop worksheet are available.");
