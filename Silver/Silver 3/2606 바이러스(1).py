from collections import defaultdict, deque

n=int(input())
g=defaultdict(list)
for i in range(int(input())):
    a,b=map(int,input().split())
    g[a]+=[b]
    g[b]+=[a]
will=deque([1])
visit=[0]*(n+1)
while will:
    a=will.popleft()
    if visit[a]==0:
        visit[a]=1
        will.extend(g[a])
print(visit[1:].count(1)-1)
