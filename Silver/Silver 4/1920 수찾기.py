import sys
input=sys.stdin.readline
       
n=int(input())
nlist=list(map(int,input().split()))
m=int(input())
mlist=list(map(int,input().split()))

def goFast(start,end,M):
    pivot=(start+end)//2
    if M==nlist[pivot]:
        print(1)
        return
    if end-start==1:
        print(0)
        return
    if M<nlist[pivot]:
        goFast(start,pivot,M)
    else: 
        goFast(pivot,end,M)
 
nlist.sort()
for M in mlist:
    goFast(0,n,M)