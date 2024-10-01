/**
 * @param {string[]} records
 */
function solution(records) {
  const historyMap = new Map();
  const actionMap = {
    Leave: "님이 나갔습니다.",
    Enter: "님이 들어왔습니다.",
  };

  const parsedRecords = [];

  records.forEach((record) => {
    let [action, userId, nickName] = record.split(" ");

    switch (action) {
      case "Change":
        historyMap.set(userId, nickName);
        break;
      case "Enter":
        historyMap.set(userId, nickName);
      case "Leave":
        parsedRecords.push([action, userId]);
        break;
    }
  });

  return parsedRecords.map(([action, userId]) => `${historyMap.get(userId)}${actionMap[action]}`);
}

console.log(
  solution([
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan",
  ])
);
