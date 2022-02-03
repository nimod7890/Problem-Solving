from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n,m=map(int,input().split())
d=defaultdict(list)
if m==0: 
    print(n)
    exit(1)

for i in range(m):
    a,b=map(int,input().split())
    d[a]+=[b]
    d[b]+=[a]

iter_visit=[x for x in d.keys()]
num=0
while iter_visit:
    visit=[]
    will_visit=[iter_visit[0]]
    while will_visit:
        v=will_visit.pop(0)
        if v in visit: 
            continue
        visit.append(v)
        for w in d[v]:
            will_visit.append(w)
    iter_visit=list(set(iter_visit)-set(visit))
    num+=1
print(num)