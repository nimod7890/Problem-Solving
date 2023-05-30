from collections import defaultdict
import heapq
import sys


input=sys.stdin.readline
graph=defaultdict(list)
n,m,x=map(int,input().split())
for _ in range(m):
    s,e,w=map(int,input().split())
    graph[e].append((s,w))
    
def dijkstra(START,END=0):
    path=[sys.maxsize]*(n+1)
    path[START]=0
    queue=[(0,START)]
    while queue:
        sw,s=heapq.heappop(queue)
        if path[s]<sw: continue
        for e,ew in graph[s]:
            w=sw+ew
            if path[e]<=w: continue
            path[e]=w
            heapq.heappush(queue,(w,e))
    if END:
        return path[END]
    return path

fromX=dijkstra(x)
maxi=0
for end in range(1,n+1):
    maxi=max(dijkstra(end,x)+fromX[end],maxi) 
print(maxi)
