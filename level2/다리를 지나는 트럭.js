var bridge_length = 2;
var weight = 10;
var truck_weights = [7, 4, 5, 6];

let weightArr = Array.from({ length: bridge_length }).fill(0);
var start = -1;

for (let i = 0; i < truck_weights.length; i++) {
  start = weightArr.findIndex(
    (value, index) => index > start && weight >= value + truck_weights[i]
  );
  start = start >= 0 ? start : weightArr.length;

  for (let j = start; j < start + bridge_length; j++) {
    if (j == weightArr.length) {
      weightArr.push(truck_weights[i]);
    } else {
      weightArr[j] += truck_weights[i];
    }
  }
}

console.log(weightArr.length + 1);
