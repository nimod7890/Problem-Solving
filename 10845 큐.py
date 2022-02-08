import sys


input=sys.stdin.readline
n=int(input())
queue=[]
for i in range(n):
    do=input().split()
    if do[0]=="push":
        queue.append(do[1])
    elif do[0]=="pop":
        if len(queue)==0:
            print(-1)
        else:
            print(queue.pop(0))
    elif do[0]=="size":
        print(len(queue))
    elif do[0]=="empty":
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif do[0]=="front":
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    else:
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])
    