from collections import defaultdict

n = int(input())
graph = defaultdict(int)
graph[1]=2
graph[2]=2
if n>2:
    for i in range(3, n+1):
        graph[i] = (graph[i-1]+graph[i-2]) % 10007
print(graph[n])
