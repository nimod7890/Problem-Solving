from collections import defaultdict
import heapq
import sys


def dijkstra(START):
    cost=[sys.maxsize]*(n+1)
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
for _ in range(int(input())):
    n,m,t=map(int,input().split())
    s,g,h=map(int,input().split())
    graph=defaultdict(list)
    for _ in range(m):
        a,b,d=map(int,input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))
        if (a==g and b==h) or (a==h and b==g):
            g2h=d
    sCost=dijkstra(s)
    gCost=dijkstra(g)
    hCost=dijkstra(h)
    g2h=gCost[h]
    ansList=[]
    for _ in range(t):
        x=int(input())
        if min(sCost[g]+hCost[x],sCost[h]+gCost[x])+g2h==sCost[x]:
            ansList.append(x)
    print(*sorted(ansList),sep=' ')
