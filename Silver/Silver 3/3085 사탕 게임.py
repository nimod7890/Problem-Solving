import sys

input = sys.stdin.readline
n = int(input())
nList = [list(input().strip()) for i in range(n)]
maxi = 0


def check(x, y, X, Y):
    global maxi
    nList[x][y], nList[X][Y] = nList[X][Y], nList[x][y]
    for i in range(0, n):
        last = 0
        row = [1]
        for j in range(1, n):
            if nList[i][j] == nList[i][j-1]:
                row[last] += 1
            else:
                last += 1
                row.append(1)
        maxi = max(max(row), maxi)

    for j in range(0, n):
        last = 0
        column = [1]
        for i in range(1, n):
            if nList[i][j] == nList[i-1][j]:
                column[last] += 1
            else:
                last += 1
                column.append(1)
        maxi = max(max(column), maxi)
    nList[x][y], nList[X][Y] = nList[X][Y], nList[x][y]
    return maxi


for i in range(n):
    for j in range(n):
        for x, y in [[i + 1, j], [i, j + 1]]:
            if 0 <= x < n and 0 <= y < n and nList[x][y] != nList[i][j]:
                maxi = check(x, y, i, j)
print(maxi)
