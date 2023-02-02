n=int(input())
nlist=list(map(int,input().split()))
dp=[0]*(n+1)
for i in range(1,n+1):
    dp[i]=nlist[i-1]
    for j in range(1,i):
        dp[i]=max(dp[i-j]+nlist[j-1],dp[i])
print(dp[-1])