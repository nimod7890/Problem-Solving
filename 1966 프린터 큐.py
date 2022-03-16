from collections import deque
import sys

input = sys.stdin.readline
t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    nlist = [[idx, x] for idx, x in enumerate(map(int, input().split()))]
    important = sorted(nlist[:], reverse=True, key=lambda x: x[1])

    cnt = 0
    while True:
        x = nlist.pop(0)
        if x[1] < important[0][1]:  # 뒤에 재배치
            nlist.append(x)
            continue
        cnt += 1
        if m == x[0]:
            break
        important.pop(0)
    print(cnt)
