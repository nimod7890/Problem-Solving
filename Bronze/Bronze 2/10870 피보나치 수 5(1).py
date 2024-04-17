a,b=0,1
n=int(input())
if n==0:
  print(0)
  exit()
  
for i in range(n-1):
  a,b=b,(a+b)
print(b)
