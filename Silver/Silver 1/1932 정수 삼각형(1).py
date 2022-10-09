from collections import deque
import sys


input=sys.stdin.readline
n=int(input())
nlist=deque([list(map(int,input().split())) for i in range(n)])
nlist.appendleft(0)
dp=[0,[nlist[1][0]]]
for i in range(2,n+1):
    tmp=[0]*i
    tmp[0]=dp[i-1][0]+nlist[i][0]
    tmp[i-1]=dp[i-1][i-2]+nlist[i][i-1]
    for j in range(1,i-1):
        tmp[j]=max(dp[i-1][j-1],dp[i-1][j])+nlist[i][j]
    dp.append(tmp)
print(max(dp[n]))