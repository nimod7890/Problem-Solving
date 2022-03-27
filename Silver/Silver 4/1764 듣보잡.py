# set 교집합 구글링함 ㅋㅋ

n,m=map(int,input().split())
dlist=[input() for i in range(n)]
blist=[input() for i in range(m)]
anslist=sorted(list(set(dlist)& set(blist))) 
print(len(anslist))
print("\n".join(anslist))