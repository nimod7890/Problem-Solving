// common[common.length - 1] 대신 pop 쓰기

/**
 *
 * @param {Array<number>} common
 * @returns
 */
function solution(common) {
  if (common[2] - common[1] == common[1] - common[0]) {
    return common.pop() + common[1] - common[0];
  }
  return common.pop() * (common[1] / common[0]);
}

console.log(solution([2, 4, 8]));
console.log(solution([1, 2, 3, 4]));
