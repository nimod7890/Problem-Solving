from collections import defaultdict
import heapq
import sys


input=sys.stdin.readline
n,m=map(int,input().split())
nlist=list(map(int,input().split()))
graph=defaultdict(list)
for _ in range(m):
    a,b,t=map(int,input().split())
    graph[a].append((b,t))
    graph[b].append((a,t))
cost=[sys.maxsize]*n
cost[0]=0
queue=[(0,0)]
while queue:
    startWeight,start=heapq.heappop(queue)
    if cost[start]<startWeight:continue
    for end,endWeight in graph[start]:
        weight=startWeight+endWeight
        if nlist[end]==1 and end!=n-1:continue
        if cost[end]<=weight:continue
        cost[end]=weight
        heapq.heappush(queue,(weight,end))
print(-1 if cost[-1]==sys.maxsize else cost[-1])