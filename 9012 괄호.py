import sys
input=sys.stdin.readline
n=int(input())
for j in range(n):
    arr=input()
    stack=0
    for i in arr:
        if i=="(":
            stack+=1
        elif i==")":
            stack-=1
        if stack<0:
            print("NO")
            break
    else:
        if stack==0: print("YES")
        else: print("NO")