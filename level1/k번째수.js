var array = [1, 5, 2, 6, 3, 7, 4];
var commands = [
  [2, 5, 3],
  [4, 4, 1],
  [1, 7, 3],
];

console.log(
  commands.map(
    (value) => [...array].slice(value[0] - 1, value[1]).sort((a, b) => a - b)[value[2] - 1]
  )
);
