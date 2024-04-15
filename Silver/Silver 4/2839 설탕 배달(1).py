from collections import deque

n=int(input())
will=deque([[n,0]])
visited=[0]*(n+1)
while will:
  kg,num=will.popleft()
  if kg==0:
    print(num)
    break
  if kg<0 or visited[kg]:
    continue
  
  visited[kg]=1
  will.extend([[kg%5,num+kg//5],[kg-3,num+1]])
else:
  print(-1)
