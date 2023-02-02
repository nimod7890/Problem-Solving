N=9901
dp=[1,3,7]
n=int(input())
if n>2:
    for i in range(2,n):
        dp.append((2*dp[i]+dp[i-1])%N)
print(dp[n]%N)