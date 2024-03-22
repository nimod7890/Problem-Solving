import itertools
import sys

input=sys.stdin.readline
n,m=map(int,input().split())
for values in itertools.product(sorted(set(map(int,input().split()))),repeat=m):
  print(*values)