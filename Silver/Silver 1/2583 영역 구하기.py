from collections import deque

m,n,k=map(int,input().split())
nlist=[[1 for j in range(n)] for i in range(m)]
for _ in range(k):
    lx,ly,rx,ry=map(int,input().split())
    ly=m-ly
    ry=m-ry
    for i in range(ry,ly):
        for j in range(lx,rx):
            nlist[i][j]=0
cnt=0
result=[]
for i in range(m):
    for j in range(n):
        if nlist[i][j]==1:
            r=1
            will=deque([[j,i]])
            nlist[i][j]=0
            while will:
                x,y=will.popleft()
                for X,Y in [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]:
                    if 0<=X<n and 0<=Y<m and nlist[Y][X]==1:
                        will.append([X,Y])
                        nlist[Y][X]=0
                        r+=1
            cnt+=1
            result.append(r)
print(cnt)
print(" ".join(map(str,sorted(result))))
