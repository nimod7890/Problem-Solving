from math import inf
import sys
input=sys.stdin.readline


def backtracking(count:int,curr:int) -> None:
  global ans,visited
  
  if count==n//2:
    tmp=[0,0]
    
    for i in range(n):
      for j in range(i+1,n):
        if (visited&(1<<i)) and (visited&(1<<j)):
          tmp[0]+=ability[i][j]+ability[j][i]
        if not (visited&(1<<i)) and not (visited&(1<<j)):
          tmp[1]+=ability[i][j]+ability[j][i]
          
    ans=min(abs(tmp[0]-tmp[1]),ans)
    return 
  
  for i in range(curr,n):
    if visited&(1<<i): 
      continue
    
    visited^=(1<<i)
    backtracking(count+1,i+1)
    visited^=(1<<i)
    

n=int(input())
ability=[[*map(int,input().split())] for i in range(n)]

visited=0
ans=inf
backtracking(0,0)
print(ans)