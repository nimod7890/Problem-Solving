from collections import defaultdict
import sys

input = sys.stdin.readline
n = int(input())
if n == 1:
    print(int(input()))
    exit(0)
graph = [0]
for i in range(n):
    graph.append(int(input()))
dp = defaultdict(int)
dp[0], dp[1], dp[2] = 0, graph[1], graph[2]+dp[1]
for i in range(2, n+1):
    dp[i] = max(dp[i-2], dp[i-3]+graph[i-1])+graph[i]
print(dp[n])

# 세번째 계단은 첫번째 계단에서 두 개 건너 띈 다음꺼 or
# 0번째 계단 + 두번째 계단 다음꺼
