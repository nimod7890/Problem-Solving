'''
heapq push 할 때 graph랑 순서 다르다 ,,,
'''
from collections import defaultdict
import heapq
from math import inf
import sys

input=sys.stdin.readline
V,E=map(int,input().split())
K=int(input())-1
graph=defaultdict(list)
for _ in range(E):
    u,v,w=map(int,input().split())
    graph[u-1].append((v-1,w))
    
weightArr=[inf]*V
weightArr[K]=0
queue=[]
heapq.heappush(queue,[0,K])
while queue:
    totalWeight,start=heapq.heappop(queue)
    #없으면 약간 느려지고 메모리 더 씀 
    if weightArr[start]<totalWeight:
        continue
    for end,weightOfEnd in graph[start]:
        currentWeight=totalWeight+weightOfEnd
        if currentWeight<weightArr[end]:
            weightArr[end]=currentWeight
            heapq.heappush(queue,[currentWeight,end])
for ans in weightArr:
    print('INF' if ans==inf else ans)
'''
3 2
3
1 3 10
2 1 4

INF
INF
0
---
2 1
2
2 1 1

1
0
---
4 8
1
1 2 3
2 1 5
4 3 4
2 3 10
1 3 10
2 4 1
3 1 1
1 2 2

0
2
7
3
---

2 4
1
1 2 1
1 2 2
1 2 5
1 2 10

0
1
''' 