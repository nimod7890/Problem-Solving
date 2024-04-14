from collections import deque
import sys
input=sys.stdin.readline


def backtracking(count:int,curr:int)->None:
  global visited_city,ans
  
  if count==m:
    ans=min(sum(min(abs(house[0]-city[0])+abs(house[1]-city[1]) for city in visited_city) for house in houses),ans)
    return 

  for i in range(curr,city_count):
    if cities[i] in visited_city:
      continue
    
    visited_city.append(cities[i])
    backtracking(count+1,i+1)
    visited_city.pop()
    
n,m=map(int,input().split())
graph=[[*map(int,input().split())] for _ in range(n)]
visited_city=deque()
houses,cities=[],[]
ans=sys.maxsize

for i in range(n):
  for j in range(n):
    if graph[i][j]==2:
      cities.append((i,j))
    if graph[i][j]==1:
      houses.append((i,j))

city_count=len(cities)

backtracking(0,0)
print(ans)