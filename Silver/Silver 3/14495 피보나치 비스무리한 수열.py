from collections import defaultdict


n = int(input())
graph = defaultdict(int)
graph[1] = 1
graph[2] = 1
graph[3] = 1
if n <= 3:
    print(graph[n])
    exit()
for i in range(4, n + 1):
    graph[i] = graph[i - 1] + graph[i - 3]
print(graph[n])
