from collections import deque
import sys


def bfs(i, j):
    if apart[i][j] == '0':
        return 0
    apart[i][j] = '0'
    will = deque()
    ans = 1
    will.append([i, j])
    while will:
        i, j = will.popleft()
        for x, y in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:
            if 0 <= x < n and 0 <= y < n and apart[x][y] == '1':
                apart[x][y] = '0'
                ans += 1
                will.append([x, y])
    return ans


input = sys.stdin.readline
n = int(input())
apart = [list(input().strip()) for i in range(n)]

answer = []
for i in range(n):
    for j in range(n):
        ans = bfs(i, j)
        if ans != 0:
            answer.append(ans)
l = len(answer)
print(l)
if l != 0:
    for x in sorted(answer):
        print(x)