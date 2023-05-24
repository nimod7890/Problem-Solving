import sys

input=sys.stdin.readline

n,m=map(int,input().split())
board=[list(input().strip()) for i in range(n)]
# print(board,sep='\n')
visit=[[0]*m for i in range(n)]
isCycle=False
for y in range(n):
    for x in range(m):
        visit[y][x]=1
        dfs(board[y][x],x,y,1,x,y)
        if isCycle: 
            print("Yes")
            break
    else:
        continue
else:
    print("No")
