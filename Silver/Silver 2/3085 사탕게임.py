import sys
import itertools
input=sys.stdin.readline


def getMax():
  global maxi

  for i in range(n):
    num=[1,1]
    for j in range(n-1):
      stay,add=i,j+1
      if 0<=add<n:
        # check column
        if colors[add][stay]==colors[j][i]:
          num[0]+=1
          if num[0] >maxi:
            maxi=num[0]
        else:
          num[0]=1
        # check row
        if colors[stay][add]==colors[i][j]:
          num[1]+=1
          if num[1]>maxi:
            maxi=num[1]
        else:
          num[1]=1
          
n=int(input())
colors=[list(input().rstrip()) for _ in range(n)]

maxi=0
for (x,y) in list(itertools.permutations(range(n),2)):
  for (_i,_j) in [[0,1],[1,0]]:
    i,j=x+_i,y+_j
    if 0<=i<n and 0<=j<n and colors[x][y]!=colors[i][j]:
      colors[x][y],colors[i][j]=colors[i][j],colors[x][y]
      getMax()
      colors[x][y],colors[i][j]=colors[i][j],colors[x][y]
      
print(maxi)
