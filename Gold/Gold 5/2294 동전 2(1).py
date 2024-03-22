from math import inf
import sys


input=sys.stdin.readline

n,k=map(int,input().split())
nlist=[int(input()) for _ in range(n)]
dp=[inf]*(k+1)
dp[0]=0

for value in nlist:
  for i in range(value,k+1):
    if i-value>=0:
      dp[i]=min(dp[i-value]+1,dp[i])
      
print(dp[-1] if dp[-1]!=inf else -1)