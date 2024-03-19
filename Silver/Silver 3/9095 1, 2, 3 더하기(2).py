import sys
input=sys.stdin.readline

# process

dp=[0]*11
dp[:3]=[1,2,4,7]

for i in range(4,11):
  dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
  
# output

for t in range(int(input())):
  print(dp[int(input())-1])  