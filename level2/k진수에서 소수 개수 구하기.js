// 에라토스테네스 -> 런타임에러

/**
 * @param {number} n
 * @param {number} k
 */
function solution(n, k) {
  const numArr = n.toString(k).split("0");
  return numArr.filter(isPrime).length;
}
const isPrime = (num) => {
  num = Number(num);
  if (num <= 1) return false;
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return true;
};

console.log(solution(437674, 3));
console.log(solution(110011, 10));
