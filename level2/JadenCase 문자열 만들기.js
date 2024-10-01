/**
 * @param {string} s
 */
function solution(s) {
  return s
    .split(" ")
    .map((word) => capitalize(word))
    .join(" ");
}

function capitalize(word) {
  return word.charAt(0).toUpperCase() + word.substring(1).toLowerCase();
}

console.log(solution(" 3people  unFollowed me"));
console.log(solution("for  the last week"));
console.log(solution(" a b "));
console.log(solution(" "));
console.log(solution(" for the what 1what  "));
