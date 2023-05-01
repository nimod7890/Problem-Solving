from itertools import combinations
import sys

input=sys.stdin.readline
n,m=map(int,input().split())
nlist=[*map(int,input().split())]
cnt=0
for i in range(1,n+1):
    for li in combinations(nlist,i):
        if sum(li)==m:
            cnt+=1
print(cnt)