function solution(n) {
  if (n == 1) return 1;
  let answer = n % 2;
  for (let i = 1; i < n / 2 + 1; i = i + 2) {
    if (n % i == 0) {
      answer++;
    }
  }
  return answer;
}

console.log(solution(1));
console.log(solution(2));
console.log(solution(3));
console.log(solution(5));
console.log(solution(9));
console.log(solution(15));
