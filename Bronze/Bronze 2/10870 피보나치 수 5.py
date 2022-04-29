from collections import defaultdict


n = int(input())
dp = defaultdict(int)
dp[0] = 0
dp[1] = 1
if n == 1:
    print(dp[n])
    exit()
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[n])
