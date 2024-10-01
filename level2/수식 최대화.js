const priorities = [
  // + - *
  ["+", "-", "*"],
  ["+", "*", "-"],
  ["-", "+", "*"],
  ["-", "*", "+"],
  ["*", "+", "-"],
  ["*", "-", "+"],
];

/**
 * @param {string} expression
 */
function solution(expression) {
  const expressions = [];

  for (let i = 0; i < expression.length; i++) {
    const num = expression.slice(i).match(/\d+/);
    expressions.push(num[0]);
    i += num.index + num[0].length;
    if (expression[i]) expressions.push(expression[i]);
  }

  return priorities.reduce((max, priority) => {
    const result = Math.abs(getResult([...expressions], priority));
    return max > result ? max : result;
  }, 0);
}

/**
 * @param {(string|number)[]} expressions
 * @param {Array<'+'|'-'|'*'>} priority
 */
function getResult(expressions, priority) {
  priority.forEach((expression) => {
    while (true) {
      const index = expressions.indexOf(expression);
      if (index < 0) break;
      expressions.splice(
        index - 1,
        3,
        calculate(expressions[index - 1], expressions[index + 1], expressions[index])
      );
    }
  });

  return expressions[0];
}

function calculate(a, b, op) {
  a = +a;
  b = +b;
  switch (op) {
    case "*":
      return a * b;
    case "+":
      return a + b;
    default:
      return a - b;
  }
}

console.log(solution("100-200*300-500+20"));
console.log(solution("50*6-3*2"));
