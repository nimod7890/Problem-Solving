// bfs 로 했는데 시간초과 남 ;; ;

var numbers = [4, 1, 2, 1];
var target = 4;

var answer = 0;

function dfs(number, index) {
  if (index == numbers.length) {
    if (number == target) {
      answer++;
    }
    return;
  }

  dfs(number + numbers[index], index + 1);
  dfs(number - numbers[index], index + 1);
}

dfs(0, 0);

console.log(answer);
