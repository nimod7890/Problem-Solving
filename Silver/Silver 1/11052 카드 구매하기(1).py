import sys


input=sys.stdin.readline

n=int(input())
dp=[0]*n
for i,v in enumerate(list(map(int,input().split()))):
  dp[i]=v

for i in range(n):
  for j in range(i):
    dp[i]=max(dp[i],dp[i-j-1]+dp[j])

print(dp[n-1])