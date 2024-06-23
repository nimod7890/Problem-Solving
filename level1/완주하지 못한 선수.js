function solution(participant, completion) {
  var hash = new Map();

  for (let i = 0; i < participant.length; i++) {
    hash.set(participant[i], (hash.get(participant[i]) ?? 0) + 1);
    hash.set(completion[i], (hash.get(completion[i]) ?? 0) - 1);
  }

  for (let [key, value] of hash) {
    if (value > 0) {
      console.log(key);
      return key;
    }
  }
}
