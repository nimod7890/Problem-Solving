from collections import deque
from copy import deepcopy
from itertools import combinations
import sys


def bfs(i,j):
    global newgraph,visit
    will=deque()
    will.append([i,j])
    while will:
        i,j=will.popleft()
        for x,y in [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]:
            if 0<=x<n and 0<=y<m and newgraph[x][y]==0 and visit[x][y]==0:
                will.append([x,y])
                visit[i][j]=1
                newgraph[x][y]=2

input=sys.stdin.readline
n,m=map(int,input().split())
graph=[]
wall=[]
for i in range(n):
    tmp=list(map(int,input().split()))
    for j in range(m):
        if tmp[j]==0:
            wall.append([i,j])
    graph.append(tmp)

mini=-1
for a,b,c in combinations(wall,3):
    newgraph=deepcopy(graph)
    visit=[[0 for i in range(m)] for j in range(n)]
    for i,j in [a,b,c]:
        newgraph[i][j]=1
    for i in range(n):
        for j in range(m):
            if newgraph[i][j]==2 and visit[i][j]==0:
                visit[i][j]=1
                bfs(i,j)
    cnt=0
    for v in newgraph:
        cnt+=v.count(0)
    mini=max(cnt,mini)
print(mini)