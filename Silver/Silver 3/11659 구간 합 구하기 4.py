import sys

input = sys.stdin.readline
n, m = map(int, input().split())
sumList = [0]
for i, v in enumerate(map(int, input().split())):
    sumList.append(v + sumList[i])
for _ in range(m):
    i, j = map(int, input().split())
    print(sumList[j] - sumList[i - 1])
