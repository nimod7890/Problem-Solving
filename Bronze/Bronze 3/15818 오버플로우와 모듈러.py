n,m=map(int,input().split())
ans=1 
for num in map(int,input().split()):
    num%=m
    ans=num*ans%m
print(ans)