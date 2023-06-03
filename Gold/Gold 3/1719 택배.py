import sys

input=sys.stdin.readline
n,m=map(int,input().split())
weight=[[sys.maxsize]*(n) for _ in range(n)]
path=[[j for j in range(1,n+1)] for _ in range(n)]
for _ in range(m):
    a,b,t=map(int,input().split())
    weight[a-1][b-1]=t
    weight[b-1][a-1]=t
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j:
                weight[i][j]=0
                path[i][j]='-'
            elif weight[i][k]+weight[k][j]<weight[i][j]:
                weight[i][j]=weight[i][k]+weight[k][j]
                path[i][j]=path[i][k]
for p in path:
    print(*p)