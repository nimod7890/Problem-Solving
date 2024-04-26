import sys
input=sys.stdin.readline

n=int(input())+1
  
print(sum(p*(n:=n-1) for p in sorted(map(int,input().split()))))