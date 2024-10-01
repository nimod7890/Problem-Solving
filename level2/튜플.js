// forEach부분 별로긴 한데 로직 자체는 맞음

/**
 * @param {string} s
 */
function solution(s) {
  let prevNumber = 0;
  let temp = [];
  const tuple = [];

  /* 조금만 고민하면 가능하긴 할 듯
  const tupleFrom = (str) =>
    str.slice(2, -2).split('},{')
      .map((it) => toNumbers(it))
  */
  [...s].forEach((value) => {
    if (value == "}") {
      if (prevNumber > 0) {
        temp.push(prevNumber);
        prevNumber = 0;
      }
      temp.length && tuple.push(temp);
      temp = [];
    } else if (value == "{") {
      temp = [];
    } else if (value == ",") {
      prevNumber > 0 && temp.push(prevNumber);
      prevNumber = 0;
    } else {
      prevNumber = 10 * prevNumber + Number(value);
    }
  });

  return tuple
    .sort((a, b) => a.length - b.length)
    .reduce((answer, arr) => [...answer, ...arr.filter((value) => !answer.includes(value))], []);
}

console.log(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"));
console.log(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"));
console.log(solution("{{20,111},{111}}"));
console.log(solution("{{123}}"));
console.log(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"));
