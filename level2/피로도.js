var k = 80;

var dungeons = [
  [80, 20],
  [50, 40],
  [30, 10],
];

var ans = 0;
var visited = Array.from(dungeons.length).fill(false);

function dfs(cnt, k) {
  for (let i = 0; i < dungeons.length; i++) {
    if (!visited[i] && k - dungeons[i][0] >= 0) {
      visited[i] = true;
      dfs(cnt + 1, k - dungeons[i][1]);
      visited[i] = false;
    }
  }

  ans = Math.max(cnt, ans);
}

dfs(0, k);

console.log(ans);
