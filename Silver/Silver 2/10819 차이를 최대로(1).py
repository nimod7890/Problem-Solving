from itertools import permutations
import sys
input=sys.stdin.readline

n=int(input())
print(max(sum(abs(a-b) for a,b in zip(li,li[1:])) for li in permutations(map(int,input().split()))))