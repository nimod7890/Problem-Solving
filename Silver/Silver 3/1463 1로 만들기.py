from collections import defaultdict

n = int(input())
dp = defaultdict(int)
for i in range(2, n+1):
    dp[i] = dp[i-1]+1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
print(dp[n])
