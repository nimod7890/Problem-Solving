function solution(distance, rocks, n) {
  var answer = 0;
  let [st, en] = [1, distance];
  rocks.sort((a, b) => a - b);

  while (st <= en) {
    const mid = Math.floor((st + en) / 2);
    let [prev, cnt] = [0, 0];

    for (let i = 0; i < rocks.length; i++) {
      if (rocks[i] - prev < mid) {
        cnt++;
      } else {
        prev = rocks[i];
      }
    }

    if (distance - prev < mid) {
      cnt++;
    }

    if (cnt > n) {
      en = mid - 1;
    } else {
      answer = Math.max(answer, mid);
      st = mid + 1;
    }
  }

  return answer;
}
