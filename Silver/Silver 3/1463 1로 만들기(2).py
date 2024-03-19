import sys
input=sys.stdin.readline

dp=[0,0,1,1]

N=int(input())

for i in range(4,N+1):
  dp.append(dp[i-1]+1)
  if i%3==0:
    dp[i]=min(dp[i//3]+1,dp[i])
  if i%2==0:
    dp[i]=min(dp[i//2]+1,dp[i])
  
print(dp[N])

# 답 봤는디 반성햇음 난 DP 바보야 ,,..................