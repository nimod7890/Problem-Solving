var sizes = [
  [14, 4],
  [19, 6],
  [6, 16],
  [18, 7],
  [7, 11],
];
var [W, H] = [0, 0];
sizes.forEach(([w, h]) => {
  [w, h] = w > h ? [w, h] : [h, w];
  [W, H] = [Math.max(w, W), Math.max(h, H)];
});
console.log(W * H);
