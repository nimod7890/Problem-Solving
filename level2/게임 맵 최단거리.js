var maps = [
  [1, 0, 1, 1, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 1],
  [1, 1, 1, 0, 0],
  [0, 0, 0, 0, 1],
];

var [n, m] = [maps.length, maps[0].length];
var queue = [[0, 0]];
var near = [
  [0, -1],
  [-1, 0],
  [1, 0],
  [0, 1],
];

while (queue.length) {
  var [i, j] = queue.shift();

  if (i == n && j == m) {
    break;
  }

  for (var [Y, X] of near) {
    var [y, x] = [Y + i, X + j];
    if (0 <= y && y < n && 0 <= x && x < m && maps[y][x] == 1) {
      maps[y][x] = maps[i][j] + 1;
      queue.push([y, x]);
    }
  }
}
console.log(maps[n - 1][m - 1] == 1 ? -1 : maps[n - 1][m - 1]);
