from collections import defaultdict
import heapq
from math import inf
import sys


input=sys.stdin.readline
n,e=map(int,input().split())
graph=defaultdict(list)
for _ in range(e):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1,v2=map(int,input().split())


def dijkstra(START):
    path=[inf]*(n+1)
    path[START]=0
    queue=[(0,START)]
    while queue:
        startWeight,start=heapq.heappop(queue)
        if path[start]<startWeight: continue
        for end,endWeight in graph[start]:
            weight=startWeight+endWeight
            if path[end]<weight: continue
            path[end]=weight
            heapq.heappush(queue,(weight,end))
    return path

must=dijkstra(v1)[v2] # v1~v2
# 1~v1, 1~v2
toPath=dijkstra(1)
toV1,toV2=toPath[v1],toPath[v2]
# v1~n, v2~n
fromPath=dijkstra(n)
fromV1,fromV2=fromPath[v1],fromPath[v2]
ans=min(toV1+fromV2,toV2+fromV1)+must
if ans==inf: 
    print(-1)
else:
    print(ans)