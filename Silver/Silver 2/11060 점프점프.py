from collections import deque
import sys

input=sys.stdin.readline
n=int(input())
nlist=list(map(int,input().split()))
visit=[0]*n
will=deque([0])
while will:
    x=will.popleft()
    if x==n-1:
        print(visit[x])
        break
    for i in range(1,nlist[x]+1):
        if 0<=i+x<n and visit[x+i]==0:
            will.append(x+i)
            visit[x+i]=visit[x]+1
else:
    print(-1)