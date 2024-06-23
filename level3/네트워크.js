var n = 3;
var computers = [
  [1, 1, 0],
  [1, 1, 0],
  [0, 0, 1],
];
var graph = Array.from({ length: n }, () => new Set());
var visited = Array.from({ length: n }, () => false);

computers.forEach((row, i) => {
  row.forEach((connected, j) => {
    if (i != j && connected == 1) {
      graph[i].add(j);
      graph[j].add(i);
    }
  });
});

function bfs(node) {
  var queue = [node];
  visited[node] = true;

  while (queue.length) {
    var start = queue.shift();
    for (var end of graph[start]) {
      if (!visited[end]) {
        visited[end] = true;
        queue.push(end);
      }
    }
  }
}

var answer = 0;
for (let i = 0; i < n; i++) {
  if (!visited[i]) {
    answer++;
    bfs(i);
  }
}

console.log(answer);
