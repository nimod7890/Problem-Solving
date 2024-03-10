from collections import deque
import sys
input=sys.stdin.readline
dy=[-1,-1,-1,0,0,1,1,1]
dx=[-1,0,1,-1,1,-1,0,1]

# process
def bfs(column,row):
  visited[column][row]=1
  next_step=deque([[column,row]])
  
  while next_step:
    start_column,start_row=next_step.pop()
    for y,x in zip(dy,dx):
      end_column,end_row=start_column+y,start_row+x
      if 0<=end_column<h and 0<=end_row<w and visited[end_column][end_row]==0 and island[end_column][end_row]==1:
        visited[end_column][end_row]=1
        next_step.append([end_column,end_row])
    
while True: 
  # input
  w,h=map(int,input().split())
  if w==h==0:
    break
  
  island=[list(map(int,input().split())) for _ in range(h)]
  
  # init
  visited=[[0]*w for _ in range(h)]
  cnt=0
  
  # output
  for i in range(h):
    for j in range(w):
      if island[i][j]==1 and visited[i][j]==0:
        bfs(i,j)
        cnt+=1
  
  print(cnt)