# from collections import defaultdict
# n=int(input())
# nlist=sorted([list(map(int,input().split())) for i in range(n)])
 
# maxi=defaultdict(int)
# for i in range(n):
#   newIndex=i+nlist[i][1]
#   maxi[newIndex]=max(maxi[newIndex],maxi[i]+1) #maxi[i]+1 부분이 틀렸
#   print(i,nlist[i],maxi,newIndex)
# print(max(maxi.values()))

n=int(input())
nlist=sorted([list(map(int,input().split())) for i in range(n)],key=lambda x:(x[1],x[0]))
k,cnt=0,0
for a, b in nlist:
    if a>=k:
        cnt+=1
        k=b
print(cnt)