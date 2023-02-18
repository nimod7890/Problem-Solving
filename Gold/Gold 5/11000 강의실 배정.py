import heapq
import sys

input=sys.stdin.readline
li=[]
for s,t in sorted([list(map(int,input().split())) for i in range(int(input()))]):
    if li and s>=li[0]:
        heapq.heappop(li)
    heapq.heappush(li,t)
print(len(li))
