n,k=map(int,input().split())
ans=1
k=min(k,n-k)
for i in range(k):
    ans*=(n-i)//(i+1)
print(ans)    
