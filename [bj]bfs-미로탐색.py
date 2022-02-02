n,m=map(int,input().split())
miro=[]
visit=[]
will_visit=[]
for i in range(n):
    miro[i]=list(input())

#여기부턴 베꼈음 ㅜ 난멍청해

dx=[1,-1,0,0]
dy=[0,0,-1,1]

will_visit.append([0,0])
visit[0][0]=1

while will_visit:
    i,j=will_visit.pop(0)
    for idx in range(4):
        x=i+dx[idx]
        y=j+dy[idx]
        if 0<=x<n and 0<=y<m and visit[x][y]==1:
            will_visit.append([x,y])
            visit[x][y]+=1
print(visit[n-1][m-1])



