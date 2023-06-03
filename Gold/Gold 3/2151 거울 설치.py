import heapq
import sys


input=sys.stdin.readline
n=int(input())
graph=[[] for _ in range(n)]
START=[]
END=[]
for i in range(n):
    for j,x in enumerate(list(input().rstrip())):
        graph[i].append(x)
        if x=='#':
            if len(START)==0:
                START=[i,j]
            else:
                END=[i,j]
cost=[[100]*n for _ in range(n)]
visit=[[[] for _ in range(n)] for _ in range(n)]
cost[START[0]][START[1]]=0
visit[START[0]][START[1]]=[[0,1],[1,0],[-1,0],[0,-1]]
queue=[[cost[START[0]][START[1]],START[0],START[1],visit[START[0]][START[1]]]]
while queue:
    sw,i,j,pathList=heapq.heappop(queue)
    for x,y in pathList:
        X,Y=i+x,j+y
        if 0<=X<n and 0<=Y<n and graph[X][Y]!='*':
            if [x,y] in visit[X][Y]: continue
            if [X,Y]==END and sw==0: 
                print(0)
                exit()
            else: 
                cost[X][Y]=sw
            visit[X][Y].append([x,y])
            if graph[X][Y]=='!':
                heapq.heappush(queue,(sw+1,X,Y,[[y,x],[-y,-x]]))
            heapq.heappush(queue,(sw,X,Y,[[x,y]]))
print(cost[END[0]][END[1]])
