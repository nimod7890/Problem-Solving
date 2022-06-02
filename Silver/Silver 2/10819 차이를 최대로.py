from itertools import permutations

n = int(input())
maxi = 0
for L in permutations(list(map(int, input().split()))):
    tmp = 0
    for i in range(1, n):
        tmp += abs(L[i-1]-L[i])
    maxi = tmp if maxi < tmp else maxi
print(maxi)
