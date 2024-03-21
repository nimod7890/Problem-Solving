import sys


input=sys.stdin.readline

n=int(input())
nlist=[int(input()) for _ in range(n)]

dp=[[0,0] for _ in range(n)]
dp[0]=[nlist[0],0]
for i in range(1,n):
  dp[i]=[max(dp[i-2])+nlist[i],dp[i-1][0]+nlist[i]]
print(max(dp[-1]))