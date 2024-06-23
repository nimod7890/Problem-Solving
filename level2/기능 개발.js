// 구조는 거의 동일한데 답안 보고 좀 더 깔끔하게 고쳐봄

var progresses = [93, 30, 55];
var speeds = [1, 30, 5];

var max = 0;
var ans = [0];
var j = 0;

for (let i = 0; i < progresses.length; i++) {
  var tmp = Math.ceil((100 - progresses[i]) / speeds[i]);
  if (max == 0) {
    max = tmp;
  }

  if (max >= tmp) {
    ans[j]++;
  } else {
    ans[++j] = 1;
    max = tmp;
  }
}

console.log(ans);
