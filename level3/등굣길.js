var m = 4;
var n = 3;
var puddles = [[2, 2]];
// return 4

var dp = Array.from({ length: n }, () => []);
dp[0] = Array.from({ length: m }, (_, j) => j + 1);
console.log(dp);
puddles.forEach(([i, j]) => (dp[i - 1][j - 1] = -1));

for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    if (dp[i][j] != -1) {
      if (dp[i - 1][j] == -1 && dp[i][j - 1] == -1) {
        dp[i][j] = -1;
      } else if (dp[i - 1][j] == -1 && dp[i][j - 1] != -1) {
        dp[i][j] = dp[i][j - 1] + 1;
      } else if (dp[i - 1][j] != -1 && dp[i][j - 1] == -1) {
        dp[i][j] = dp[i - 1][j] + 1;
      } else {
        dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1]) + 1;
      }
    }
  }
}
console.log(dp);
console.log(dp[n][m]);
