from collections import defaultdict, deque

n,m,v=input().split()
graph=defaultdict(list)
for i in range(int(m)):
    a,b=map(int,input().split())
    graph[a]+=[b]
    graph[b]+=[a]
    
#dfs
will=deque()
will.append(int(v))
visit=[]
while will:
    node=will.popleft()
    if node not in visit:
        visit.append(node)
        will.extendleft(sorted(graph[node],reverse=True))
            
print(" ".join(map(str,visit)))

#bfs
will=deque()
will.append(int(v))
visit=[]
while will:
    node=will.popleft()
    if node not in visit:
        visit.append(node)
        will.extend(sorted(graph[node]))
            
print(" ".join(map(str,visit)))

