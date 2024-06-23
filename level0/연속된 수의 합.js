// // ㅏ 코드 맘에 안 들었는데 Math.ceil 쓰면 깔끔해짐

function solution(num, total) {
  var min = Math.ceil(total / num - num / 2);
  return Array.from({ length: num }, (_, i) => min + i);
}
