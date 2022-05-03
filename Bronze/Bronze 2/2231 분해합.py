n = int(input())

for N in range(1, n + 1):
    nList = list(str(N))
    hap = N + sum(map(int, nList))
    if n == hap:
        print(N)
        break
else:
    print(0)
