from collections import deque

m,n=map(int,input().split())
graph=[]
will=deque()
for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(m):
        if graph[i][j]==1:
            will.append([i,j])
    
while will:
    i,j=will.popleft()
    for a,b in [[i-1,j],[i,j-1],[i,j+1],[i+1,j]]:
        if 0<=a<n and 0<=b<m and graph[a][b]==0 and graph[a][b]!=-1:
            graph[a][b]=graph[i][j]+1
            will.append([a,b])
maxi=0
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            print(-1)
            exit()
    maxi=max(max(graph[i]),maxi)
print(maxi-1)

