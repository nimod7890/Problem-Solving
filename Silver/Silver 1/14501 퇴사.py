import sys


input = sys.stdin.readline
n = int(input())
nlist = [list(map(int, input().split())) for i in range(n)]
dp = [0]*n
for i in reversed(range(n-1)):
    if i+nlist[i][0] > n-1:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], nlist[i][1]+dp[i+nlist[i][0]])
print(dp[0])
'''
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

'''
