import sys
input=sys.stdin.readline

n=int(input())
dp=[[0,0] for _ in range(n)]
dp[0]=[2,1]
for i in range(1,n):
  dp[i]=[((int(dp[i-1][0]/2)+dp[i-1][1])%9901)*2 ,sum(dp[i-1])%9901]
print(sum(dp[-1])%9901)