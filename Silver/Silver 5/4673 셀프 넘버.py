nlist = set(range(1, 10001))
tmp = set()

for x in nlist:
    for X in str(x):
        x += int(X)
    if x <= 10000:
        tmp.add(x)


print("\n".join(map(str, sorted(list(nlist-tmp)))))
