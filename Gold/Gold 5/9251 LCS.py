import sys


input=sys.stdin.readline
slist=[list(input().strip()) for i in range(2)]
len1,len2=len(slist[0]),len(slist[1])
dp=[[0 for j in range(len2+1)] for i in range(len1+1)]
for i in range(1,len1+1):
    for j in range(1,len2+1):
        if slist[0][i-1]==slist[1][j-1]:
            dp[i][j]=max(dp[i-1][j-1]+1,dp[i][j-1])
        else:
            dp[i][j]=max(dp[i][j-1],dp[i-1][j])
print(dp[-1][-1])
