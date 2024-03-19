import sys

input=sys.stdin.readline

n=int(input())
nlist=list(map(int,input().split()))

dp=[0]*n
dp[0]=nlist[0]

for i in range(1,n):
  dp[i]=max(dp[i-1],nlist[i-1],0)+nlist[i]

print(max(dp))