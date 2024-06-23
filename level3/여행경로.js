// 백트래킹까지는 생각했는데 디테일이 좀 부족했ㅅ

var tickets = [
  ["ICN", "SFO"],
  ["ICN", "ATL"],
  ["SFO", "ATL"],
  ["ATL", "SFO"],
  ["ATL", "ICN"],
];

var path = new Map();

tickets.forEach(([start, end]) => {
  if (!path.has(start)) path.set(start, []);
  path.get(start).push(end);
});

path.forEach((value, key) => {
  path.set(key, value.sort());
});

var result = ["ICN"];

function backtracking(start) {
  if (result.length == tickets.length + 1) {
    return true;
  }

  if (!path.has(start)) {
    return false;
  }

  var destinations = path.get(start);
  for (let i = 0; i < destinations.length; i++) {
    var end = destinations[i];
    result.push(end);
    destinations.splice(i, 1);
    if (backtracking(end)) {
      return true;
    }
    result.pop();
    destinations.splice(i, 0, end);
  }
}

backtracking("ICN");
