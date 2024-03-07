from collections import deque
import sys
input=sys.stdin.readline

def bfs(init_node):
  if color[init_node]>0 or len(graph[init_node])==0:
    return True
    
  next_step=deque([init_node])
  color[init_node]=1
    
  # process
  while next_step:
    start=next_step.popleft()  
    next_color=color[start] % 2 + 1
    
    for end in graph[start]:
      # 방문하지 않았을 경우
      if color[end]==0:
        color[end]=next_color
        next_step.append(end)
        
      # 현재 노드와 같은 색일 경우
      elif color[end]!=next_color:
        print('NO')
        return False
      
  return True
        

for _ in range(int(input())): 
  
  # input
  V,E=map(int,input().split()) 
  graph=[[] for _ in range(V)]
  
  for _ in range(E):
    u,v=map(int,input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)
  
  # init
  color=[0]*V
  
  # output
  for start in range(V):

    if not bfs(start):
      break
  else:
    print('YES')