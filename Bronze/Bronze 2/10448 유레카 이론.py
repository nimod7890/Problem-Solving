from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline
tlist = []
k = num = 1
while num <= 1000:
    tlist.append(num)
    k += 1
    num += k
for _ in range(int(input())):
    n = int(input())
    for i, j, k in combinations_with_replacement(tlist, 3):
        if i+j+k == n:
            print(1)
            break
    else:
        print(0)
