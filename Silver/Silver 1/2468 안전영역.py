from collections import deque
import sys


def bfs(x, y, bound):
    global visit
    will = deque()
    will.append([x, y])
    visit[x][y] = 1
    while will:
        x, y = will.popleft()
        for i, j in [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]:
            if 0 <= i < n and 0 <= j < n and visit[i][j] == 0 and graph[i][j] >= bound:
                visit[i][j] = 1
                will.append([i, j])


def visiting(bound):
    global visit
    visit = [[0 for i in range(n)]for i in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0 and graph[i][j] >= bound:
                bfs(i, j, bound)
                cnt += 1
    return cnt


input = sys.stdin.readline
n = int(input())
graph = list()
maxi = -1
for i in range(n):
    tmp = list(map(int, input().split()))
    temp = max(tmp)
    maxi = temp if maxi == -1 or temp > maxi else maxi
    graph.append(tmp)

ans = -1
for bound in range(1, maxi+1):
    temp = visiting(bound)
    ans = temp if ans == -1 or temp > ans else ans

print(ans)
