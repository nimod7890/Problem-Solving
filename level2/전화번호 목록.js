// 답 보기 전으로 돌아갈 수 없는 몸이 됨

/**
 *
 * @param {string[]} phone_book
 * @returns
 */
function solution(phone_book) {
  return !phone_book.sort().some((value, index, self) => self[index + 1]?.indexOf(value) == 0);
}
