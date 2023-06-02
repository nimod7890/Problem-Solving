import sys

input=sys.stdin.readline
n,m,r=map(int,input().split())
tlist=list(map(int,input().split()))
weight=[[sys.maxsize]*(n+1) for _ in range(n+1)]
for _ in range(r):
    a,b,l=map(int,input().split())
    weight[a][b]=l
    weight[b][a]=l

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j: 
                weight[i][j]=0
            else:
                weight[i][j]=min(weight[i][k]+weight[k][j],weight[i][j])
print(max([sum([t if w<=m else 0 for w,t in zip(wlist[1:],tlist)]) for wlist in weight]))