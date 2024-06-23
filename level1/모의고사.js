var answers = [1, 3, 2, 4, 2];

var submits = [
  [1, 2, 3, 4, 5],
  [2, 1, 2, 3, 2, 4, 2, 5],
  [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
];
var scores = answers.reduce(
  ([a, b, c], answer, i) => [
    submits[0][i % 5] == answer ? a + 1 : a,
    submits[1][i % 8] == answer ? b + 1 : b,
    submits[2][i % 10] == answer ? c + 1 : c,
  ],
  [0, 0, 0]
);

var maxi = Math.max(...scores);
console.log(
  scores.map((value, index) => (value === maxi ? index + 1 : -1)).filter((index) => index !== -1)
);
