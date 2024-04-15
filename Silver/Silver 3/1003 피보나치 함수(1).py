import sys
input=sys.stdin.readline

count=[[1,0],[0,1]]
for _ in range(int(input())):
  n=int(input())
  if n>=len(count):
    for i in range(len(count),n+1):
      count.append([count[i-1][0]+count[i-2][0],count[i-1][1]+count[i-2][1]])
  print(*count[n])