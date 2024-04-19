import sys
input=sys.stdin.readline

A,B=input(),input()
dp=[[0]*len(B) for i in A]

for i in range(1,len(A)):
  for j in range(1,len(B)):
    dp[i][j]=dp[i-1][j-1]+1 if A[i-1]==B[j-1] else max(dp[i-1][j],dp[i][j-1])

print(dp[-1][-1])
