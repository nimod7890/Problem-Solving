function check(a, b, c, d) {
  return (b[0] - a[0]) / (b[1] - a[1]) == (c[0] - d[0]) / (c[1] - d[1]);
}

function solution(dots) {
  if (check(dots[0], dots[1], dots[2], dots[3])) {
    return 1;
  }
  if (check(dots[0], dots[2], dots[1], dots[3])) {
    return 1;
  }
  if (check(dots[0], dots[3], dots[1], dots[2])) {
    return 1;
  }

  return 0;
}
