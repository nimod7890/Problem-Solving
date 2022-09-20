from collections import deque
import sys

input=sys.stdin.readline
for _ in range(int(input())):
    m,n,k=map(int,input().split())
    nlist=[[0 for _ in range(m)] for _ in range(n)]
    for i in range(k):
        a,b=map(int,input().split())
        nlist[b][a]=1
    cnt=0
    for i in range(n):
        for j in range(m):
            if nlist[i][j]==1:
                will=deque([[i,j]])
                while will:
                    y,x=will.popleft()
                    if nlist[y][x]==1:
                        nlist[y][x]+=1
                        for X,Y in [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]:
                            if 0<=X<m and 0<=Y<n:
                                will.append([Y,X])
                cnt+=1
    print(cnt)        