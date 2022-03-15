from collections import deque
import sys
input = sys.stdin.readline


def quick(queue):
    if len(queue) < 2:
        return queue
    piv = queue[len(queue)//2]
    small, equal, big = [], [], []
    for x in queue:
        if x < piv:
            small.append(x)
        elif x > piv:
            big.append(x)
        else:
            equal.append(x)
    return quick(small)+equal+quick(big)


t = int(input())
for i in range(t):
    k = int(input())
    queue = deque()
    for j in range(k):
        do = input().split()
        num = int(do[1])
        if do[0] == 'I':
            queue.append(num)
            queue = quick(queue)
        else:
            if len(queue) != 0:
                if do[1] == '1':
                    queue.pop()
                else:
                    queue.pop(0)
    if len(queue) == 0:
        print("EMPTY")
    else:
        print(f"{queue[-1]} {queue[0]}")
