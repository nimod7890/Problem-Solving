import sys

input=sys.stdin.readline
nlist=[]
for i in range(int(input())):
    n=int(input())
    if n==0:
        nlist.pop()
    else:
        nlist.append(n)
print(sum(nlist))