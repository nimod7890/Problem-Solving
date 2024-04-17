import sys


input=sys.stdin.readline
dp=[0,1,1]
for _ in range(int(input())):
  n=int(input())
  
  if n>=len(dp):
    for i in range(len(dp),n+1):
      dp.append(dp[i-2]+dp[i-3])
      
  print(dp[n])