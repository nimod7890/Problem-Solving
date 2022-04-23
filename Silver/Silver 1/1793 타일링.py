from collections import defaultdict
import sys

input = sys.stdin.readline
dp = defaultdict(int)
dp[0] = 1
dp[1] = 1

while True:
    try:
        n = int(input())
    except:
        break
    if n <= 1:
        print(dp[n])
        continue
    for i in range(2, n + 1):
        if dp[i] == 0:
            dp[i] = dp[i - 1] + 2 * dp[i - 2]
    print(dp[n])
