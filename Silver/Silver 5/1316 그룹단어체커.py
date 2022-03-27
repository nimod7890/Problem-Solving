##비효율적이라 생각했는데 다른 사람들꺼 보니까 내 코드도 나쁘지 않을지도? 

n=int(input())
l=["" for i in range(n)]

num=0
for v in l:
    v=input()
    for s in v:
        i=v.index(s)
        c=v.count(s)
        if v[i:i+c]!=s*c:
            num+=1
            break
print(n-num)