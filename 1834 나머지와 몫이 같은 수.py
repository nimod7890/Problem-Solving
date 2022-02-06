n=int(input())
ans=[x*n+x for x in list(range(1,n))]
print(sum(ans))