import sys

input=sys.stdin.readline
n,k=map(int,input().split())
path=[[0]*n for _ in range(n)]
for i in range(k):
    a,b=map(int,input().split())
    path[a-1][b-1]=-1
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j: continue
            if path[i][k]==-1 and path[k][j]==-1:
                path[i][j]=-1
                
ans=[]
for _ in range(int(input())):
    a,b=map(int,input().split())
    ans.append(-1 if path[a-1][b-1]==-1 else 1 if path[b-1][a-1]==-1 else 0)
print(*ans,sep='\n')