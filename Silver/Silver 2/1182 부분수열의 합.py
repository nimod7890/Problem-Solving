from itertools import combinations
import sys
input = sys.stdin.readline
n, s = map(int, input().split())
num = 0
arr = list(map(int, input().split()))
for i in range(1, n+1):
    for x in combinations(arr, i):
        if sum(x) == s:
            num += 1
print(num)
