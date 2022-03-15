import sys


input = sys.stdin.readline
t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    important = [[idx, x] for idx, x in enumerate(map(int, input().split()))]
