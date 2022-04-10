from collections import defaultdict
import sys
num = 1000000009
graph = defaultdict(list)
graph[1] = [1, 0, 0]
graph[2] = [0, 1, 0]
graph[3] = [1, 1, 1]
input = sys.stdin.readline
for i in range(int(input())):
    n = int(input())
    s = sum(graph[n]) % num
    if s != 0:
        print(s)
        continue
    for i in range(4, n+1):
        if len(graph[i]) == 0:
            graph[i] = [(graph[i-1][1]+graph[i-1][2]) % num, (graph[i-2]
                        [0]+graph[i-2][2]) % num, (graph[i-3][0]+graph[i-3][1]) % num]
    print(sum(graph[n]) % 1000000009)
