from collections import defaultdict, deque
from copy import deepcopy
import sys

input=sys.stdin.readline
n=int(input())
graph=defaultdict(deque)
for i in range(n):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
relation=deepcopy(graph)
# queue=deque([1])
# visit[1]=1
# while queue:
#     parent=queue.pop()
#     for child in graph[parent]:
#         if visit[child]==0:
#             queue.append(child)
#         visit[child]+=1
#     print(visit)

queue=deque()
parent=[0]*(n+1)
cnt=[0]*(n+1)
for c_node,relations in graph.items():
    for p_node in graph[c_node]:
        if len(relation[p_node])==1:
            parent[c_node]=p_node
            queue.append(p_node)
            relation[c_node].remove(p_node)
            relation[p_node].remove(c_node)
while queue:
    c_node=queue.pop()
    for p_node in graph[c_node]:
        print(p_node,c_node,relation,relation[p_node])
        if len(relation[p_node])==1:
            parent[c_node]=p_node
            queue.append(p_node)
            relation[c_node].remove(p_node)
            relation[p_node].remove(c_node)
            print(relation)
print("parent: ",parent)
# for node,p_node in enumerate(parent[1:]):
#     if p_node!=0:
        
    