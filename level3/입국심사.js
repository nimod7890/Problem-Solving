function solution(n, times) {
  times.sort((a, b) => a - b);
  let [start, end] = [1, times[times.length - 1] * n];

  while (start <= end) {
    const mid = Math.floor((start + end) / 2);

    times.reduce((acc, cur) => acc + Math.floor(mid / cur), 0) < n
      ? (start = mid + 1)
      : (end = mid - 1);
  }

  return start;
}
