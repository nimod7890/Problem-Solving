'''
Floyd-Warshall ㅋㅋ 메모리 초과!
'''

from math import inf
import sys


input=sys.stdin.readline
V,E=map(int,input().split())
K=int(input())-1
weight=[[inf]*V for _ in range(V)]
for i in range(E):
    u,v,w=map(int,input().split())
    weight[u-1][v-1]=w
for k in range(V):
    for i in range(V):
        for j in range(V):
            if i==j:
                weight[i][j]=0
            else:
                weight[i][j]=min(weight[i][k]+weight[k][j],weight[i][j])
print(*weight[K],sep='\n')