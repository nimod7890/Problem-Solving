n=int(input())
num=0
while n:
  if n%5==0:
    print(num+n//5)
    break
  n-=3
  num+=1
else:
  print(-1)
