// 모범 답안 확인 후
// map, reduce -> some, forEach로 풀이 수정

const nearby = [
  [0, 1],
  [1, 0],
  [-1, 0],
  [0, -1],

  [1, 1],
  [-1, -1],
  [1, -1],
  [-1, 1],
];

function solution(board) {
  var answer = 0;

  board.forEach((column, i, self) =>
    column.forEach(
      (value, j) => value == 0 && !nearby.some(([y, x]) => self[y + i]?.[x + j] == 1) && answer++
    )
  );

  return answer;
}
