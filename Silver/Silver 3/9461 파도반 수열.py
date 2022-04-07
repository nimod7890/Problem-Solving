from collections import defaultdict
import sys
input = sys.stdin.readline
graph = defaultdict(int)
graph[1] = graph[2] = graph[3] = 1
for i in range(4, 101):
    if graph[i] == 0:
        graph[i] = graph[i-3]+graph[i-2]
for i in range(int(input())):
    print(graph[int(input())])
