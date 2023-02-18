import sys

input=sys.stdin.readline
n=int(input())
nlist=list(map(int,input().split()))
sequence={v:i for i,v in enumerate(sorted(list(set(nlist))))}
print(*[sequence[v] for v in nlist])