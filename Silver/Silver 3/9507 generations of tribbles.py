from collections import defaultdict
import sys

input = sys.stdin.readline
dp = defaultdict(int)
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(int(input())):
    n = int(input())
    if n <= 3:
        print(dp[n])
        continue
    for i in range(4, n + 1):
        if dp[i] == 0:
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4]
    print(dp[n])
