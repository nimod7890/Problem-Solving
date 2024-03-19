import sys
input=sys.stdin.readline

n=int(input())
nlist=list(map(int,input().split()))
dp=[1]*n

for i in range(n):
  for j in range(i):
    if nlist[j]<nlist[i]:
      dp[i]=max(dp[i],dp[j]+1)
      
print(max(dp))