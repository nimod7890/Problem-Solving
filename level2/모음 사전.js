var word = "AAAAE";
const gathers = "AEIOU";
const maxNums = [781, 156, 31, 6, 1];

console.log(word.split("").reduce((sum, w, i) => sum + gathers.indexOf(w) * maxNums[i] + 1, 0));
