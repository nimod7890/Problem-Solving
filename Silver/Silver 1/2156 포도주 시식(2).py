import sys
input=sys.stdin.readline

dp=[0,0,0]
for i in range(int(input())):
  v=int(input())
  dp=[max(dp),dp[2]+v,dp[0]+v]
print(max(dp))