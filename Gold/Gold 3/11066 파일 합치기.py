import sys

input=sys.stdin.readline
for i in range(int(input())):
    n=int(input())
    dp=[[0]*n for i in range(n)]
    mini=0
    dic=[mini:=i+mini for i in map(int,input().split())]
    dic.append(0)
    for j in range(1,n):
        for k in range(n-1):
            if (e:=k+j) >=n: break
            dp[k][e]=float("inf")
            for m in range(k,e):
                dp[k][e]=min(dp[k][e],dp[k][m]+dp[m+1][e]+dic[e]-dic[k-1])
    print(dp[0][-1])