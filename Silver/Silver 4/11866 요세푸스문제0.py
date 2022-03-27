n,k=map(int,input().split())
nlist=[str(i+1) for i in range(n)]
anslist=[]
go=k-1
for i in range(n):
    go%=len(nlist)
    anslist.append(nlist.pop(go))
    go+=k-1
print("<",end="")
print(", ".join(anslist),end="")
print(">")