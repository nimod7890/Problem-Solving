n, x = map(int, input().split())
nlist = list(map(int, input().split()))
ansList = []
for num in nlist:
    if num < x:
        ansList.append(num)
print(" ".join(map(str, ansList)))
