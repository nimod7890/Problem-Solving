import sys

input=sys.stdin.readline
numList=[[*map(int,input().split())] for _ in range(5)]
ans=set()
def func(X,Y,cnt,num):
    if cnt==6:
        ans.add(num)
        return 
    for y,x in [[-1,0],[0,1],[1,0],[0,-1]]:
        if 0<=X+x<5 and 0<=Y+y<5:
            func(X+x,Y+y,cnt+1,10*num+numList[Y+y][X+x])
            
for y,nList in enumerate(numList):
    for x,n in enumerate(nList):
        func(x,y,1,n)
print(len(ans))