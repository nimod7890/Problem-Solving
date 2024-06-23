function solution(genres, plays) {
  var hash = new Map();
  var sum = new Map();

  for (let i = 0; i < genres.length; i++) {
    sum.set(genres[i], (sum.get(genres[i]) ?? 0) + plays[i]);

    hash.set(
      genres[i],
      [...(hash.get(genres[i]) ?? []), [plays[i], i]].sort((a, b) => b[0] - a[0]).slice(0, 2)
    );
  }
  return [...sum]
    .sort((a, b) => b[1] - a[1])
    .flatMap(([key]) => hash.get(key).map((index) => index[1]));
}
