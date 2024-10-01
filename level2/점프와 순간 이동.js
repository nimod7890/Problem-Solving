// 구현만 하지말고 효율성 고려하기

/* 런타임에러 시초 .. ~ !
function solution(n) {
  const dp = [0, 1];
  for (let i = 2; i <= n; i++) {
    dp.push(i % 2 == 0 ? Math.min(dp[i - 1] + 1, dp[i / 2]) : dp[i - 1] + 1);
  }
  return dp.pop();
}
*/

/**
 * @description 나의 한계 ..
 * @param {number} n
 */
function solution(n) {
  let cnt = 0;
  while (n > 0) {
    if (n % 2 == 0) {
      n /= 2;
    } else {
      n -= 1;
      cnt += 1;
    }
  }
  return cnt;
}

/* 그리고 멋진 풀이
function solution(n) {
  return n.toString(2).replace(/0/g, "").length;
}
 */
console.log(solution(1));
console.log(solution(2));
console.log(solution(5));
console.log(solution(6));
console.log(solution(5000));

/*
0 1 2 3 4 5
0 1 1   1 2
*/
