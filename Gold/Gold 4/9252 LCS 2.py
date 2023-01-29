# 풀이 참고
import sys
input=sys.stdin.readline

a=[""]+list(input().strip())
b=[""]+list(input().strip())
aLen,bLen=len(a),len(b)
dp=[[0 for j in range(aLen)] for i in range(bLen)]
ans=""

for i in range(1,bLen):
    for j in range(1,aLen):
        if a[j]==b[i]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])

i=len(b)-1
j=len(a)-1
while i>0 and j>0:
    if dp[i][j]==dp[i-1][j]:
        i-=1
    elif dp[i][j]==dp[i][j-1]:
        j-=1
    else:
        ans+=a[j]
        j-=1
        i-=1
            
print(dp[-1][-1])
if len(ans)!=0:
    print(ans[::-1])