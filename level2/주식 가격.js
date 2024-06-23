var prices = [1, 2, 3, 2, 3];

console.log(
  prices.map((current, index) => {
    let end;
    for (end = index + 1; end < prices.length; end++) {
      if (current > prices[end]) {
        end++;
        break;
      }
    }
    return end - index - 1;
  })
);
