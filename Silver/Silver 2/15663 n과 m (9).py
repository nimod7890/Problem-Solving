from itertools import permutations
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
for v in sorted(map(list, set(permutations(map(int, input().split()), m)))):
    print(" ".join(map(str, v)))
