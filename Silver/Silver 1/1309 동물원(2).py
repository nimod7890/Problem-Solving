dp=[[1,1]]
for i in range(1,int(input())+1):
    dp.append([sum(dp[i-1])%9901,(dp[i-1][0]*2+dp[i-1][1])%9901])
print(dp[-1][1]%9901)