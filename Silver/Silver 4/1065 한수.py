n = int(input())
cnt = n if n < 100 else 99
if n >= 100:
    for n in range(100, n+1):
        nlist = list(map(int, str(n)))
        d = nlist[1]-nlist[0]
        tmp = nlist[1]
        for i, num in enumerate(nlist[2:], 2):
            if num-tmp == d:
                tmp = num
            else:
                break
        else:
            cnt += 1
print(cnt)
