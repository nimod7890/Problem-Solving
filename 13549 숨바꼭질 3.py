from collections import defaultdict, deque

n, k = map(int, input().split())
visit = defaultdict(int)
visit[n] = 1
will = deque([n])
ans = []
while will:
    x = will.popleft()
    if x == k:
        ans.append(visit[k])
    for i in [x-1, x+1, 2*x]:
        if i == n:
            continue
        if 0 <= i <= 100000 and visit[i] == 0:
            will.append(i)
            if i == 2*x:
                visit[i] = visit[x]
            else:
                visit[i] = visit[x]+1
print(len(ans))
print(min(ans))
