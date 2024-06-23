var n = 5;
var results = [
  [4, 3],
  [4, 2],
  [3, 2],
  [1, 2],
  [2, 5],
];

var graph = Array.from({ length: n + 1 }, () => [new Set(), new Set()]);

results.forEach(([winner, loser]) => {
  graph[winner][0].add(loser);
  graph[loser][1].add(winner);
});

for (let i = 1; i <= n; i++) {
  var losers = graph[i][0]; // i한테 진 애들 -> i를 이긴 애들(winners) 한테도 짐
  var winners = graph[i][1]; // i를 이긴 애들 -> i한테 진 애들한테도 이김

  for (var winner of winners) {
    losers.forEach((loser) => graph[winner][0].add(loser));
  }
  for (var loser of losers) {
    winners.forEach((winner) => graph[loser][1].add(winner));
  }
}

var answer = graph.reduce(
  (sum, [winners, losers]) => (winners.size + losers.size == n - 1 ? sum + 1 : sum),
  0
);
