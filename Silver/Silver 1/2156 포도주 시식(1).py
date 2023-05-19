n=int(input())
nlist=[int(input()) for _ in range(n)]
if n==1:
    print(nlist[0])
elif n==2:
    print(nlist[0]+nlist[1])
elif n==3:
    print(max(nlist[0]+nlist[2],nlist[1]+nlist[2],nlist[0]+nlist[1]))
else:
    dp=[nlist[0],nlist[0]+nlist[1],max(nlist[0]+nlist[2],nlist[1]+nlist[2],nlist[0]+nlist[1])]
    for i in range(3,n):
        dp.append(max(dp[i-2]+nlist[i],dp[i-3]+nlist[i-1]+nlist[i],dp[i-1]))
    print(dp[-1])