n=int(input())
nlist=list(map(int,input().split()))
mlist=list(map(int,input().split()))
mini=mlist[0]
ans=0
for n,m in zip(nlist,mlist):
    if mini>m:
        mini=m
    ans+=n*mini
print(ans)