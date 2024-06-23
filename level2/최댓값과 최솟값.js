const s = "1 2 3 4";
const arr = s.split(" ").map(Number);
console.log([Math.min(...arr), Math.max(...arr)].join(" "));
