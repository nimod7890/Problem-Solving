import sys
input=sys.stdin.readline

n,k=map(int,input().split())
if k==1:
  print(1)
elif k==2:
  print(n+1)
else:
  dp=[[j+1 for j in range(k)] for i in range(n)]
  for i in range(1,n):
    for j in range(1,k):
      dp[i][j]=(dp[i-1][j]+dp[i][j-1])%1000000000
  print(dp[-1][-1])