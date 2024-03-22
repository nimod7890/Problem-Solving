import itertools
import sys

input=sys.stdin.readline
n,m=map(int,input().split())

for nlist in itertools.combinations_with_replacement(range(1,n+1),m):
  print(" ".join(list(map(str,nlist))))