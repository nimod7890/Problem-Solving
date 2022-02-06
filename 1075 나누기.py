n=input() #100<=n<2 * 10*9
f=int(input()) #<=100
if len(n)>=3: n=n[:-2]+'00'
n=int(n)
k=n%f
if k!=0: k=f-k
k=str(k)
if len(k)==1: k='0'+k
print(k[:2])