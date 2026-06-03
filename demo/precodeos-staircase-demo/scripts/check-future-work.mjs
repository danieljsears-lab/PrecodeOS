import { existsSync, readFileSync } from "node:fs";

const todo = readFileSync("tasks/todo.md", "utf8");
const features = readFileSync("FEATURES.md", "utf8");

const isB001 = todo.includes("current_bead: tasks/beads/B001-validate-precode-readiness.md");
const isB002 = todo.includes("current_bead: tasks/beads/B002-add-difficulty-filter.md");
const requiredCandidates = [
  "Save Favorite Staircases",
  "Sort Staircases By Climb Time",
  "Add Neighborhood Filter",
  "Add Staircase Detail View",
  "Share A Staircase Route",
];
const proposedBeads = [
  "tasks/beads/B003-mark-staircase-visited.md",
  "tasks/beads/B004-sort-by-climb-time.md",
  "tasks/beads/B005-add-neighborhood-filter.md",
  "tasks/beads/B006-add-staircase-detail-view.md",
  "tasks/beads/B007-share-staircase-route.md",
];
const candidateCount = (features.match(/^### /gm) || []).length;
const inactiveCount = (features.match(/^- Active: no$/gm) || []).length;

if (!isB001 && !isB002) {
  console.error("Expected active bead to be B001 before capture or B002 during future work capture.");
  process.exit(1);
}

if (candidateCount < 5) {
  console.error(`Expected at least 5 future candidates in FEATURES.md, found ${candidateCount}.`);
  process.exit(1);
}

const missingCandidates = requiredCandidates.filter((candidate) => !features.includes(`### ${candidate}`));

if (missingCandidates.length > 0) {
  console.error(`Missing expected future candidates: ${missingCandidates.join(", ")}.`);
  process.exit(1);
}

if (inactiveCount < candidateCount) {
  console.error(`Expected every future candidate to be inactive. Candidates: ${candidateCount}; inactive markers: ${inactiveCount}.`);
  process.exit(1);
}

if (features.includes("Status: in_progress") || features.includes("Active: yes")) {
  console.error("FEATURES.md appears to activate future work.");
  process.exit(1);
}

const missingBeads = proposedBeads.filter((path) => !existsSync(path));

if (missingBeads.length > 0) {
  console.error(`Missing proposed bead files: ${missingBeads.join(", ")}.`);
  process.exit(1);
}

const activeLaterBeads = proposedBeads.filter((path) => {
  const bead = readFileSync(path, "utf8");
  return !bead.includes("status: proposed") || bead.includes("> CLASS: active-task");
});

if (activeLaterBeads.length > 0) {
  console.error(`Later beads must remain proposed and inactive: ${activeLaterBeads.join(", ")}.`);
  process.exit(1);
}

if (isB002) {
  console.log(`Future work check passed: ${candidateCount} FEATURES.md candidates are inactive, B003-B007 remain proposed, and B002 remains active.`);
} else {
  console.log(`Future work check passed: ${candidateCount} FEATURES.md candidates are inactive and B003-B007 remain proposed before B002 is activated.`);
}
