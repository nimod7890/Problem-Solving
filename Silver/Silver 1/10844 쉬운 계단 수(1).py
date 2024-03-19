import sys
divide=1000000000
input=sys.stdin.readline

n=int(input())

dp=[[0,1,1,1,1,1,1,1,1,1]]

for i in range(1,n):
  tmp=[dp[i-1][1]%divide]
  for j in range(1,9):
    tmp.append((dp[i-1][j-1]+dp[i-1][j+1])%divide)
  tmp.append(dp[i-1][8]%divide)
  dp.append(tmp)

print(sum(dp[n-1])%divide)