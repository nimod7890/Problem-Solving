import sys

input=sys.stdin.readline
n,m=map(int,input().split())
hap=[0]*(n+1)
cnt=0
for idx,num in enumerate(list(map(int,input().split()))):
    hap[idx+1]+=hap[idx]+num
for i in range(n):
    if hap[i]+m in hap[i+1:]:
        cnt+=1 
print(cnt)