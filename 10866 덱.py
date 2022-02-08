from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
l=deque()
for i in range(n):
    go=input().split()
    if go[0]=="push_front":
        l.appendleft(go[1])
    if go[0]=="push_back":
        l.append(go[1])
    elif go[0]=="pop_front":
        if len(l)==0: print(-1)
        else:print(l.popleft())
    elif go[0]=="pop_back":
        if len(l)==0: print(-1)
        else:print(l.pop())
    elif go[0]=="size":
        print(len(l))
    elif go[0]=="empty":
        print(1) if len(l)==0 else print(0)
    elif go[0]=="front":
        if len(l)==0: print(-1)
        else: print(l[0])
    elif go[0]=="back":
        if len(l)==0: print(-1)
        else: print(l[-1])