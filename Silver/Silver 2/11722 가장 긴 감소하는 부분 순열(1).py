n=int(input())
nlist=list(map(int,input().split()))
cnt=[1]*n
for i in range(1,n):
    for j in range(i):
        if nlist[j]>nlist[i]:
            cnt[i]=max(cnt[j]+1,cnt[i]) #
print(max(cnt))