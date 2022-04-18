import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    nlist = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = nlist[0]
    for i in range(1, n):
        dp[i] = max(dp[i - 1] + nlist[i], nlist[i])
    print(max(dp))
