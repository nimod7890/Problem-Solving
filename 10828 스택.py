import sys
input=sys.stdin.readline
n=int(input())
l=[]
for i in range(n):
    go=input().split()
    if go[0]=="push":
        l.append(go[1])
    elif go[0]=="pop":
        if len(l)==0: print(-1)
        else:print(l.pop())
    elif go[0]=="size":
        print(len(l))
    elif go[0]=="empty":
        print(1) if len(l)==0 else print(0)
    elif go[0]=="top":
        if len(l)==0: print(-1)
        else: print(l[-1])