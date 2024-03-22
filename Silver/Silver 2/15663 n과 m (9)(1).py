import itertools
import sys

input=sys.stdin.readline
n,m=map(int,input().split())
nlist=sorted(list(set(itertools.permutations(map(int,input().split()),m))))
for values in nlist:
  print(" ".join(list(map(str,values))))