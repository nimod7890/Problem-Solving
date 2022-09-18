from collections import deque
def bfs(i,j):
    global visit
    while will:
        i,j=will.popleft()
        if visit[i][j]==0 and nlist[i][j]==1:
            visit[i][j]=1
            for x,y in [[i-1,j-1],[i-1,j],[i-1,j+1],[i,j-1],[i,j+1],[i+1,j-1],[i+1,j],[i+1,j+1]]:
                if 0<=y<w and 0<=x<h:
                    will.append([x,y])
while True:
    w,h=map(int,input().split())
    if w==h==0: break
    nlist=[list(map(int,input().split())) for i in range(h)]
    visit=[[0 for j in range(w)] for i in range(h)]
    cnt=0
    for i in range(h):
        for j in range(w):
            if visit[i][j]==0 and nlist[i][j]==1:
                will=deque([[i,j]])
                bfs(i,j)
                cnt+=1
    print(cnt)