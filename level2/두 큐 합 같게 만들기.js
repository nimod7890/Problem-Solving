// 답 보기 이전으로 돌아갈 수 없음..

/**
 * @param {number[]} queue1
 * @param {number[]} queue2
 */
function solution(queue1, queue2) {
  const sum = (queue) => queue.reduce((sum, value) => sum + value);

  let sum1 = sum(queue1);
  let half = (sum1 + sum(queue2)) / 2;

  let count = 0;
  let [i, j] = [0, queue1.length];

  const queue = [...queue1, ...queue2];
  while (half != sum1) {
    if (count >= queue.length * 3) return -1;

    if (half > sum1) {
      sum1 += queue[j];
      j++;
    } else {
      sum1 -= queue[i];
      i++;
    }

    count++;
  }

  return count;
}

console.log(solution([3, 2, 7, 2], [4, 6, 5, 1]));
console.log(solution([1, 2, 1, 2], [1, 10, 1, 2]));
console.log(solution([1, 1], [1, 5]));
