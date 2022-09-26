from collections import deque


n,m,k=map(int,input().split())
nlist=[[0 for j in range(m)] for i in range(n)]
for i in range(k):
    a,b=map(int,input().split())
    nlist[a-1][b-1]=1

for i in range(n):
    for j in range(m):
        if nlist[i][j]==1:
            will=deque([[i,j]])
            cnt=1
            while will:
                x,y=will.popleft()
                if nlist[x][y]!=0:
                    for a,b in [[x-1,y],[x,y-1],[x,y+1],[x+1,y]]:
                        if 0<=a<n and 0<=b<m and nlist[a][b]==1:
                            nlist[a][b]=cnt
                            cnt+=1
                            will.append([a,b])
maxi=0
for i in range(n):
    maxi=max(maxi,max(nlist[i]))
print(maxi-1)