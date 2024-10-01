/**
 * @param {number} cacheSize
 * @param {Array<string>} cities
 */
function solution(cacheSize, cities) {
  if (cacheSize == 0) return cities.length * 5;

  const cache = Array.from({ length: cacheSize }).fill(0);

  return cities.reduce((time, city) => {
    city = city.toLowerCase();
    const index = cache.findIndex((cachedCity) => cachedCity == city);
    if (index >= 0) {
      cache.splice(index, 1);
      cache.push(city);
      return time + 1;
    } else {
      const empty = cache.findIndex((value) => value == 0);
      if (empty >= 0) {
        cache[empty] = city;
      } else {
        cache.shift();
        cache.push(city);
      }
      return time + 5;
    }
  }, 0);
}

console.log(
  solution(3, [
    "Jeju",
    "Pangyo",
    "Seoul",
    "NewYork",
    "LA",
    "Jeju",
    "Pangyo",
    "Seoul",
    "NewYork",
    "LA",
  ])
);

console.log(
  solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])
);

console.log(
  solution(2, [
    "Jeju",
    "Pangyo",
    "Seoul",
    "NewYork",
    "LA",
    "SanFrancisco",
    "Seoul",
    "Rome",
    "Paris",
    "Jeju",
    "NewYork",
    "Rome",
  ])
);

console.log(
  solution(5, [
    "Jeju",
    "Pangyo",
    "Seoul",
    "NewYork",
    "LA",
    "SanFrancisco",
    "Seoul",
    "Rome",
    "Paris",
    "Jeju",
    "NewYork",
    "Rome",
  ])
);

console.log(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]));

console.log(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]));

console.log(solution(3, ["a", "b", "c", "b", "d", "c"]));

console.log(solution(0, ["Jeju", "Jeju"]));
