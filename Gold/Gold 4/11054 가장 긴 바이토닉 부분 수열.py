import sys

input=sys.stdin.readline
n=int(input())
nlist=[*map(int,input().split())]
dp=[[0,0] for i in range(n)]

for i in range(n):
  for j in range(i):
    if nlist[j]<nlist[i] and dp[i][0]<dp[j][0]+1:
      dp[i][0]=dp[j][0]+1
  k=n-i-1
  for j in range(n-1,k-1,-1):
    if nlist[j]<nlist[k] and dp[k][1]<dp[j][1]+1:
      dp[k][1]=dp[j][1]+1
print(max(map(lambda x:sum(x),dp))+1)