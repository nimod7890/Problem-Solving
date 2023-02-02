import sys


input=sys.stdin.readline
f=lambda:map(int,input().split())
n,m=f()
nlist=[list(f()) for i in range(n)]
xy=[[0,1],[1,0],[1,1]]
for i in range(n):
    for j in range(m):
        maxi=0
        for x,y in xy:
            if 0<=i-x<n and 0<=j-y<m:
                maxi=max(maxi,nlist[i-x][j-y])
        nlist[i][j]+=maxi
print(nlist[-1][-1])