from collections import defaultdict
import heapq
from math import inf
import sys
input=sys.stdin.readline

n=int(input())
m=int(input())
graph=defaultdict(list)
for i in range(m):
    s,e,w=map(int,input().split())
    graph[s].append((e,w))
START,END=map(int,input().split())

if START==END:
    print(*[1,1,1],sep='\n')
    exit()

queue=[]
heapq.heappush(queue,[0,START])
weight=[inf]*(n+1)
weight[START]=0
path=[0]*(n+1) 
while queue:
    w,start=heapq.heappop(queue)
    if weight[start]<w:
        continue
    for end,cost in graph[start]:
        newCost=w+cost
        if weight[end]>newCost:
            weight[end]=newCost
            path[end]=start
            heapq.heappush(queue,[newCost,end])
    
curr=END
ans=[]
while curr:
    ans.append(curr)
    curr=path[curr]
print(weight[END])
print(len(ans))
print(*ans[::-1],sep=' ')
