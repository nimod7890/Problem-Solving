import heapq
import sys


input=sys.stdin.readline
num=1
while True:
    n=int(input())
    if n==0: break
    path=[list(map(int,input().split())) for _ in range(n)]
    cost=[[sys.maxsize]*n for _ in range(n)]
    cost[0][0]=path[0][0]
    queue=[(path[0][0],0,0)]
    while queue:
        w,i,j=heapq.heappop(queue)
        if cost[i][j]<w:continue
        for x,y in [[0,1],[1,0],[-1,0],[0,-1]]:
            X,Y=i+x,j+y
            if 0<=X<n and 0<=Y<n:
                new=w+path[X][Y]
                if cost[X][Y]<=new: continue
                cost[X][Y]=new
                heapq.heappush(queue,(new,X,Y))
    print(f"Problem {num}: {cost[-1][-1]}")
    num+=1