import sys
input=sys.stdin.readline

n=int(input())

dp=[1,3]
if n>1:
  for i in range(2,n):
    dp.append((2*dp[i-2]+dp[i-1])%10007)
  
print(dp[n-1])