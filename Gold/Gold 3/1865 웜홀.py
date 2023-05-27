'''
inf + 음수 = inf 여서 inf 쓰면 안됨
시작점 정해진 문제 아니라 weightArr inf인 경우도 계산
'''
import sys
input=sys.stdin.readline
INF=10001

def bellmanFord():
    weightArr=[INF]*(n+1)
    weightArr[1]=0
    for i in range(n):
        for start,end,weight in graph:
            if weightArr[end]>weightArr[start]+weight:
                if i==n-1:
                    print('YES')
                    return 
                weightArr[end]=weightArr[start]+weight
    print('NO')
    return

for _ in range(int(input())):
    n,m,w=map(int,input().split())
    graph=[]
    for _ in range(m):
        s,e,t=map(int,input().split())
        graph.extend([[s,e,t],[e,s,t]])
    for _ in range(w):
        s,e,t=map(int,input().split())
        graph.append([s,e,-t])
    bellmanFord()