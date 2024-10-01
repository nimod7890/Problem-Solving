/**
 * @param {string[]} records
 */
function solution(records) {
  const parsed = records.map((record) => {
    const match = record.match(/\d+/);
    const matchIndex = match.index;
    return [record.slice(0, matchIndex), match[0], record.slice(matchIndex + match[0].length)];
  });

  return parsed
    .sort((a, b) =>
      a[0].toLowerCase() == b[0].toLowerCase()
        ? Number(a[1]) - Number(b[1])
        : a[0].toLowerCase() > b[0].toLowerCase()
        ? 1
        : -1
    )
    .map((arr) => arr.join(""));
}

console.log(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]));
console.log(
  solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])
);
