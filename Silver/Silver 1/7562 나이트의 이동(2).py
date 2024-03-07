from collections import deque
import sys
input=sys.stdin.readline

dx=[-2,-1,1,2,-2,-1,1,2]
dy=[-1,-2,2,1,1,2,-2,-1]

# process
def bfs(x,y,X,Y):
  next_step=deque([[x,y,0]])

  visited=[[False for _ in range(l)] for _ in range(l)]
  visited[y][x]=True
  
  while next_step:
    sm,sn,cnt=next_step.popleft()
    
    if sm==X and sn==Y:
      return cnt
    
    for em,en in zip(dx,dy):
      m,n=sm+em,sn+en
      if 0<=m<l and 0<=n<l and not visited[n][m]:
        next_step.append([m,n,cnt+1])
        visited[n][m]=True
  
  return None # cannot access
        
for _ in range(int(input())):
  # input
  l=int(input())
  sx,sy=map(int,input().split())
  ex,ey=map(int,input().split())
  
  # output
  print(bfs(sx,sy,ex,ey))