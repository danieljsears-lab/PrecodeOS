const cards = Array.from(document.querySelectorAll(".stair-card"));

function summarizeStaircases() {
  const counts = cards.reduce((summary, card) => {
    const difficulty = card.dataset.difficulty || "unknown";
    summary[difficulty] = (summary[difficulty] || 0) + 1;
    return summary;
  }, {});

  console.info("Seeded staircase cards:", counts);
}

summarizeStaircases();
