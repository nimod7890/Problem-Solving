from itertools import permutations
n,m=map(int,input().split())
for v in permutations(range(1,n+1),m):
    print(" ".join(str(x) for x in v))