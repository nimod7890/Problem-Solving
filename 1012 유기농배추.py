import sys
sys.setrecursionlimit(10**5)


def visiting(x, y):
    global visit_list
    if visit_list[y][x] == 1:
        return
    visit_list[y][x] = 1
    if x-1 >= 0 and bachu_list[y][x-1] == 1:
        visiting(x-1, y)
    if x+1 < m and bachu_list[y][x+1] == 1:
        visiting(x+1, y)  # visit right node
    if y+1 < n and bachu_list[y+1][x] == 1:
        visiting(x, y+1)  # visit lower node


t = int(input())
for i in range(t):
    m, n, k = map(int, input().split())
    bachu_list = [[0 for i in range(m)] for i in range(n)]  # m*n
    visit_list = [[0 for i in range(m)] for i in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        bachu_list[y][x] = 1
    visit = 0
    for y in range(n):
        for x in range(m):
            if visit_list[y][x] == 0 and bachu_list[y][x] == 1:
                visiting(x, y)
                visit += 1

    print(visit)
