// #자체에 대한 고려를 안하고 있었어서(tokenize없이 Regex 짬) 답이 안나와서 멜로디 길이, 재생시간 이리저리 수정하느라 오래 걸림
// time diff 구할 때 한땀한땀 했는데 Date 써서 하는 방법도 알아두면 좋을 듯

/**
 * @param {string} m
 * @param {string[]} musicinfos
 */
function solution(m, musicinfos) {
  const tokenize = (melody) => melody.replaceAll(/([A-Z])#/g, (_, p1) => p1.toLowerCase());
  const timeDiff = (start, end) =>
    (new Date(`1970-01-01 ${end}:00`) - new Date(`1970-01-01 ${start}:00`)) / 60000;

  m = tokenize(m);
  const regex = new RegExp(m, "g");

  let answer = [];
  musicinfos.forEach((musicinfo) => {
    let [start, end, name, melody] = musicinfo.split(",");
    const time = timeDiff(start, end);
    melody = tokenize(melody);

    if (melody.length < time) {
      const replay = Math.ceil((time - melody.length) / melody.length);
      melody = melody.repeat(replay + 1);
    } else {
      melody = melody.slice(0, time);
    }

    melody.match(regex) && answer.push([time, name]);
  });

  return answer.length == 0 ? "(None)" : answer.sort((a, b) => b[0] - a[0])[0][1];
}

console.log(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]));
console.log(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]));
console.log(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]));
