from collections import defaultdict
import heapq
import sys

def dijkstra(START):
    cost=[sys.maxsize]*(v+1)
    cost[START]=0
    queue=[(0,START)]
    while queue:
        startWeight,start=heapq.heappop(queue)
        if cost[start]<startWeight:continue
        for end,endWeight in graph[start]:
            weight=startWeight+endWeight
            if cost[end]<=weight:continue
            cost[end]=weight
            heapq.heappush(queue,(weight,end))
    return cost

input=sys.stdin.readline
v,e,p=map(int,input().split())
graph=defaultdict(list)
for _ in range(e):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    
masan=dijkstra(1)
fullPath=masan[v]
gunwoo=dijkstra(p)
gunWooPath=gunwoo[1]+gunwoo[v]
if gunWooPath==fullPath:
    print('SAVE HIM')
else:
    print('GOOD BYE')