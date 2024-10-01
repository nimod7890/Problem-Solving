var priorities = [2, 1, 3, 2];
var location = 2;

var queue = priorities.map((value, index) => [value, index]);
var sorted = priorities.sort((a, b) => b - a);

var node = null;
var cnt = 0;

while (queue.length) {
  node = queue.shift();

  if (node[0] != sorted[cnt]) {
    queue.push(node);
  } else {
    cnt++;
    if (node[1] == location) {
      break;
    }
  }
}
