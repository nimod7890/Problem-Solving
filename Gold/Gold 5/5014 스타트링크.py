from collections import deque
import sys

input = sys.stdin.readline
f, s, g, u, d = map(int, input().split())
s -= 1
g -= 1
visit = [0]*(f)
visit[s] = 1
will = deque([s])
while will:
    s = will.popleft()
    if s == g:
        print(visit[s]-1)
        break
    for x in [s+u, s-d]:
        if 0 <= x < f and visit[x] == 0:
            will.append(x)
            visit[x] = visit[s]+1
else:
    print("use the stairs")
