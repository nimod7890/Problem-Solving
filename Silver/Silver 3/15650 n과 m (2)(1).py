from itertools import combinations

n,m=map(int,input().split())
for nlist in combinations(range(1,n+1),m):
    print(" ".join(map(str,nlist)))