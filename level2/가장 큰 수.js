var numbers = [3, 30, 34, 5, 9];
// var numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
var answer = numbers
  .map(String)
  .sort((a, b) => b + a - (a + b))
  .join("");

console.log(answer[0] == "0" ? "0" : answer);
