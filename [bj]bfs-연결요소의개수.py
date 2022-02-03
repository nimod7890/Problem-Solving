#아예 뜯어고침 == 베꼈다는 뜻 


from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n,m=map(int,input().split())
d=defaultdict(list)


for i in range(m):
    a,b=map(int,input().split())
    d[a]+=[b]
    d[b]+=[a]
    
num=0
visit=[]
def bfs(v):
    if v in visit: return 
    visit.append(v)
    for w in d[v]:
        bfs(w)

for v in d.keys():
    if v not in visit:
        bfs(v)
        num+=1
print(num+n-len(visit))