var citations = [3, 0, 6, 1, 5];
citations
  .sort((a, b) => b - a)
  .forEach((citation, index) => {
    if (citation >= index + 1) {
      answer = index + 1;
      return;
    }
  });

return answer;
