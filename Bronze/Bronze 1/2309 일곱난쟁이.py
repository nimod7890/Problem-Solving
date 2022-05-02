nlist = sorted(list(int(input()) for i in range(9)))
hap = sum(nlist)
for i in range(9):
    for j in range(9):
        if i == j:
            continue
        if hap-nlist[i]-nlist[j] == 100:
            tmp = nlist[j]
            nlist.pop(i)
            nlist.remove(tmp)
            print("\n".join(map(str, nlist)))
            exit()
