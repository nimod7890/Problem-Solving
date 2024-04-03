import sys
input=sys.stdin.readline


date=list(map(int,input().split()))
standard=[15,28,19]
year=0

while True:
  year+=1
  for i in range(2,-1,-1):
    if (year-date[i])%standard[i]>0:
      break
  else:
    print(year)
    break

    