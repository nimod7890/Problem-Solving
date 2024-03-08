from collections import  deque
import sys
input=sys.stdin.readline
MAX=100001

# input
N,K=map(int,input().split())

# 예외 처리
if N>=K:
  print(N-K)
  exit()
  
# init
visited=[-1]*MAX
visited[N]=0
next=deque([N]) 

# process
while next: 
  start=next.popleft()
  if start==K:
    break
  
  for end in [start*2,start-1,start+1]:
    if 0<=end<MAX and visited[end]==-1:
      if end==start*2:
        visited[end]=visited[start]
        next.appendleft(end)
      else:
        visited[end]=visited[start]+1
        next.append(end)
      
# output
print(visited[K])