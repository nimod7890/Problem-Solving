from collections import deque

m,n,h=map(int,input().split())
graph=[]
will=deque()
for i in range(h):
    tmp=[]
    for j in range(n):
        tmp.append(list(map(int,input().split())))
        for k in range(m):
            if tmp[j][k]==1:
                will.append([i,j,k])
    graph.append(tmp)

while will:
    i,j,k=will.popleft()
    for x,y,z in [[i-1,j,k],[i+1,j,k],[i,j-1,k],[i,j+1,k],[i,j,k-1],[i,j,k+1]]:
        if 0<=x<h and 0<=y<n and 0<=z<m and graph[x][y][z]==0 and graph[x][y][z]!=-1:
            will.append([x,y,z])
            graph[x][y][z]=graph[i][j][k]+1
    
maxi=0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k]==0:
                print(-1)
                exit()
        maxi=max(max(graph[i][j]),maxi)
print(maxi-1)