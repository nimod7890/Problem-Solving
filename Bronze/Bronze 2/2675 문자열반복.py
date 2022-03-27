##l을 처음에 list로 만들어서 헤맷슴 조곰 베낌 ㅎ

n=int(input())

for i in range(n):
    l=""
    num, string=input().split()
    for j in string:
        l+=j*int(num)
    print("".join(l))