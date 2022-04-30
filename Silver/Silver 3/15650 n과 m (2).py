from itertools import combinations
n,m=map(int,input().split())
for v in combinations(range(1,n+1),m):
    print(" ".join(str(x) for x in v))
