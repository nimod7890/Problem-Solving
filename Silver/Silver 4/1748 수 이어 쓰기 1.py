import sys
input=sys.stdin.readline
n=input().rstrip()
digit=len(n)
if digit==1:
  print(n)
else:
  ans=0
  num=0
  for i in range(digit-1):
    num+=9*(10**i)
    ans+=9*(10**i)*(i+1)
  ans+=(int(n)-num)*digit
  print(ans)