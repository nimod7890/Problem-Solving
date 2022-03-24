from collections import defaultdict, deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = defaultdict(list)
visit = [0]*n
will = deque(i for i in range(n))
group = list(i for i in range(n))
for i in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
while will:
    x = will.popleft()
    if visit[x] == 0:
        visit[x] = 1
        for y in graph[x]:
            will.append(y)
            group[y] = group[x]
print(len(set(group)))
