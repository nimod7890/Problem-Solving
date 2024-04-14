import sys
input=sys.stdin.readline

def available(i,j):
  nlist=[False]*10
  
  block_row=(i//3)*3
  block_col=(j//3)*3
  
  for x in range(9):
    nlist[board[i][x]]=True
    nlist[board[x][j]]=True

  for y in range(block_row, block_row + 3):
    for x in range(block_col, block_col + 3):
      nlist[board[y][x]]=True
        
  return nlist

board=[[*map(int,input().split())] for i in range(9)]
empty = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

def backtracking(depth):
  if depth==len(empty):
    for line in board:
      print(*line)
    exit()
  
  i,j=empty[depth]
  nlist=available(i,j)
  for index in range(1,10):
    if nlist[index]:continue
    board[i][j]=index
    backtracking(depth+1)
    board[i][j]=0

backtracking(0)
