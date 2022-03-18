#풀었슴

N=1000-int(input())
n=0;K=[500,100,50,10,5,1]
for i in range(6):
    if K[i]>N: continue
    if N//K[i]>0:
        n+=(N//K[i])
        N%=K[i]
    if N==0: break
print(n)