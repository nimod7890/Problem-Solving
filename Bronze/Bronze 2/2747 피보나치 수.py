a,b=0,1
for i in range(int(input())-1):
  a,b=b,(a+b)
print(b)