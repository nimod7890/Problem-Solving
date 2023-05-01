from itertools import permutations
n,m=map(int,input().split())
for nlist in permutations(range(1,n+1),m):
    print(" ".join(map(str,nlist)))
