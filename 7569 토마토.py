import sys
from collections import deque


def bfs():
    while will:
        H, N, M = will.popleft()
        for Hh, Nn, Mm in [[H, N, M-1], [H, N, M+1], [H, N-1, M],
                           [H, N+1, M], [H+1, N, M], [H-1, N, M]]:
            if 0 <= Hh < h and 0 <= Nn < n and 0 <= Mm < m and apples[Hh][Nn][Mm] == 0:
                will.append([Hh, Nn, Mm])
                apples[Hh][Nn][Mm] = apples[H][N][M]+1


input = sys.stdin.readline
m, n, h = map(int, input().split())
will = deque()

apples = []
for H in range(h):
    tmp = []
    for N in range(n):
        tmp.append(list(map(int, input().split())))
        for M in range(m):
            if tmp[N][M] == 1:
                will.append([H, N, M])
    apples.append(tmp)

cnt = 0
for apple in apples:
    for a in apple:
        if 0 not in a:
            cnt += 1
if cnt == n*h:
    print(0)
    exit(0)

bfs()

maximum = 0
for apple in apples:
    for a in apple:
        if 0 in a:
            print(-1)
            exit(0)
        maximum = max(maximum, max(a))
print(maximum-1)
