from collections import deque
import sys
input=sys.stdin.readline
dydx=[[0,1],[1,0],[0,-1],[-1,0]]


# input
M,N=map(int,input().split())
maze=[list(map(int,input().strip())) for _ in range(N)]

# init
visited=[[-1]*M for _ in range(N)] # -1: 방문 안 함 / 0~: 벽 개수

visited[0][0]=0
next_step=deque([[0,0]])

# process
while next_step:
  start_column,start_row=next_step.popleft()

  for c,r in dydx:
    end_column,end_row=start_column+c, start_row+r
    
    if not (0<=end_column<N and 0<=end_row<M and visited[end_column][end_row]==-1):
      continue
    
    visited[end_column][end_row]=visited[start_column][start_row]+maze[end_column][end_row]
    
    if maze[end_column][end_row]==0:
      next_step.appendleft([end_column,end_row])
    else:
      next_step.append([end_column,end_row])
  
# output
print(visited[N-1][M-1])
