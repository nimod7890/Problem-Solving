'''
입력
첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다. 
M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 
단, 2 ≤ M,N ≤ 1,000 이다. 둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다. 
즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다. 
하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다. 
정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.

토마토가 하나 이상 있는 경우만 입력으로 주어진다.

출력
여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 
만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 
토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.

6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

8

6 4
0 -1 0 0 0 0
-1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

-1
'''
from collections import deque
import sys
input=sys.stdin.readline
nearby=[[0,1],[1,0],[-1,0],[0,-1]]

# input
M,N=map(int,input().split())
box=[list(map(int,input().split())) for _ in range(N)]

# process
next_step=deque()
for n in range(N):
  for m in range(M):
    if box[n][m]==1:
      next_step.append([m,n])


while next_step:
  x,y=next_step.popleft()
  for X,Y in nearby:
    m,n=x+X,y+Y
    if 0<=m<M and 0<=n<N and box[n][m]==0:
      box[n][m]=box[y][x]+1
      next_step.append([m,n])
        
# output
min_date=0
for row in box:
  if 0 in row:
    print(-1)
    break
  min_date=max(min_date,max(row))
else:
  print(min_date-1)