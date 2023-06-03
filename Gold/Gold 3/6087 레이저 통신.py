import heapq
import sys

input=sys.stdin.readline
w,h=map(int,input().split())
graph=[]
START=[]
END=[]
for i in range(h):
    tmp=[]
    for j,x in enumerate(list(input().rstrip())):
        tmp.append(x)
        if x=='C':
            if len(START)==0:
                START=[i,j]
            else:
                END=[i,j]
    graph.append(tmp)
visit=[[[] for _ in range(w)] for _ in range(h)]
cost=[[sys.maxsize]*w for _ in range(h)]
cost[START[0]][START[1]]=-1
visit[START[0]][START[1]]=[[0,1],[1,0],[0,-1],[-1,0]]
queue=[[0,START[0],START[1],[[0,1],[1,0],[0,-1],[-1,0]]]]
while queue:
    sw,i,j,pathList=heapq.heappop(queue)
    for x,y in pathList:
        X,Y=i+x,j+y
        if 0<=X<h and 0<=Y<w and graph[X][Y]!='*':
            if cost[X][Y]<sw or [x,y] in visit[X][Y]: continue
            cost[X][Y]=sw
            visit[X][Y].append([x,y])
            heapq.heappush(queue,(sw+1,X,Y,[[y,x],[-y,-x]])) #90도 
            heapq.heappush(queue,(sw,X,Y,[[x,y]])) #방향 유지
print(cost[END[0]][END[1]])
    

