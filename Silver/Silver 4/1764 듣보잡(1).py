n,m=map(int,input().split())
nlist=[input() for i in range(n)]
mlist=[input() for i in range(m)]
dic=sorted(list(set(nlist) & set(mlist)))
print(len(dic))
print("\n".join(dic))