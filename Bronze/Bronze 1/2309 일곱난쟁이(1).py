import sys
input=sys.stdin.readline
nlist=[int(input()) for _ in range(9)]

for i in range(9):
  for j in range(9):
    temp=[]
    if i!=j:
      for k in range(9):
        if i!=k and k!=j:
          temp.append(nlist[k])
      if sum(temp)==100:
        print(*sorted(temp),sep='\n')
        exit()