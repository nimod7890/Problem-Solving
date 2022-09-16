from collections import Counter
n=int(input())
nlist=Counter(list(map(int,input().split())))
m=int(input())
mlist=list(map(int,input().split()))
print(" ".join(map(str,[nlist[i] for i in mlist])))