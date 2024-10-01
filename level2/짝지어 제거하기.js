// stack !!

/*
function solution(s) {
  // 시초 !
  const reg = /(.)\1/g;
  while (reg.test(s)) {
    s = s.replaceAll(reg, "");
    if (s.length === 0) return 1;
  }
  return 0;
}
*/

/**
 *
 * @param {string} s
 */
function solution(s) {
  const stack = [];

  for (let letter of s) {
    if (stack.length > 0 && stack[stack.length - 1] == letter) {
      stack.pop();
    } else {
      stack.push(letter);
    }
  }

  return stack.length === 0 ? 1 : 0;
}

console.log(solution("baabaa"));
console.log(solution("aabbcc"));
console.log(solution("cdcd"));
