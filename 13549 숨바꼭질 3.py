from collections import defaultdict, deque

n, k = map(int, input().split())
visit = defaultdict(int)
will = deque([n])
visit[n] = 1
while will:
    x = will.popleft()
    if x == k:
        break
    for i in [2*x, x-1, x+1]:
        if 0 <= i <= 100000 and visit[i] == 0:
            if i == 2*x:
                visit[i] = visit[x]
                will.appendleft(i)
            else:
                visit[i] = visit[x]+1
                will.append(i)

print(visit[k]-1)
