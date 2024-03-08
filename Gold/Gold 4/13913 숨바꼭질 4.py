from collections import defaultdict, deque
import sys
input=sys.stdin.readline
MAX=100001

# input
N,K=map(int,input().split())

# 예외 처리
if N>=K:
  print(N-K)
  print(*[i for i in range(N,K-1,-1)])
  exit()
  
# init
visited=[-1]*MAX
next=deque([N]) 

# process
while next: 
  start=next.popleft()
  if start==K:
    break
  
  for end in [start-1,start*2,start+1,]:
    if 0<=end<MAX and visited[end]==-1:
      visited[end]=start
      next.append(end)
      
# output
path=deque()
while K!=N:
  path.appendleft(K)
  K=visited[K]
path.appendleft(N)

print(len(path)-1)
print(*path)