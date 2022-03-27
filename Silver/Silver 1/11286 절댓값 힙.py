import heapq
import sys
input = sys.stdin.readline
n = int(input())
arr = list()
for i in range(n):
    x = int(input())
    if x == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr)[1])
    else:
        heapq.heappush(arr, [abs(x), x])
