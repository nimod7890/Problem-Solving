var n = 7;
var wires = [
  [1, 2],
  [2, 7],
  [3, 7],
  [3, 4],
  [4, 5],
  [6, 7],
];
var tree = Array.from({ length: n + 1 }, () => []);
wires.forEach(([a, b]) => {
  tree[a].push(b);
  tree[b].push(a);
});

function bfs(root, except) {
  var cnt = 1;
  var visited = Array.from(n + 1).fill(false);
  var queue = [root];
  visited[root] = true;

  while (queue.length) {
    var start = queue.shift();
    for (var end of tree[start]) {
      if (!visited[end] && end != except) {
        visited[end] = true;
        queue.push(end);
        cnt++;
      }
    }
  }

  return cnt;
}

var ans = Number.MAX_SAFE_INTEGER;
wires.forEach(([a, b]) => {
  ans = Math.min(bfs(a, b), ans);
});

console.log(ans);
