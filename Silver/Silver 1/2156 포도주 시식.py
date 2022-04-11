import sys

input=sys.stdin.readline
N=int(input())
nlist=[int(input()) for i in range(N)]
graph=[0]*N
graph[0]=nlist[0] 
if N==1:
    print(graph[0])
    exit()
graph[1]=graph[0]+nlist[1]  
if N==2:
    print(graph[1])
    exit()
graph[2]=max(graph[0]+nlist[2],nlist[1]+nlist[2],graph[1]) 
if N==3:
    print(graph[2])
    exit()
for n in range(3,N):
    graph[n]=max(graph[n-2]+nlist[n],graph[n-1],graph[n-3]+nlist[n-1]+nlist[n])
print(graph[N-1])
