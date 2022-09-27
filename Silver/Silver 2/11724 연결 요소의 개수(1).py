from collections import defaultdict, deque
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
graph=defaultdict(list)
for i in range(m):
    u,v=map(int,input().split())
    graph[u]+=[v]
    graph[v]+=[u]

visit=[0]*(n+1)
cnt=0
for i in range(1,n+1):
    if visit[i]==0:
        will=deque([i])
        while will:
            v=will.popleft()
            if visit[v]==0:
                visit[v]=1
                will.extend(graph[v])
        cnt+=1
        
print(cnt)