import heapq
import sys

input = sys.stdin.readline
n = int(input())
heap = []
for i in range(n):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)*(-1))
    else:
        heapq.heappush(heap, (-1)*x)
