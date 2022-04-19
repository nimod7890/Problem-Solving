from collections import defaultdict
import sys

input = sys.stdin.readline
n = int(input())
triangle = defaultdict(list)
triangle[0] = [int(input())]
for i in range(1, n):
    triangle[i] = list(map(int, input().split()))
dp = defaultdict(list)
if n == 1:
    print(triangle[0][0])
    exit()
dp[0] = [triangle[0][0]]
dp[1] = [dp[0][0]+triangle[1][0], dp[0][0]+triangle[1][1]]
if n == 2:
    print(max(dp[n-1]))
    exit()
for i in range(2, n):
    for j in range(i):
        if j == 0:
            dp[i].append(dp[i-1][j]+triangle[i][j])
        elif j == i-1:
            dp[i].append(max(dp[i-1][j], dp[i-1][j-1])+triangle[i][j])
            dp[i].append(dp[i-1][j]+triangle[i][j+1])
        else:
            dp[i].append(max(dp[i-1][j], dp[i-1][j-1])+triangle[i][j])
print(max(dp[n-1]))
