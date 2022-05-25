n = int(input())
nlist = []
for i in range(n):
    a, b = map(int, input().split())
    nlist.append([a, b, 1, i])
nlist.sort(key=lambda x: (x[0], x[1]))
for idx in range(n):
    weight, height, _, _ = nlist[idx]
    for i in range(idx):
        w, h, _, _ = nlist[i]
        if w < weight and h < height:
            nlist[i][2] += 1

nlist.sort(key=lambda x: x[3])
for w, h, rank, idx in nlist:
    print(rank, end=' ')
