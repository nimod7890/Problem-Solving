
from collections import defaultdict, deque


n=int(input())
nlist=defaultdict()
will=deque()
if n%3==0:
    tmp=n
    cnt=0
    while tmp%3==0:
        cnt+=1
        tmp//=3
    will.append([tmp,cnt])
    print([tmp,cnt])
will.append([n-1,1])
ans=[]
while will:
    n,cnt=will.popleft()
    if n==1: 
        ans.append(cnt)
    if n<1: continue
    if n%3==0:
        will.appendleft([n//3,cnt+1])
    elif n%2==0:
        will.append([n//2,cnt+1])
    else:
        will.append([n-1,cnt+1])
    print(will)
print(min(ans))