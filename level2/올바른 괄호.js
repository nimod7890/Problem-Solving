function solution(s) {
  var sum = 0;
  for (let word of s) {
    word == "(" ? sum++ : sum--;
    if (sum < 0) {
      return false;
    }
  }
  return sum == 0;
}
