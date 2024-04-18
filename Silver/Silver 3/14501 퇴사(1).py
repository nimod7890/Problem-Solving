import sys
input=sys.stdin.readline

n=int(input())
dp=[0]*(n+1)
for i in range(n):
  t,p=map(int,input().split())
  if i+t<=n:
    dp[i+t]=max(dp[i+t],max(dp[:i+1])+p)

print(max(dp))