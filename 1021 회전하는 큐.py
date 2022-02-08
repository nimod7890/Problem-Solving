from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
cnt=0
deq=deque(i+1 for i in range(n))
for v in map(int,input().split()):
    idx=deq.index(v)
    if idx==0:
        deq.popleft()
        continue
    if idx<=len(deq)//2:
        deq.rotate(-idx)
        cnt+=idx
    else:
        deq.rotate(len(deq)-idx)
        cnt+=len(deq)-idx
    deq.popleft()
print(cnt)