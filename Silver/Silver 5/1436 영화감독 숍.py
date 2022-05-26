n = int(input())
if n <= 6:
    numList = [666, 1666, 2666, 3666, 4666, 5666]
    print(numList[n-1])
    exit()
num = 6000
cnt = 6
ans = 5666
while cnt != n:
    numList = list(str(num))
    for i in range(len(numList)-2):
        if numList[i:i+3] == ['6', '6', '6']:
            cnt += 1
            ans = num
            break
    num += 1
print(ans)
