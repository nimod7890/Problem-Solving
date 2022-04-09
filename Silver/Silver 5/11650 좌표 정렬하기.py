n = int(input())
nlist = []
for i in range(n):
    a, b = map(int, input().split())
    nlist.append([a, b])
nlist.sort(key=lambda x: [x[0], x[1]])
for a, b in nlist:
    print(f"{a} {b}")
