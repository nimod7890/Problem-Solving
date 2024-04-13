
def available(row,col):
  for r in range(row):
    if visited[r]==col or abs(r-row)==abs(visited[r]-col):
      return False
  
  return True

def dfs(row):
  global cnt
  if row==n:
    cnt+=1
    return 
  
  for col in range(n):
    if available(row,col):
      visited[row]=col
      dfs(row+1)

n=int(input())
cnt=0
visited=[-1]*n

dfs(0)
print(cnt)


# def dfs(row, cols, ldiag, rdiag):
#     global cnt
#     if row == n:
#       cnt += 1
#       return

#     for col in range(n):
#       if not (cols & (1 << col) or ldiag & (1 << (row - col + n - 1)) or rdiag & (1 << (row + col))):
#         dfs(row + 1, cols | (1 << col), ldiag | (1 << (row - col + n - 1)), rdiag | (1 << (row + col)))

# n = int(input())
# cnt = 0
# dfs(0, 0, 0, 0)
# print(cnt)
