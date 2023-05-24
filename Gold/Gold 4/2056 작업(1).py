import sys


input=sys.stdin.readline
time=[0]
n=int(input())
count=[0]*(n+1)
for i in range(n):
    tmp=list(map(int,input().split()))
    for v in tmp[1:]:
        count[i+1]=max(count[i+1],count[v]+tmp[0])
        
print(max(count))