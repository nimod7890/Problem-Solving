import sys
input=sys.stdin.readline

n=int(input())
dp=[[0,1]]

for i in range(1,n):
  dp.append([sum(dp[i-1]),dp[i-1][0]])
  
print(sum(dp[n-1]))