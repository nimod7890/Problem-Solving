import sys


sys.setrecursionlimit(10**6)
n = int(input())
nlist = [list(input()) for i in range(n)]
visit = [[0 for i in range(n)] for i in range(n)]
visit_rg = [[0 for i in range(n)] for i in range(n)]
cnt = 0
cnt_rg = 0


def go(x, y, color):
    global visit
    if visit[x][y] == 1:
        return
    if nlist[x][y] != color:
        return
    visit[x][y] = 1
    if 0 <= y < n-1:
        go(x, y+1, color)
    if 0 <= x < n-1:
        go(x+1, y, color)
    if y > 0:
        go(x, y-1, color)
    if x > 0:
        go(x-1, y, color)


def go_rg(x, y, color):
    global visit_rg
    if visit_rg[x][y] == 1:
        return
    if nlist[x][y] != color:
        if nlist[x][y] == 'B' or color == 'B':
            return
    visit_rg[x][y] = 1
    if 0 <= y < n-1:
        go_rg(x, y+1, color)
    if 0 <= x < n-1:
        go_rg(x+1, y, color)
    if y > 0:
        go_rg(x, y-1, color)
    if x > 0:
        go_rg(x-1, y, color)


for y in range(n):
    for x in range(n):
        if visit[x][y] == 0:
            go(x, y, nlist[x][y])
            cnt += 1
        if visit_rg[x][y] == 0:
            go_rg(x, y, nlist[x][y])
            cnt_rg += 1

print(cnt, cnt_rg)
