
import sys


input=sys.stdin.readline
A,B=input(),input()
dp=[[""]*len(B) for i in range(2)]
a,b=0,1
for i in range(1,len(A)):
  a,b=b,a
  for j in range(1,len(B)):
    if A[i-1]==B[j-1]:
      dp[a][j]=dp[b][j-1]+A[i-1]
    else:
      dp[a][j]=dp[a][j-1] if len(dp[a][j-1])>=len(dp[b][j]) else dp[b][j]
print(len(dp[a][-1]))
print(dp[a][-1])
