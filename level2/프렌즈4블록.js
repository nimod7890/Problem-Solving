/**
 * @param {number} m
 * @param {number} n
 * @param {string[][]} boards
 */
function solution(m, n, boards) {
  const dydx = [
    [0, 0],
    [0, -1],
    [-1, -1],
    [-1, 0],
  ];

  boards = boards.map((v) => v.split(""));

  while (true) {
    let willBeRemovedBlocks = [];

    if (!search()) break;

    deleteBlocks();
    setBoards();

    function search() {
      function canBeRemoved(i, j) {
        const arr = dydx.map(([x, y]) => boards[x + i][y + j]);
        if (new Set(arr).size == 1) {
          willBeRemovedBlocks.push([i, j]);
          return true;
        }
        return false;
      }

      let again = false;
      for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
          boards[i][j] != 0 && canBeRemoved(i, j) && (again = true);
        }
      }

      return again;
    }
    function deleteBlocks() {
      willBeRemovedBlocks.forEach(([i, j]) => {
        dydx.forEach(([x, y]) => (boards[x + i][y + j] = 0));
      });
    }
    function setBoards() {
      // 이 부분에서 j -> i 로 접근해서 막혔음
      for (let i = m - 1; i > 0; i--) {
        if (!boards[i].some((v) => !v)) continue;
        for (let j = 0; j < n; j++) {
          for (let k = i - 1; k >= 0 && !boards[i][j]; k--) {
            if (boards[k][j]) {
              boards[i][j] = boards[k][j];
              boards[k][j] = 0;
              break;
            }
          }
        }
      }
    }
  }

  return boards.flat().filter((element) => element === 0).length;
}

console.log(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]));
console.log(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]));
