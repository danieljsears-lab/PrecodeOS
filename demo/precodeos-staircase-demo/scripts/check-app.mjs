import { readFileSync } from "node:fs";

const html = readFileSync("index.html", "utf8");
const app = readFileSync("src/app.js", "utf8");

const cardCount = (html.match(/class="stair-card"/g) || []).length;
const difficulties = ["easy", "moderate", "hard"];
const missingDifficulties = difficulties.filter(
  (difficulty) => !html.includes(`data-difficulty="${difficulty}"`),
);

if (cardCount < 4) {
  console.error(`Expected at least 4 seeded staircase cards, found ${cardCount}.`);
  process.exit(1);
}

if (missingDifficulties.length > 0) {
  console.error(`Missing seeded difficulty values: ${missingDifficulties.join(", ")}.`);
  process.exit(1);
}

if (!app.includes("querySelectorAll")) {
  console.error("Expected src/app.js to inspect staircase cards.");
  process.exit(1);
}

console.log("App check passed: seeded staircase cards are present.");
