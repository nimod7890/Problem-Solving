from collections import Counter
n=int(input())
nlist=Counter(list(map(int,input().split())))
m=int(input())
print(" ".join(map(str,[nlist[i] for i in map(int,input().split())])))