# https://ddggblog.tistory.com/211

from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)

input=sys.stdin.readline
n=int(input())
graph=defaultdict(list)

def dfs(num):
    visit[num]=1
    dp[num]=[0,1]
    for child in graph[num]:
        if visit[child]==0:
            dfs(child)
            dp[num]=[dp[num][0]+dp[child][1],dp[num][1]+min(dp[child])]
            
for i in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dp=[[0,0] for _ in range(n+1)]
visit=[0]*(n+1)
           
dfs(1)
print(min(dp[1]))