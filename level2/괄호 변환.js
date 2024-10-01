// isPerfect 부분은 맨 앞뒤만 비교해도 되긴하지만 정석으로 해도 풀리긴 함

/**
 * @param {string} p
 */
function solution(p) {
  function recursive(str) {
    if (str.length == 0) return "";
    let [u, v] = balancedSplit(str);
    v = recursive(v);
    if (isPerfect(u)) {
      return u + v;
    } else {
      return "(" + v + ")" + switchString(u.slice(1, u.length - 1));
    }
  }

  const getAddedNumber = (str) => (str == "(" ? 1 : -1);

  function balancedSplit(str) {
    let cnt = getAddedNumber(str[0]);

    for (let i = 1; i < str.length; i++) {
      cnt += getAddedNumber(str[i]);
      if (cnt == 0) return [str.slice(0, i + 1), str.slice(i + 1)];
    }

    return [str, ""];
  }

  function isPerfect(str) {
    let cnt = 0;
    for (const s of str) {
      cnt += getAddedNumber(s);
      if (cnt < 0) return false;
    }
    return true;
  }

  function switchString(str) {
    return [...str].map((s) => (s == "(" ? ")" : "(")).join("");
  }

  return recursive(p);
}

console.log(solution("(()())()"));
console.log(solution(")("));
console.log(solution("()))((()"));
