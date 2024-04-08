from math import inf
import sys
input=sys.stdin.readline


def dfs(init,start,visited):
  if visited==visited_all:
    return graph[start][init] if graph[start][init] else inf
  
  if dp[start][visited]!=inf:
    return dp[start][visited]
  
  for end in range(n):
    if graph[start][end]==0 or visited&(1<<end):
      continue
    
    dp[start][visited]=min(dp[start][visited],graph[start][end]+dfs(init,end,visited|(1<<end)))
    
  return dp[start][visited]


n=int(input())
graph=[list(map(int,input().split())) for i in range(n)]
dp=[[inf]*(1<<n) for i in range(n)]

visited_all=(1<<n)-1
  
print(dfs(0,0,1))