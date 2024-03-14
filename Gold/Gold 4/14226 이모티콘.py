from collections import defaultdict, deque
import sys
input=sys.stdin.readline

# process
def bfs():
  # init
  visited=set()
  visited.add((1,0))
  next=deque([(1,0,0)]) # value, copy, count

  while next:
    start,copy,cnt=next.popleft()
    if start==s:
      return cnt
    
    cases=[(start,start),(start+copy,copy),(start-1,copy)]
    
    for case in cases:
      if start<0 or start>s:
        continue
      if case not in visited:
        visited.add(case)
        a,b=case
        next.append((a,b,cnt+1))
      
  return None # cannot access
      
# input
s=int(input())

# output
print(bfs())
