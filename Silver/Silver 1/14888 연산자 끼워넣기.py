from math import inf
import sys
input=sys.stdin.readline

operations = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: -(abs(x)//y) if x<0 and y>0 else x // y]

def backtracking(index,curr):
  global ans
  
  if index==n:
    ans=[max(ans[0],curr),min(ans[1],curr)]
    return
  
  for i in range(4):
    if operator_count[i]==0:
      continue
    
    operator_count[i]-=1
    backtracking(index+1,operations[i](curr, nlist[index]))
    operator_count[i]+=1

n=int(input())
nlist=list(map(int,input().split()))
operator_count=list(map(int,input().split()))

ans=[-inf,inf] 
backtracking(1,nlist[0])
print(*ans,sep='\n')