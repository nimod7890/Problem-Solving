from collections import defaultdict


n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    graph = defaultdict(int)
    graph[1] = 1
    graph[2] = 2
    for i in range(3, n+1):
        graph[i] = (graph[i-1]+graph[i-2]) % 10007
    print(graph[n])
