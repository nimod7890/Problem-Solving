import heapq
import sys

input=sys.stdin.readline
n,m=map(int,input().split())
miro=[list(map(int,list(input().rstrip()))) for _ in range(m)]
path=[[sys.maxsize]*n for _ in range(m)]
path[0][0]=0
queue=[(0,0,0)]
while queue:
    w,i,j=heapq.heappop(queue)  
    if path[i][j]<w: continue  
    for x,y in [[0,1],[1,0],[-1,0],[0,-1]]:
        X,Y=i+x,j+y
        if 0<=X<m and 0<=Y<n:
            new=miro[X][Y]+path[i][j]
            if path[X][Y]<=new: continue
            path[X][Y]=new
            heapq.heappush(queue,(new,X,Y))
print(path[m-1][n-1])