from collections import deque
import sys


def bfs(i, j):
    global timeCnt, weight
    will = deque()
    will.append([i, j])
    fishCnt = 0
    while will:
        i, j = will.popleft()
        find = deque()
        find.append([i, j])
        visit = [[0 for i in range(n)] for i in range(n)]
        search = []
        while find:
            i, j = find.popleft()
            for x, y in [[i-1, j], [i, j-1], [i, j+1], [i+1, j]]:
                if 0 <= x < n and 0 <= y < n and visit[x][y] == 0 and graph[x][y] <= weight:
                    find.append([x, y])
                    visit[x][y] = visit[i][j]+1
                    if 0 < graph[x][y] < weight:
                        search.append([x, y, visit[x][y]])
        if len(search) == 0:
            continue
        search.sort(key=lambda x: (x[2], x[0], x[1]))
        x, y = search[0][:2]
        will.append([x, y])
        graph[x][y] = 0
        timeCnt += visit[x][y]
        fishCnt += 1
        if fishCnt == weight:
            weight += 1
            fishCnt = 0


input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for i in range(n)]
timeCnt = 0
weight = 2
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            graph[i][j] = 0
            bfs(i, j)
            break
print(timeCnt)
