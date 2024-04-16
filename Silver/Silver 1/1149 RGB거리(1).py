import sys
input=sys.stdin.readline

dp=[0]*3
for i in range(int(input())):
  r,g,b=map(int,input().split())
  dp=[min(dp[1],dp[2])+r,min(dp[0],dp[2])+g,min(dp[0],dp[1])+b]
print(min(dp))