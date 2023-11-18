'''
재난방재청에서는 많은 비가 내리는 장마철에 대비해서 다음과 같은 일을 계획하고 있다. 먼저 어떤 지역의 높이 정보를 파악한다. 그 다음에 그 지역에 많은 비가 내렸을 때 물에 잠기지 않는 안전한 영역이 최대로 몇 개가 만들어 지는 지를 조사하려고 한다. 이때, 문제를 간단하게 하기 위하여, 장마철에 내리는 비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠긴다고 가정한다.
물에 잠기지 않는 안전한 영역이라 함은 물에 잠기지 않는 지점들이 위, 아래, 오른쪽 혹은 왼쪽으로 인접해 있으며 그 크기가 최대인 영역을 말한다. 
(꼭짓점으로만 붙어 있는 두 지점은 인접하지 않는다고 취급한다).
이와 같이 장마철에 내리는 비의 양에 따라서 물에 잠기지 않는 안전한 영역의 개수는 다르게 된다. 
위의 예와 같은 지역에서 내리는 비의 양에 따른 모든 경우를 다 조사해 보면 물에 잠기지 않는 안전한 영역의 개수 중에서 최대인 경우는 5임을 알 수 있다.
어떤 지역의 높이 정보가 주어졌을 때, 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 계산하는 프로그램을 작성하시오.

입력
첫째 줄에는 어떤 지역을 나타내는 2차원 배열의 행과 열의 개수를 나타내는 수 N이 입력된다. 
N은 2 이상 100 이하의 정수이다. 
둘째 줄부터 N개의 각 줄에는 2차원 배열의 첫 번째 행부터 N번째 행까지 순서대로 한 행씩 높이 정보가 입력된다. 
각 줄에는 각 행의 첫 번째 열부터 N번째 열까지 N개의 높이 정보를 나타내는 자연수가 빈 칸을 사이에 두고 입력된다. 
높이는 1이상 100 이하의 정수이다.

출력
첫째 줄에 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 출력한다.

5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7

5
'''
from collections import deque
from itertools import product
import sys

input=sys.stdin.readline

def getSaftyArea(area:list):
  localMax=0
  for i,j in dlist:
    if area[i][j]<=minLimitNum:
      continue
    area[i][j]=minLimitNum
    will=deque([[i,j]])
    while will:
      a,b=will.pop()
      for dy,dx in [[-1,0],[0,-1],[1,0],[0,1]]:
        A,B=dy+a,dx+b  
        if 0<=A<n and 0<=B<n and area[A][B]>minLimitNum:
          will.append([A,B])
          area[A][B]=minLimitNum
    localMax+=1
  return localMax

n=int(input())
precipitation=[]


for _ in range(n):
  tmp=list(map(int,input().split()))
  precipitation.append(tmp)

dlist=list(product(range(n),repeat=2))
globalMax=0
maxLimitNum=100
minLimitNum=0

while minLimitNum<maxLimitNum:
  globalMax=max(globalMax,getSaftyArea([row[:] for row in precipitation]))
  minLimitNum+=1
  
print(globalMax)
