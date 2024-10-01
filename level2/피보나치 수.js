// 이전 값 기억 불필요

/**
 *
 * @param {number} n
 */
function solution(n) {
  const array = [0, 1];
  if (n < 3) return array[n - 1];
  for (let i = 2; i <= n; i++) {
    array.push((array[i - 1] + array[i - 2]) % 1234567);
  }
  return array.pop();
}

console.log(solution(3));
console.log(solution(5));
