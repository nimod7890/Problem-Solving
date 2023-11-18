'''
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.
(1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다.
(1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.

6 5
1 2
2 5
5 1
3 4
4 6

2
'''
from collections import defaultdict, deque
import sys
input=sys.stdin.readline

n,m=map(int,input().split())

graph=defaultdict(list)
for _ in range(m):
  u,v=  map(int,input().split())
  graph[u]+=[v]
  graph[v]+=[u]

cnt=0
visited=[False]*(n+1)
for i in range(1,n+1):
  if visited[i]:continue
  will=deque([i])
  visited[i]=True
  while will:
    start=will.pop()
    for end in graph[start]:
      if visited[end]:continue
      visited[end]=True
      will.append(end)
  cnt+=1
print(cnt)