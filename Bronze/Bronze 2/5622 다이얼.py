string=list(input())
l=list('3334445556667778888999',)
l.extend(list('10 10 10 10'.split()))
sum=0
for i in string:
    sum+=(int(l[ord(i)-ord('A')]))
print(sum)