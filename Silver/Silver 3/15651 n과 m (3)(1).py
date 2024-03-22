import itertools
import sys

input=sys.stdin.readline
n,m=map(int,input().split())

for nlist in itertools.product(range(1,n+1),repeat=m):
  print(" ".join(list(map(str,nlist))))