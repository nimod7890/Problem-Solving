from collections import defaultdict, deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = defaultdict(list)
for i in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

visit = [0 for i in range(n)]
visit[0] = 1
will = deque([0])
while will:
    x = will.popleft()
    for new in graph[x]:
        if visit[new] == 0:
            will.append(new)
            visit[new] = visit[x]+1
maxi = max(visit)
idx = visit.index(maxi)
print(idx+1, visit[idx]-1, visit.count(maxi))
