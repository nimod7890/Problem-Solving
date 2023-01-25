import sys
input=sys.stdin.readline

n,m=map(int,input().split())
nlist=dict()

for i in range(n):
    n=input().strip()
    nlist[str(i+1)]=n
    nlist[n]=str(i+1)

for i in range(m):
    print(nlist.get(input().strip()))