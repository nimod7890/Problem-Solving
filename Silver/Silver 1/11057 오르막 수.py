from collections import defaultdict
n=int(input())
dp=defaultdict(list)
dp[0]=[1]*10
for i in range(1,n):
    dp[i]=[sum(dp[i-1][:j+1])%10007 for j in range(10)]
print(sum(dp)%10007)