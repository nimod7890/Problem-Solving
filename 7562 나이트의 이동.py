from collections import deque
import sys

input = sys.stdin.readline
for _ in range(int(input())):
    l = int(input())
    j, i = map(int, input().split())
    y, x = map(int, input().split())
    will = deque()
    will.append([i, j])
    visit = [[0 for i in range(l)] for i in range(l)]
    while visit:
        i, j = will.popleft()
        if i == x and j == y:
            break
        go = [[i-1, j-2], [i-2, j-1], [i-2, j+1], [i-1, j+2],
              [i+1, j-2], [i+2, j-1], [i+2, j+1], [i+1, j+2]]
        for X, Y in go:
            if 0 <= X < l and 0 <= Y < l and visit[X][Y] == 0:
                will.append([X, Y])
                visit[X][Y] = visit[i][j]+1
    print(visit[x][y])
