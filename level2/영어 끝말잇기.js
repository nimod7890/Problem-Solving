/**
 * @param {number} n
 * @param {Array<string>} words
 */
function solution(n, words) {
  const wordHistory = [words[0]];
  for (let i = 1; i < words.length; i++) {
    const word = words[i];

    if (
      !wordHistory.includes(word) &&
      words[i - 1].charAt(words[i - 1].length - 1) == word.charAt(0)
    ) {
      wordHistory.push(word);
      continue;
    }
    return [(i % n) + 1, Math.ceil((i + 1) / n)];
  }
  return [0, 0];
}

console.log(
  solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])
);
console.log(
  solution(5, [
    "hello",
    "observe",
    "effect",
    "take",
    "either",
    "recognize",
    "encourage",
    "ensure",
    "establish",
    "hang",
    "gather",
    "refer",
    "reference",
    "estimate",
    "executive",
  ])
);
console.log(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]));
