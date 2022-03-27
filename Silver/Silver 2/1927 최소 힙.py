import heapq
import sys
input = sys.stdin.readline
minheap = []
n = int(input())
num = 0
for i in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(minheap, x)
        num += 1
    elif x == 0:
        if num == 0:
            print(0)
        else:
            print(heapq.heappop(minheap))
            num -= 1
