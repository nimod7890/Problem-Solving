// 코드 참고 .. Map().values().next()

/**
 * @param {string[]} gems
 */
function solution(gems) {
  const map = new Map();
  const gemSize = new Set(gems).size;

  let answer = [0, gems.length - 1];

  gems.forEach((gem, endIndex) => {
    map.delete(gem);
    map.set(gem, endIndex);
    if (map.size === gemSize) save(endIndex);
  });

  function save(endIndex) {
    const startIndex = map.values().next().value;
    const checking = answer[1] - answer[0] - (endIndex - startIndex);

    if (checking > 0 || (checking == 0 && answer[0] > startIndex)) {
      answer = [startIndex, endIndex];
    }
  }

  return [++answer[0], ++answer[1]];
}

// console.log(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]));
console.log(solution(["AA", "AB", "AC", "AA", "AC"]));
console.log(solution(["XYZ", "XYZ", "XYZ"]));
// console.log(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]));

/**
 * @param {string[]} gems
 * @description 굉장한 비효율
 */
function solution1(gems) {
  let gemSize = new Set(gems).size;

  let answer = [0, gems.length - 1];

  function dfs(start, end) {
    if (new Set(gems.slice(start, end + 1)).size == gemSize) {
      const checking = answer[1] - answer[0] - (end - start);
      if (checking > 0 || (checking == 0 && answer[0] > start)) {
        answer = [start, end];
      }
      return;
    }

    for (let i = start; i < gems.length; i++) {
      for (let j = end + 1; j < gems.length; j++) {
        dfs(i, j);
      }
    }
  }

  dfs(0, 0);
  return [++answer[0], ++answer[1]];
}
