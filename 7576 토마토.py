from collections import deque


m, n = map(int, input().split())
apples = []
will = deque()
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j] == 1:
            will.append([i, j])
    apples.append(tmp)
for apple in apples:
    if 0 in apple:
        break
else:
    print(0)
    exit(0)
while will:
    y, x = will.popleft()
    go = [[y-1, x], [y+1, x], [y, x-1], [y, x+1]]
    for N, M in go:
        if 0 <= N < n and 0 <= M < m and apples[N][M] == 0:
            will.append([N, M])
            apples[N][M] = apples[y][x]+1
maxi = 0
for apple in apples:
    if 0 in apple:
        print(-1)
        break
    maxi = max(maxi, max(apple))
else:
    print(maxi-1)
