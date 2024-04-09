from itertools import combinations
import sys
input=sys.stdin.readline

while True:
  k,*nlist=list(map(int,input().split()))
  
  if k==0:
    break
  
  for li in combinations(nlist,6):
    print(*li)
    
  print()