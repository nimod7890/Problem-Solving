var triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]];

var dp = Array(triangle.length + 1).fill(0);

triangle.reverse().forEach((nlist) => {
  dp = nlist.map((number, index) => Math.max(dp[index], dp[index + 1]) + number);
});
console.log(dp[0]);
