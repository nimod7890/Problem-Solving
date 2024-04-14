from collections import deque
import sys
input=sys.stdin.readline
dx=[-1,1,0,0]
dy=[0,0,-1,1]

r,c=map(int,input().split())
board=[list(input().rstrip()) for i in range(r)]
ans=1

def backtracking(depth,y,x):
  global visited,ans
  if depth > ans:
    ans=depth

  for (_y,_x) in zip(dx,dy):
    i,j=_y+y,_x+x
    if (0<=i<r and 0<=j<c) and (board[i][j] not in visited):
      visited.add(board[i][j])
      backtracking(depth+1,i,j)
      visited.discard(board[i][j])

visited=set([board[0][0]])
backtracking(1,0,0)
print(ans)