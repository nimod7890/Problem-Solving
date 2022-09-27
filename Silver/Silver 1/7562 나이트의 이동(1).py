from collections import deque
import sys

input=sys.stdin.readline
dx=[-2,-1,-2,-1,1,2,1,2]
dy=[-1,-2,1,2,-2,-1,2,1]

def bfs():
    l=int(input())
    startX,startY=map(int,input().split())
    x,y=map(int,input().split())
    nlist=[[0 for i in range(l)] for i in range(l)]
    will=deque([[startX,startY]])
    while will:
        a,b=will.popleft()
        if a==x and b==y: 
            break
        for X,Y in zip(dx,dy):
            X+=a
            Y+=b    
            if 0<=X<l and 0<=Y<l:
                if nlist[X][Y]==0:
                    nlist[X][Y]=nlist[a][b]+1
                    will.append([X,Y])
    print(nlist[x][y])

for _ in range(int(input())):
    bfs()