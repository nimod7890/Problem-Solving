// 이분탐색 싫다 ..

/**
 * @param {number[]} stones
 * @param {number} k
 */
function solution(stones, k) {
  let left = 1;
  let right = 200000000;

  while (left < right - 1) {
    let mid = Math.floor((left + right) / 2);
    available(mid) ? (left = mid) : (right = mid);
  }

  function available(mid) {
    let count = 0;
    for (let i = 0; i < stones.length; i++) {
      stones[i] < mid ? count++ : (count = 0);
      if (count >= k) return false;
    }
    return true;
  }

  return left;
}

console.log(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3));
