n, k = map(int, input().split())
if n == k or k == 0:
    print(1)
elif k == 1:
    print(n)
else:
    dp = [[1 for j in range(i+1)] for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            if i == j or j == 0:
                continue
            dp[i][j] = (dp[i-1][j-1]+dp[i-1][j]) % 10007
    print((dp[n-1][k-1]+dp[n-1][k]) % 10007)
