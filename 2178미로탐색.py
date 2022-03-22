from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
will = deque()
will.append([0, 0])
miro = [list(input().strip()) for i in range(n)]

while will:
    i, j = will.popleft()
    for N, M in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:
        if 0 <= N < n and 0 <= M < m and miro[N][M] == '1':
            will.append([N, M])
            miro[N][M] = int(miro[i][j])+1
print(miro[n-1][m-1])
