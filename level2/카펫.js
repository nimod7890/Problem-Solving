var brown = 10;
var yellow = 2;
var sum = brown + yellow;
var [a, b] = [1, sum / 1];
while (true) {
  console.log(a, b);
  if (2 * a + 2 * (b - 2) == brown) {
    break;
  }
  a++;
  while (sum % a != 0) {
    a++;
  }
  b = sum / a;
}
console.log([b, a]);
