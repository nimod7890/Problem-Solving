'''
n=1 -> 1+1+1+1+...+1
n=2 -> 10+9+8+7+...+1
n=3 -> 
'''
dp=[1,1,1,1,1,1,1,1,1,1]
for i in range(int(input())-1):
  dp=[sum(dp[j:]) for j in range(10)]
print(sum(dp)%10007)