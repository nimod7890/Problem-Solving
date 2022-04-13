from collections import defaultdict
n = int(input())
f = defaultdict(int)
f[0] = 0
f[1] = 1
if n == 0:
    print(0)
elif n > 0:
    print(1)
    for i in range(2, n+1):
        f[i] = (f[i-1]+f[i-2]) % 1000000000
else:
    for i in range(1, n+1, -1):
        if f[i]-f[i-1] >= 0:
            f[i-2] = (f[i]-f[i-1]) % 1000000000
        else:
            f[i-2] = -((f[i-1]-f[i]) % 1000000000)
    print(1) if f[n] > 0 else print(-1) if f[n] < 0 else print(0)
print(abs(f[n]) % 1000000000)
