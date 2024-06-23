// 얘도 코드 맘에 안들었는데
// split 해서 개수를 세던가
// reduce 사용하는 코드도 있음

/**
 *
 * @param {string} s
 * @returns {boolean}
 */
function solution(s) {
  var p = 0;
  var y = 0;

  [...s.toLowerCase()].forEach((str) => {
    if (str == "p") {
      p++;
    }
    if (str == "y") {
      y++;
    }
  });

  return p == y;
}
