'''
문제
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 
이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 
칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 
다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 
각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 
항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

4 6
101111
101010
101011
111011

15

풀이: 최소 어쩌구라 bfs
헷갈린 부분: 아래에서 1일때 무조건 min 값 안따져도 되는 거에서 헤맴 
if 0<=I<N and 0<=J<M and graph[I][J]==1:
  graph[I][J]=1+graph[i][j]
  
'''
from collections import deque
import sys


input=sys.stdin.readline

N,M=map(int,input().split())
graph=[list(map(int,input().strip())) for _ in range(N)]

will=deque([[0,0]])
while will:
  i,j=will.popleft()
  for a,b in [[0,-1],[-1,0],[1,0],[0,1]]:
    I,J=a+i,b+j
    if 0<=I<N and 0<=J<M and graph[I][J]==1:
      graph[I][J]=1+graph[i][j]
      will.append([I,J])

print(graph[N-1][M-1])
