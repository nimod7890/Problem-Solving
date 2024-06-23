// 프로그래머스 댓글보면 자존감 향상됨

function solution(arr) {
  return arr.filter((a, index) => a != arr[index + 1]);
}
