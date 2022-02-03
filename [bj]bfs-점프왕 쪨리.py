
##문제 조건이 이상해서 제출 안함

import sys
input=sys.stdin.readline

n=int(input())
d=[[] for i in range(n)]
for i in range(n):
    d[i]=list(map(int, input().split()))
# print(d)
visit=[[0 for i in range(n)] for i in range(n)]

def bfs(x,y):
    global visit
    if x==n-1 and y==n-1: 
        print("HaruHaru")
        exit(1)
    for i in range(d[x][y]+1):
        # print("start x y",x+1,y+1,i)
        x_=x+i
        y_=y+d[x][y]-i
        # print(x_,y_)
        if 0<=x_<n and 0<=y_<n:
            if visit[x_][y_]==1: 
                # print("visit before")
                continue
            # print("new xy",x_+1,y_+1)
            bfs(x_,y_)
            visit[x_][y_]=1
visit[0][0]=1
bfs(0,0)
print("Hing")
        
