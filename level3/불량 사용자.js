// dfs 오랜만

/**
 * @param {string[]} userIds
 * @param {string[]} bannedIds
 */
function solution(userIds, bannedIds) {
  const regex = bannedIds.map((id) => new RegExp(`^${id.replaceAll("*", ".")}$`));

  const isChecked = Array.from({ length: userIds.length }, () => false);
  const set = new Set();

  const bannedIdsLength = bannedIds.length;

  function dfs(ids, bannedIdx) {
    if (bannedIdx == bannedIdsLength) {
      set.add(ids.sort().join(","));
      return;
    }

    userIds.forEach((userId, index) => {
      if (!isChecked[index] && userId.match(regex[bannedIdx])) {
        isChecked[index] = true;
        dfs([...ids, userId], bannedIdx + 1);
        isChecked[index] = false;
      }
    });
  }

  dfs([], 0);

  return set.size;
}

console.log(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]));
console.log(
  solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])
);
console.log(
  solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])
);
