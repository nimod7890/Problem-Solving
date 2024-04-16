import sys
input=sys.stdin.readline

for _ in range(int(input())):
  k,n=int(input()),int(input())
  dp=[i+1 for i in range(n)]
  
  for i in range(k):
    dp=[sum(dp[:j]) for j in range(1,n+1)]
  print(dp[-1])