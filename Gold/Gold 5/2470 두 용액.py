import sys

input=sys.stdin.readline
n=int(input())
nlist=sorted(list(map(int,input().split())))
i,j=0,n-1
mini=abs(nlist[i]+nlist[j])
while i<j:
    new=nlist[i]+nlist[j]
    if abs(new)<=mini:
       ans=[nlist[i],nlist[j]]
       mini=abs(nlist[i]+nlist[j])
    if new>0: 
        j-=1
    else: 
        i+=1
print(*ans)