n = int(input())

for N in range(1, n + 1):
    hap = N + sum(map(int, str(N)))
    if n == hap:
        print(N)
        break
else:
    print(0)
