from collections import defaultdict


n = int(input())
pinary = defaultdict(list)
pinary[1] = [0, 1]
if n == 1:
    print(1)
    exit(0)
for i in range(2, n+1):
    pinary[i] = [pinary[i-1][1]+pinary[i-1][0], pinary[i-1][0]]
print(pinary[i][0]+pinary[i][1])
