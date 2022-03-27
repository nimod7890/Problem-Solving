from collections import defaultdict

n=int(input())
m=int(input())
d=defaultdict(list)
for i in range(m):
    a,b=input().split()
    d[a].append(b) #d[a]+=b로 하면 100 이 1,0,0으로 들어감 
    d[b].append(a)
visit_n=0
visit=[]
will_visit=['1']
if len(d['1'])==0:
    print(0)
else:
    while will_visit:
        v=will_visit.pop(0)
        if v in visit: 
            continue
        visit.append(v)
        visit_n+=1
        will_visit.extend(d[v])
    print(visit_n-1)