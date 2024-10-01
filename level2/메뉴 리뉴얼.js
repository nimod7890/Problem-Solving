// python의 맛을 잊지 못해 불행한 나

/**
 * @param {string[]} orders
 * @param {number[]} courses
 */
function solution(orders, courses) {
  orders.sort();

  const bestCourse = [];

  courses.forEach((course) => {
    const hashMap = new Map();

    let maxOrderCount = 0;
    orders.forEach((order) => {
      combination(order.split(""), course).forEach((list) => {
        const menu = list.sort().join("");
        const count = 1 + (hashMap.has(menu) ? hashMap.get(menu) : 0);
        hashMap.set(menu, count);
        maxOrderCount = maxOrderCount < count ? count : maxOrderCount;
      });
    });

    if (maxOrderCount >= 2) {
      hashMap.forEach((count, menu) => count == maxOrderCount && bestCourse.push(menu));
    }
  });

  return bestCourse.sort();
}

function combination(list, number) {
  if (number == 1) return list.map((value) => [value]);

  let combi = [];
  list.forEach((value, index, li) =>
    combi.push(...combination(li.slice(index + 1), number - 1).map((l) => [value, ...l]))
  );

  return combi;
}

console.log(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]));
console.log(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]));
console.log(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]));
