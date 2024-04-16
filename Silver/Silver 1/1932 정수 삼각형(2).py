import sys


input=sys.stdin.readline
n=int(input())
dp=[0]*n
for i in range(1,n+1):
  cost=[*map(int,input().split())]
  dp=[cost[j]+(dp[0] if j==0 else dp[j-1] if j==i-1 else max(dp[j],dp[j-1])) for j in range(i)]
print(max(dp))