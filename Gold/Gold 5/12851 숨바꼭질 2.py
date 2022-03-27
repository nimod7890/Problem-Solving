from collections import defaultdict, deque

n, k = map(int, input().split())
visit = defaultdict(int)
will = deque([n])
ans = 0
while will:
    x = will.popleft()
    if x == k:
        ans += 1
        continue
    go = [x-1, x+1, 2*x]
    for idx, i in enumerate(go):
        if 0 <= i <= 100000 and (visit[i] == 0 or visit[i] == visit[x]+1):
            will.append(i)
            visit[i] = visit[x]+1

print(visit[k])
print(ans)
