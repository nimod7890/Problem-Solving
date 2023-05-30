import bisect
import sys
input=sys.stdin.readline
n=int(input())
nlist=[]
for num in map(int,input().split()):
    if len(nlist)==0 or nlist[-1]<num:
        nlist.append(num)
        continue
    nlist[bisect.bisect_left(nlist,num)]=num
print(len(nlist))