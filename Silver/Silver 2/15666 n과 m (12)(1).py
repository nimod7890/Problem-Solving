import itertools
import sys

input=sys.stdin.readline
n,m=map(int,input().split())
for values in itertools.combinations_with_replacement(sorted(set(map(int,input().split()))),m):
  print(*values)