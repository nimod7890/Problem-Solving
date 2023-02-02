N=9901
dp=[[1,1,1]]
for i in range(1,int(input())):
    a,b,c=dp[i-1]
    dp.append([(a+b+c)%N,(a+c)%N,(a+b)%N])
print(sum(dp[-1])%N)