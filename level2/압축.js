/**
 * @param {string} msg
 */
function solution(msg) {
  const answer = [];
  const dictionary = [
    0,
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
  ];

  for (var i = 0; i < msg.length; i++) {
    for (var j = msg.length; j > i; j--) {
      const search = msg.slice(i, j);
      const index = dictionary.findIndex((value) => value == search);
      if (index < 0) continue;
      answer.push(index);
      dictionary.push(msg.slice(i, j + 1));
      i += j - i - 1;
      break;
    }
  }

  return answer;
}

// console.log(solution("KAKAO"));
// console.log(solution("TOBEORNOTTOBEORTOBEORNOT"));
console.log(solution("ABABABABABABABAB"));
