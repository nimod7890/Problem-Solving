for i in range(int(input())):
    num, ans = 0, 0
    for ox in list(input()):
        if ox == 'O':
            num += 1
            ans += num
        else:
            num = 0
    print(ans)
