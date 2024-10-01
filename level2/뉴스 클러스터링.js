// 중복허용 다중집합 부분에서 코드 참고

/**
 * @param {string} str1
 * @param {string} str2
 */
function solution(str1, str2) {
  let [first, second] = [[], []];

  for (let i = 0; i < Math.max(str1.length, str2.length); i++) {
    const [a, b] = [getString(str1, i), getString(str2, i)];
    isValid(a) && first.push(a);
    isValid(b) && second.push(b);
  }

  if (first.length == 0 && second.length == 0) {
    return 65536;
  }

  let [intersection, union] = [[], []];

  union = first.concat(second);

  // intersection
  first.forEach((value) => {
    const index = second.findIndex((sec) => value == sec);
    if (index >= 0) {
      intersection.push(value);
      second.splice(index, 1);
    }
  });

  // union
  intersection.forEach((value) => {
    const index = union.findIndex((uni) => value == uni);
    union.splice(index, 1);
  });

  return Math.floor((intersection.length / union.length) * 65536);
}

const getString = (str, i) =>
  str
    .slice(i, i + 2)
    .replace(/\s+/g, "")
    .toLowerCase();
const isValid = (str) => /[a-zA-Z][a-zA-Z]/g.test(str);

console.log(solution("FRANCE", "french"));
console.log(solution("handshake", "shake hands"));
console.log(solution("aa1+aa2", "AAAA12"));
console.log(solution("E=M*C^2", "e=m*c^2"));
