import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    for j in range(m):
        maxi = 0
        if 0 <= i - 1 < n and 0 <= j - 1 < m:
            maxi = max(graph[i - 1][j - 1], maxi)
        if 0 <= i - 1 < n and 0 <= j < m:
            maxi = max(graph[i - 1][j], maxi)
        if 0 <= i < n and 0 <= j - 1 < m:
            maxi = max(graph[i][j - 1], maxi)
        graph[i][j] += maxi
print(graph[n - 1][m - 1])
