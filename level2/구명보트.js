/**
 * @param {Array<number>} people
 * @param {number} limit
 */
function solution(people, limit) {
  people.sort((a, b) => b - a);
  let [left, right] = [0, people.length - 1];
  let minCount = 0;
  while (left <= right) {
    if (left == right || limit >= people[left] + people[right]) {
      right--;
    }
    minCount++;
    left++;
  }

  return minCount;
}

console.log(solution([70, 50, 80, 50], 100));
console.log(solution([70, 80, 50], 100));
