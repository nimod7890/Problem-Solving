from itertools import combinations
import sys


input=sys.stdin.readline

n,s=map(int,input().split())
nlist=sorted(map(int,input().split()))

print(sum(sum(1 if sum(li)==s else 0 for li in  combinations(nlist,i)) for i in range(1,n+1)))

