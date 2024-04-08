from itertools import permutations
import sys
input=sys.stdin.readline

for li in list(permutations(range(1,int(input())+1))):
  print(*li)