from collections import defaultdict
import heapq
from math import inf
import sys

input=sys.stdin.readline
N,M,K=map(int,input().split())
graph=defaultdict(list)
for i in range(M):
    s,e,w=map(int,input().split())
    graph[s].append((e,w))
    graph[e].append((s,w))
    
weight=[[inf]*(K+1) for _ in range(N+1)]
weight[1][0]=0
queue=[]
heapq.heappush(queue,(0,1,0))
while queue:
    weightOfStart,start,k=heapq.heappop(queue)
    if weight[start][k]<weightOfStart:continue
    for end,weightOfEnd in graph[start]:
        currWeight=weightOfStart+weightOfEnd
        # 포장 x
        if weight[end][k]>currWeight:
            weight[end][k]=currWeight
            heapq.heappush(queue,(currWeight,end,k))
        # 포장 o
        if k<K and weight[end][k+1]>weightOfStart:
            weight[end][k+1]=weightOfStart
            heapq.heappush(queue,(weightOfStart,end,k+1))
print(min(weight[N]))