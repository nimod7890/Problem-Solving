import sys
input=sys.stdin.readline


n=int(input())
nlist=[*map(int,input().split())]
dp=[0]*n
dp[0]=nlist[0]

for i in range(1,n):
  dp[i]=nlist[i]
  for j in range(i):
    if nlist[i]>nlist[j]:
      dp[i]=max(dp[i],dp[j]+nlist[i])
print(max(dp))