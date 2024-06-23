function solution(numbers) {
  return getNumberList(numbers).filter((v) => isPrime(v)).length;
}

function getNumberList(str) {
  const answer = new Set();
  const n = str.length;
  let ch = Array.from(n).fill(false);

  function dfs(curStr) {
    answer.add(+curStr);
    for (let i = 0; i < n; i++) {
      if (!ch[i]) {
        ch[i] = true;
        dfs(curStr + str[i]);
        ch[i] = false;
      }
    }
  }

  dfs("");
  return [...answer];
}

const isPrime = (n) => {
  if (n === 0 || n === 1) return false;
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
};

console.log(solution("17"));
