import heapq
import sys

input=sys.stdin.readline
n=int(input())
path=[list(map(int,list(input().rstrip()))) for _ in range(n)]
cost=[[sys.maxsize]*n for _ in range(n)]
cost[0][0]=0
queue=[(0,0,0)]
while queue: 
    w,i,j=heapq.heappop(queue)
    if cost[i][j]<w: continue
    for x,y in [[1,0],[-1,0],[0,1],[0,-1]]:
        X,Y=i+x,j+y
        if 0<=X<n and 0<=Y<n:
            weight=w+(path[X][Y]^1)
            if cost[X][Y]<=weight:continue
            cost[X][Y]=weight
            heapq.heappush(queue,(cost[X][Y],X,Y))
print(cost[-1][-1])