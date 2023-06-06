import heapq
import sys

def fox():
    p=[sys.maxsize]*(n+1)
    p[1]=0
    q=[[0,1]]
    while q:
        sw,s=heapq.heappop(q)
        if p[s]<sw: continue
        for e,ew in g[s]:
            w=sw+ew
            if p[e]<=w:continue
            p[e]=w
            heapq.heappush(q,[w,e])
    return p

def wolf():
    p=[[sys.maxsize]*(n+1) for _ in range(2)]
    p[1][1]=0
    q=[[0,1,0]]
    while q:
        sw,s,sp=heapq.heappop(q)
        if p[sp^1][s]<sw:continue
        for e,ew in g[s]:
            w=sw+(ew*2 if sp else ew//2)
            if p[sp][e]<=w: continue
            p[sp][e]=w
            heapq.heappush(q,[w,e,sp^1])
    return p

input=sys.stdin.readline
n,m=map(int,input().split())
g=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,d=map(int,input().split())
    g[a].append((b,d*2))
    g[b].append((a,d*2))
    
p1=fox()
p2=wolf()

a=0
for i in range(1,n+1):
    if p1[i]<min(p2[0][i],p2[1][i]):
        a+=1
print(a)