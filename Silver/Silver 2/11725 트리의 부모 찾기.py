from collections import defaultdict, deque

tree=defaultdict(list)
n=int(input())
result=[0]*(n+1)
will=deque([1])

for i in range(n-1):
    a,b=map(int,input().split())
    tree[a]+=[b]
    tree[b]+=[a]
    
while will:
    node=will.popleft()
    for v in tree[node]:
        if result[v]==0:
            result[v]=node
            will.append(v)
print(*(result[2:]),sep=' ')
print(" ".join(map(str,result[2:])))