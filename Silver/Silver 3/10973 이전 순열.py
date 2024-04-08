import sys
input=sys.stdin.readline

def find_before():
  i=n-2
  while i>=0 and nlist[i]<nlist[i+1]:
    i-=1

  if i<0:
    print(-1)
    return 
    
  j=n-1
  while nlist[i]<nlist[j]:
    j-=1

  nlist[i],nlist[j]=nlist[j],nlist[i]
  nlist[i+1:]=nlist[i+1:][::-1]
  print(*nlist)


n=int(input())
nlist=list(map(int,input().split()))

find_before()