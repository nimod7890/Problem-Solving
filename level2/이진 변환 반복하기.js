// 정규식 왜 생각 안나는건데 !!

function solution(s) {
  s = [...s];
  let answer = [0, 0];
  let zeroCnt = 0;
  while (s != ["1"]) {
    [s, zeroCnt] = replay(s);
    answer = [answer[0] + 1, answer[1] + zeroCnt];
  }
  return answer;
}

function replay(before) {
  const after = [...before].filter((num) => num === "1").length;
  const cnt = before.length - after;
  return [after.toString(2), cnt];
}

// 이건 모범답안
/**
 *
 * @param {string} s
 */
function solution(s) {
  let answer = [0, 0];
  while (s != "1") {
    answer[0] += 1;
    answer[1] += (s.match(/0/g) || []).length;
    s = s.replace(/0/g, "").length.toString(2);
  }
  return answer;
}

console.log(solution("110010101001"));
console.log(solution("01110"));
console.log(solution("1111111"));
