// 아무튼 .. 반성해라 ..

/**
 *
 * @param {Array<number>} arr
 */
function solution(arr) {
  return arr.reduce((answer, value) => lcm(answer, value), 1);
}

function lcm(a, b) {
  return (a * b) / gcd(a, b);
}

function gcd(a, b) {
  // return a % b ? gcd(b, a%b) : b
  if (b == 0) {
    return a;
  }
  if (a % b == 0) {
    return b;
  }
  return gcd(b, a % b);
}

console.log(solution([2, 6, 8, 14]));
console.log(solution([1, 2, 3]));
console.log(solution([2, 2, 7, 14]));
console.log(solution([2, 4, 8, 16]));
