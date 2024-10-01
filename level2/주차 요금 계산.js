/**
 * @param {string[]} fees
 * @param {string[]} records
 */
function solution(fees, records) {
  const inMap = new Map();
  const minutesMap = new Map();

  function caculateTime(car, timeArr) {
    const inTime = inMap.get(car);

    if (timeArr[1] < inTime[1]) {
      timeArr[0]--;
      timeArr[1] += 60;
    }
    const currentTime = (timeArr[0] - inTime[0]) * 60 + timeArr[1] - inTime[1];
    const originTime = minutesMap.has(car) ? minutesMap.get(car) : 0;

    minutesMap.set(car, originTime + currentTime);
    inMap.delete(car);
  }

  records.forEach((record) => {
    const [time, car, status] = record.split(" ");
    const timeArr = time.split(":").map(Number);

    if (status == "IN") inMap.set(car, timeArr);
    else caculateTime(car, timeArr);
  });

  inMap.forEach((_, car) => caculateTime(car, [23, 59]));

  return [...minutesMap].sort().map(([, minutes]) => getFees(fees, minutes));
}

function getFees(fees, minutes) {
  const feeMins = Math.ceil((minutes - fees[0]) / fees[2]);
  return (feeMins > 0 ? feeMins * fees[3] : 0) + fees[1];
}

console.log(
  solution(
    [180, 5000, 10, 600],
    [
      "05:34 5961 IN",
      "06:00 0000 IN",
      "06:34 0000 OUT",
      "07:59 5961 OUT",
      "07:59 0148 IN",
      "18:59 0000 IN",
      "19:09 0148 OUT",
      "22:59 5961 IN",
      "23:00 5961 OUT",
    ]
  )
);
console.log(
  solution(
    [120, 0, 60, 591],
    ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]
  )
);
console.log(solution([1, 461, 1, 10], ["00:00 1234 IN"]));
