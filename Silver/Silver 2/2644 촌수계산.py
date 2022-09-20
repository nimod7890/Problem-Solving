from collections import defaultdict, deque

n=int(input())
p1,p2=map(int,input().split())
graph=defaultdict(list)
for i in range(int(input())):
    a,b=map(int,input().split())
    graph[a]+=[b]
    graph[b]+=[a]
visit=[0]*(n+1)
will=deque([p1])
cnt=0
l=[0]*(n+1)
while will:
    node=will.popleft()
    if node==p2:
        print(l[node])
        break
    if visit[node]==0:
        visit[node]=1
        for v in graph[node]:
            l[v]=l[node]+1
        will.extend(graph[node])
else:
    print(-1)