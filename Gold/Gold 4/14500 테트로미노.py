import sys
input=sys.stdin.readline

arrays=[
  [[0,0],[0,1],[1,0],[1,-1]],
  [[0,0],[0,1],[1,0],[1,1]],
  [[0,0],[0,1],[1,1],[1,2]],
  [[0,0],[1,0],[1,1],[2,1]],
  [[0,0],[1,0],[1,-1],[2,-1]]
  ]

array1=[[0,0],[1,0],[2,0]]
array2=[[0,0],[0,1],[0,2]]
array1_dot=[[0,-1],[1,-1],[2,-1],[3,0],[0,1],[1,1],[2,1]]

for dot in array1_dot:
  new_array1 = array1[:] + [dot]  
  new_array2 = array2[:] + [dot[::-1]] 
  arrays.extend([new_array1, new_array2]) 


n,m=map(int,input().split())
paper=[list(map(int,input().split())) for _ in range(n)]

ans=0
for i in range(n):
  for j in range(m):
    for array in arrays:
      tmp=0 
      for Y,X in array:
        y,x=i+Y,j+X
        if not (0<=y<n and 0<=x<m):
          break
        tmp+=paper[y][x]
      else:
        if tmp>ans:
          ans=tmp 

print(ans)