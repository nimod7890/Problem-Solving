from itertools import product
n,m=map(int,input().split())
for v in product(range(1,n+1),repeat=m):
    print(" ".join(str(i) for i in v))