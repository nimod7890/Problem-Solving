import sys
input=sys.stdin.readline
t=int(input())
a=dict()
for i in range(t):
    a[i]=int(input())
a=dict(sorted(a.items(),key=lambda x:x[1]))
flist=[0 for i in range(41)]

def fibonacci(n):
    if n==0: 
        return flist[0]
    if flist[n]!=0:
        return flist[n]
    if n==1:
        flist[1]=1
        return flist[1]
    flist[n]= fibonacci(n-1)+fibonacci(n-2)
    return flist[n]


for value in a.items():
    flist[value[1]]=fibonacci(value[1])
    
for i in range(t):
    if a[i]==0:
        print("1 0")
    elif a[i]==1:
        print("0 1")
    else:
        print(f"{flist[a[i]-1]} {flist[a[i]]}")
    