from xmlrpc.client import MAXINT


n = int(input())
nList = [list(input()) for i in range(n)]
maxi = 0


def check(x, y, X, Y):
    global maxi
    nList[x][y], nList[X][Y] = nList[X][Y], nList[x][y]
    for i in range(n):
        for j in range(n):
            pass

    return maxi


for i in range(n):
    for j in range(n):
        for x, y in [[i + 1, j], [i, j + 1]]:
            if 0 <= x < n and 0 <= y < n and nList[x][y] != nList[i][j]:
                maxi = check(x, y, i, j)
