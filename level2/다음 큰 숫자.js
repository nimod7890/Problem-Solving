/**
 *
 * @param {number} n
 */
function solution(n) {
  const nbitCnt = n.toString(2).match(/1/g).length;
  while (true) {
    n++;
    if (nbitCnt === n.toString(2).match(/1/g).length) return n;
  }
}

console.log(solution(78));
console.log(solution(15));
