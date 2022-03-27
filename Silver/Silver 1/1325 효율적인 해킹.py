from collections import defaultdict, deque
import sys
input = sys.stdin.readline


def bfs(node):
    visit = [False]*n
    visit[node] = True
    will = deque([node])
    cnt = 1
    while will:
        node = will.popleft()
        for new in graph[node]:
            if visit[new] == False:
                will.append(new)
                visit[new] = True
                cnt += 1
    return cnt


n, m = map(int, input().split())
graph = defaultdict(list)
for i in range(m):
    a, b = map(int, input().split())
    graph[b-1].append(a-1)

maxi = -1
for node in range(n):
    value = bfs(node)
    if value > maxi:
        maxi = value
        Node = [str(node+1)]
    elif value == maxi:
        Node.append(str(node+1))
print(" ".join(Node))
