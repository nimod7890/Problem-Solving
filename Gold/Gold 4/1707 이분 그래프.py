from collections import defaultdict, deque
import sys


def bfs(node):
    global visit, isBi
    will = deque([node])
    visit[node] = 1
    while will:
        node = will.popleft()
        for new in graph[node]:
            if visit[new] == 0:
                will.append(new)
                visit[new] = visit[node]*-1
            elif visit[new] == visit[node]:
                isBi = False
                break


input = sys.stdin.readline
k = int(input())
for i in range(k):
    v, e = map(int, input().split())
    graph = defaultdict(list)
    for j in range(e):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    visit = [0]*v
    isBi = True
    for node in range(v):
        if visit[node] == 0:
            bfs(node)
            if isBi == False:
                break
    print("YES" if isBi == True else "NO")
