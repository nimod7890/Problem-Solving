'''
queue와 path에 push할 때 weight 부호 구분하기 
'''
import heapq  
import sys

input=sys.stdin.readline
n,m,k=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    
path=[[] for _ in range(n+1)]
path[1].append(0)
queue=[(0,1)]
while queue:
    startWeight,start=heapq.heappop(queue)
    for end,endWeight in graph[start]:
        w=startWeight+endWeight
        if len(path[end])<k:
            heapq.heappush(path[end],-w)
            heapq.heappush(queue,(w,end))
        elif -path[end][0]>w: 
            heapq.heappop(path[end])
            heapq.heappush(path[end],-w)
            heapq.heappush(queue,(w,end))

for end in range(1,n+1):
    print(-path[end][0] if len(path[end])==k else -1)