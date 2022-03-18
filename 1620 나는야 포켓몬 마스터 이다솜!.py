import sys
input = sys.stdin.readline
n, m = map(int, input().split())
pocketmon = dict()
for i in range(n):
    name = input().strip()
    pocketmon[str(i+1)] = name
    pocketmon[name] = str(i+1)
for i in range(m):
    print(pocketmon.get(input().strip()))
