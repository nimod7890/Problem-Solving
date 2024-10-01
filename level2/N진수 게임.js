/**
 * @param {number} n
 * @param {number} t
 * @param {number} m
 * @param {number} p
 */
function solution(n, t, m, p) {
  const answer = [];
  let i = 0;
  let cnt = 0;
  let str = "";
  while (answer.length < t) {
    str += cnt.toString(n);
    if (p - 1 == i) answer.push(str[cnt]);
    i = (i + m + 1) % m;
    cnt++;
  }
  return answer.join("").toUpperCase();
}

console.log(solution(2, 4, 2, 1));
console.log(solution(16, 16, 2, 1));
console.log(solution(16, 16, 2, 2));
