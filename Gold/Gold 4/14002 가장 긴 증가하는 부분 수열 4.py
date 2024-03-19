import sys
input=sys.stdin.readline

n=int(input())
nlist=list(map(int,input().split()))
dp=[1]*n
path=[-1]*n

for i in range(n):
  for j in range(i):
    if nlist[j]<nlist[i] and dp[i]<dp[j]+1:
      dp[i]=dp[j]+1
      path[i]=j

maxi=max(dp)
index=dp.index(max(dp))
p=[]
while index!=-1:
  p.append(nlist[index])
  index=path[index]
  
print(maxi)
print(*p[::-1],sep=' ')