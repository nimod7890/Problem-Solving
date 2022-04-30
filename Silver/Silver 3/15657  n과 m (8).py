from itertools import combinations_with_replacement
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
for nList in combinations_with_replacement(sorted(map(int, input().split())), m):
    print(" ".join(map(str, nList)))
