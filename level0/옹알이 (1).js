// 정규식 쓰기

function solution(babbling) {
  var words = ["aya", "ye", "woo", "ma"];

  return babbling
    .map((b) => {
      for (let avaliable of words) {
        b = b.replace(avaliable, " ");
      }
      return b == " " * b.length ? 1 : 0;
    })
    .reduce((a, b) => a + b);
}
