from collections import defaultdict

n,m,v=map(int, input().split())
d=defaultdict(list)
will_visit=[]
visited=[]
for i in range(m):
    A,B=map(int, input().split())
    d[A]+=[B]
    d[B]+=[A]

def dfs(v):
    if v in visited: #len=0 일때도 수행되어야 함. 
        return 
    visited.append(v)
    d[v].sort()
    for value in d[v]:
        dfs(value)

def bfs(v):
    will_visit.append(v)
    while will_visit:
        visiting=will_visit.pop(0)
        if visiting not in visited:
            visited.append(visiting)
            will_visit.extend(d[visiting])


dfs(v)
print(" ".join(str(i) for i in visited))
visited=[]
bfs(v)
print(" ".join(str(i) for i in visited))







'''



1 2 4 3
1 2 3 4



5 5 3
5 4
5 2
1 2
3 4
3 1

3 1 2 5 4
3 1 4 2 5



1000 1 1000
999 1000

1000 999
1000 999
'''