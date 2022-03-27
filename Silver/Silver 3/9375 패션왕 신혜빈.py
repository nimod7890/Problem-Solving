from collections import defaultdict
import sys
input = sys.stdin.readline
c = int(input())
for i in range(c):
    n = int(input())
    nlist = defaultdict(list)
    for j in range(n):
        name, kind = input().split()
        nlist[kind].append(name)
    num = 1
    for value in nlist.values():
        num *= (len(value)+1)
    print(num-1)
