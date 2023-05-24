'''4퍼에서 틀림
'''
from collections import defaultdict, deque

relation=defaultdict(list)
time=[0]
n=int(input())
queue=deque()
count=[0]*(n+1)
for i in range(n):
    tmp=list(map(int,input().split()))
    time.append(tmp[0])
    if tmp[1]>0:
        for v in tmp[2:]:
            relation[v].append(i+1)
    else:
        queue.append(i+1)
        count[i+1]=tmp[0]
while queue:
    node=queue.popleft()
    for v in relation[node]:
        count[v]=max(count[v],count[node]+time[v])
        queue.append(v)
    print(count)
print(max(count))        

'''
7
5 0
1 1 1
3 1 2
6 1 1
1 2 2 4
8 2 2 4
4 3 3 5 6

(23)
4
10 0
6 1 1
7 1 1
5 1 2

(21)

7
5 0
3 0
6 0
1 0
8 0
4 0
2 0
(8)

4
10 0
6 1 1
7 1 1
5 1 2
(21)
'''