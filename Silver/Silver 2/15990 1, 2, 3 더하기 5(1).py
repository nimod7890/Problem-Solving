import sys


input=sys.stdin.readline

dp=[[1,0,0],[0,1,0],[1,1,1]]

for t in range(int(input())):
  n=int(input())
  end_point=len(dp)
  if end_point<n:
    for i in range(end_point,n):
      dp.append([(dp[i-1][1]+dp[i-1][2])%1000000009,(dp[i-2][0]+dp[i-2][2])%1000000009,(dp[i-3][0]+dp[i-3][1])%1000000009])
      
  print(sum(dp[n-1])%1000000009)