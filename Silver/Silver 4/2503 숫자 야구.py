import sys

input = sys.stdin.readline
nlist = []
for i in range(int(input())):
    tmp = list(map(int, input().split()))
    nlist.append([list(str(tmp[0])), tmp[1], tmp[2]])
ans = 0


def check(i, j, k):
    for num, strike, ball in nlist:
        n_strike = 0
        n_ball = 0
        if i == num[0]:
            n_strike += 1
        if j == num[1]:
            n_strike += 1
        if k == num[2]:
            n_strike += 1
        if strike != n_strike:
            return 0
        if i == num[1] or i == num[2]:
            n_ball += 1
        if j == num[0] or j == num[2]:
            n_ball += 1
        if k == num[0] or k == num[1]:
            n_ball += 1
        if ball != n_ball:
            return 0
    return 1


for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or i == k or j == k:
                continue
            ans += check(str(i), str(j), str(k))
print(ans)
