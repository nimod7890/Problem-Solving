import itertools
import sys

input=sys.stdin.readline
n,m=map(int,input().split())
nlist=sorted(set(itertools.combinations(sorted(map(int,input().split())),m)))
for values in nlist:
  print(*values)