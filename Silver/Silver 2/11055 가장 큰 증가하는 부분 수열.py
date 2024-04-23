import sys

input = sys.stdin.readline
n = int(input())
nList = list(map(int, input().split()))
dp = [0] * n
for i in range(n):
    dp[i] = nList[i]
    for j in range(i):
        if nList[i] > nList[j]:
            dp[i] = max(dp[i], dp[j] + nList[i])
print(max(dp))
