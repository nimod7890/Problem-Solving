e, s, m = map(int, input().split())
year, E, S, M = 1, 1, 1, 1

while not (E == e and S == s and M == m):
    E = E % 15+1
    S = S % 28+1
    M = M % 19+1
    year += 1
print(year)
