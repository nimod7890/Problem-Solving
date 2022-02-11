n=int(input())
nlist=list(map(int,input().split()))
maxNum=max(nlist)
prime=[True for i in range(maxNum-1)]
prime.insert(0,False)
cnt=0
for i in range(1,maxNum+1):
    if prime[i-1]==False: continue
    if i in nlist:
        cnt+=1
        del nlist[nlist.index(i)]
    for idx in range(2,maxNum):
        if idx*i>maxNum: break
        prime[idx*i-1]=False
print(cnt)