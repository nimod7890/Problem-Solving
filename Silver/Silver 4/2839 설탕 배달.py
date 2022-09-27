n=int(input())

dp=[0]*(n+1)
dp[3]=1
if n>=5:
    dp[5]=1
for i in range(4,n+1):
    if dp[i-5] and dp[i-3]:
        dp[i]=min(dp[i-5],dp[i-3])+1
    elif dp[i-5]:
        dp[i]=dp[i-5]+1
    elif dp[i-3]:
        dp[i]=dp[i-3]+1
if dp[n]: 
    print(dp[n])
else: 
    print(-1) 