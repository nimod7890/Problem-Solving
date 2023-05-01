n,k=map(int,input().split())
stack=[i+1 for i in range(n)]
curr=0
ans=[]
while len(stack)!=0:
    ans.append(stack.pop(curr:=(k-1+curr)%len(stack)))
print("<"+", ".join(map(str,ans))+">")