n=int(input())
nlist=[list(map(int,input().split())) for i in range(n)]
ilist=[[0,0],[0,1],[1,0],[1,1]]

while n!=1:
    nlist=[[sorted([nlist[i+k][j+l] for k,l in ilist])[2] for j in range(0,n-1,2)] for i in range(0,n-1,2)]
    n//=2
    
print(nlist[0][0])