var n = 6;
var vertex = [
  [3, 6],
  [4, 3],
  [3, 2],
  [1, 3],
  [1, 2],
  [2, 4],
  [5, 2],
];

var graph = new Map();
var distance = Array.from({ length: n + 1 }).fill(-1);

vertex.forEach((value) => {
  graph.set(value[0], [...(graph.get(value[0]) ?? []), value[1]]);
  graph.set(value[1], [...(graph.get(value[1]) ?? []), value[0]]);
});

var queue = [1];
distance[1] = 0;

while (queue.length) {
  var start = queue.shift();
  for (end of graph.get(start)) {
    if (distance[end] == -1) {
      distance[end] = distance[start] + 1;
      queue.push(end);
    }
  }
}

var maxi = Math.max(...distance);
var answer = distance.reduce((sum, value) => (value == maxi ? sum + 1 : sum), 0);

console.log(distance, answer);
