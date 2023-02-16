import sys

MAX=10001
input=sys.stdin.readline
n,k=map(int,input().split())
dp=[MAX]*(k+1)
dp[0]=0
for i in [int(input()) for i in range(n)]:
    for j in range(i,k+1):
        dp[j]=min(dp[j-i]+1,dp[j])
print(dp[k]) if dp[k]!=MAX else print(-1)
