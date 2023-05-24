from collections import defaultdict, deque
from math import inf
import sys

def bfs(start):
    bacon=[0]*n
    visit=[0]*n
    will=deque([start])
    visit[start]=1
    while will:
        # 이거 왜 pop() 안되는데?? ! ? 
        s=will.popleft()
        for e in graph[s]:
            if visit[e]==1:continue
            visit[e]=1
            bacon[e]=bacon[s]+1
            will.append(e)
    return sum(bacon)

input=sys.stdin.readline
n,m=map(int,input().split())
graph=defaultdict(list)
for _ in range(m):
    a,b=map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)


minimum=inf
ans=-1
for start in range(n):
    minOfStart=bfs(start)
    if minimum>minOfStart:
        ans=start 
        minimum=minOfStart
print(ans+1)