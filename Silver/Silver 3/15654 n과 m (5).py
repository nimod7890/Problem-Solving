from itertools import permutations
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
for nList in permutations(sorted(map(int, input().split())), m):
    print(" ".join(map(str, nList)))
