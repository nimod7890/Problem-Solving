from collections import defaultdict, deque

n, k = map(int, input().split())
visit = defaultdict(int)
will = deque([n])
while will:
    x = will.popleft()
    if x == k:
        break
    for i in [x-1, x+1, 2*x]:
        if 0 <= i <= 100000 and visit[i] == 0:
            will.append(i)
            visit[i] = visit[x]+1

print(visit[k])
