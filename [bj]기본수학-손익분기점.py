##멍청했다 while이 아예 필요가 없구나!
import sys
input=sys.stdin.readline

a,b,c=map(int,input().split())
x=0
k=b-c
sum=a
if k>=0:
    print(-1)
else:
    print(int(a/-k+1))
