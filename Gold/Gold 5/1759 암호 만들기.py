from itertools import combinations
import sys
input=sys.stdin.readline

L, C = map(int, input().split())

for word in combinations(sorted(input().split()), L):
  cnt_vow=len([1 for i in word if i in "aeiou"])
  if cnt_vow >= 1 and L - cnt_vow >= 2:
    print(*word,sep='')