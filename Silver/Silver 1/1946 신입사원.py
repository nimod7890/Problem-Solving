# 문제 이해를 멍청하게 했
import sys

input=sys.stdin.readline
for i in range(int(input())):
    n=int(input())
    nlist=[0]*(n+1)
    for i in range(n):
        a,b=map(int,input().split())
        nlist[a]=b
    mMax=nlist[1]
    cnt=0
    for a,b in enumerate(nlist[1:]):
        if b<=mMax:
            cnt+=1
            mMax=b
    print(cnt)

'''
1
6
6 4
4 1
5 2
1 6
2 3
3 5
-> 3
'''