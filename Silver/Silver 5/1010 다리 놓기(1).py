import sys
input=sys.stdin.readline

dp=[1,1]
def factor(x:int)->int:
  if x>=len(dp):
    for i in range(len(dp),x+1):
      dp.append(dp[i-1]*i)
  return dp[x]

for _ in range(int(input())):
  n,m=map(int,input().split())
  print(factor(m)//(factor(n) * factor(m-n)))