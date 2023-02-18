#메모리 초과 ~~
import sys

input=sys.stdin.readline
n=int(input())
nlist=[sorted(map(int,input().split()),reverse=True) for i in range(n)]
ilist=[0]*n
m=0
for i in range(n): #iter
    m=nlist[n-1][ilist[n-1]]
    l=n-1
    for line in reversed(range(n-1)): #line 
        v=nlist[line][ilist[line]]
        if v>m:
            l=line
            m=v
        else:
            break
    ilist[l]+=1
print(m)