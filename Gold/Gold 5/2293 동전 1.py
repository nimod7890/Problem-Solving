import sys

input=sys.stdin.readline
n,k=map(int,input().split())
nlist=[int(input()) for i in range(n)]
dp=[0]*(k+1)
dp[0]=1
for i in nlist:
    for j in range(i,k+1):
        if j>=i:
            dp[j]+=dp[j-i]
print(dp[-1])