import sys
input=sys.stdin.readline
f=lambda:map(int,input().split())
n,m=f()
b=[0]*m
for i in range(n):
    p=0;b=[p:=c+max(p,d) for c,d in zip(f(),b)]
print(p)