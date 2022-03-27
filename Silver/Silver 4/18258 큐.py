##push pop 하려면 deque 사용하자!


from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
queue=deque()
l=0
for i in range(n):
    do=input().split()
    if do[0]=="push":
        queue.append(do[1])
        l+=1
    elif do[0]=="pop":
        if l==0:
            print(-1)
        else:
            print(queue.popleft())
            l-=1
    elif do[0]=="size":
        print(l)
    elif do[0]=="empty":
        if l==0:
            print(1)
        else:
            print(0)
    elif do[0]=="front":
        if l==0:
            print(-1)
        else:
            print(queue[0])
    else:
        if l==0:
            print(-1)
        else:
            print(queue[-1])
    