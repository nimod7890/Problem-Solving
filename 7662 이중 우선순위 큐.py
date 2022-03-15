import heapq
import sys
input = sys.stdin.readline


t = int(input())
for i in range(t):
    k = int(input())
    min_heap = []
    max_heap = []
    for j in range(k):
        do = input().split()
        num = int(do[1])
        if do[0] == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        else:
            if len(min_heap) != 0:
                if do[1] == '1':
                    min_heap.remove(-heapq.heappop(max_heap))
                else:
                    max_heap.remove(-heapq.heappop(min_heap))

    if len(min_heap) == 0:
        print("EMPTY")
    else:
        print(f"{min_heap[-1]} {min_heap[0]}")
