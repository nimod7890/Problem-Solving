function solution(clothes) {
  var hash = new Map();

  clothes.forEach(([_, key]) => {
    hash.set(key, (hash.get(key) ?? 0) + 1);
  });

  var answer = 1;
  for (let [_, value] of hash) {
    answer *= value + 1;
  }

  return answer - 1;
}
