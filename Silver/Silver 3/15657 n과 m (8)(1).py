import itertools
import sys

input=sys.stdin.readline
n,m=map(int,input().split())
nlist=sorted(list(map(int,input().split())))

for values in itertools.combinations_with_replacement(nlist,m):
  print(" ".join(list(map(str,values))))