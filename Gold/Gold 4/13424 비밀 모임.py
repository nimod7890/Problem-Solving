import sys

input=sys.stdin.readline
for _ in range(int(input())):
    n,m=map(int,input().split())
    graph=[[sys.maxsize]*(n) for _ in range(n)]
    for _ in range(m):
        a,b,c=map(int,input().split())
        graph[a-1][b-1]=c
        graph[b-1][a-1]=c
    k=int(input())
    klist=list(map(int,input().split()))
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j]=0 if i==j else min(graph[i][j],graph[i][k]+graph[k][j])
    ans=0
    mini=sys.maxsize
    for node,g in enumerate(graph):
        tmp=sum([g[k-1] for k in klist])
        if tmp<mini:
            ans=node
            mini=tmp
    print(ans+1)