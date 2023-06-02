from collections import defaultdict
import heapq
import sys

input=sys.stdin.readline
for _ in range(int(input())):
    n,d,c=map(int,input().split())
    graph=defaultdict(list)
    for _ in range(d):
        a,b,s=map(int,input().split())
        graph[b].append((a,s))
    cost=[sys.maxsize]*(n+1)
    cost[c]=0
    queue=[(0,c)]
    while queue:
        startWeight,start=heapq.heappop(queue)
        if cost[start]<startWeight:continue
        for end,endWeight in graph[start]:
            weight=startWeight+endWeight
            if cost[end]<=weight:continue
            cost[end]=weight
            heapq.heappush(queue,(weight,end))
    ans=list(filter(lambda x:x<sys.maxsize,cost[1:]))
    print(len(ans),max(ans))
