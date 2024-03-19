import sys
input=sys.stdin.readline

n=int(input())
dp=list(map(int,input().split()))
for i in range(n):
  for j in range(i):
    dp[i]=min(dp[i-j-1]+dp[j],dp[i])
    
print(dp[n-1])