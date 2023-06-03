from collections import defaultdict
import heapq
import sys

input=sys.stdin.readline
n,m=map(int,input().split())
graph=defaultdict(list)
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
cost=[sys.maxsize]*(n+1)
path=[sys.maxsize]*(n+1)
cost[1]=0
queue=[(0,1)]
while queue:
    startWeight,start=heapq.heappop(queue)
    if cost[start]<startWeight:continue
    for end,endWeight in graph[start]:
        weight=startWeight+endWeight
        if cost[end]<=weight:continue
        cost[end]=weight
        heapq.heappush(queue,(weight,end))
        path[end]=start
print(n-1)
for start,end in enumerate(path[2:]):
    print(start+2,end)
