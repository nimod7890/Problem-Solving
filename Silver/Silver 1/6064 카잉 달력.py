import sys
input=sys.stdin.readline
  
for _ in range(int(input())):
  m,n,x,y=map(int,input().split())
  year=x
  
  while year<=m*n:
    if year%n==y or (n==y and year%n==0):
      print(year)
      break
    year+=m
  else: 
    print(-1)