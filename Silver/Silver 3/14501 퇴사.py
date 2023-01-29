import sys


input=sys.stdin.readline
n=int(input())
nlist=[list(map(int,input().split())) for i in range(n)]
dp=[0]*(n+1)
for i in reversed(range(n)):
    if i+nlist[i][0]>n:
        dp[i]=dp[i+1]
    else:
        dp[i]=max(dp[i+1],dp[i+nlist[i][0]]+nlist[i][1])
print(dp[0])