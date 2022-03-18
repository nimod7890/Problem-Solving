#답 베낌

N=int(input())
n=0
while(N>=0):
    if N%5==0 :
        n+=(N//5)
        print(n)
        break
    N-=3
    n+=1
else:
    print(-1)
