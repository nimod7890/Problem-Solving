from collections import Counter
n=int(input())
nlist=Counter(list(map(int,input().split())))
m=int(input())
print(" ".join(map(str,[1 if nlist[i] else 0 for i in map(int,input().split())])))