import heapq,sys

input=sys.stdin.readline
heap=[]
for i in range(int(input())):
    for v in map(int,input().split()):
        if i==0:
            heapq.heappush(heap,v)
            continue
        if heap[0]<v:
            heapq.heappush(heap,v)
            heapq.heappop(heap)
print(heap[0])