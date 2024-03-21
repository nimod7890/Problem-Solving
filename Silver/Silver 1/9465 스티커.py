import sys


input=sys.stdin.readline

for _ in range(int(input())):
  n=int(input())
  nlist=[list(map(int,input().split())) for _ in range(2)]
  dp=[[0]*(n+1) for _ in range(2)]
  
  dp[0][1]=nlist[0][0]
  dp[1][1]=nlist[1][0]
  
  if n>1:
    maxi=0
    
    for i in range(1,n+1):
      maxi=max(dp[0][i-2],dp[1][i-2])
      for j in range(2):
        dp[j][i]=max(dp[(j+1)%2][i-1],maxi)+nlist[j][i-1]
      
  print(max(dp[0][-1],dp[1][-1]))