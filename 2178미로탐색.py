#거의 베꼈음 난 멍청해 ㅜ 

n,m=map(int,input().split())
miro=[]
visit=[[0 for i in range(m)] for i in range(n)]
print(visit)
will_visit=[]
for i in range(n):
    miro.append(list(input()))


dx=[1,-1,0,0]
dy=[0,0,-1,1]

will_visit.append([0,0])
visit[0][0]=1

while will_visit:
    i,j=will_visit.pop(0)
    for idx in range(4):
        x=i+dx[idx]
        y=j+dy[idx]
        if 0<=x<n and 0<=y<m:
            if visit[x][y]==0:
                print("visit",x,y)
                will_visit.append([x,y])
                visit[x][y]=1+visit[i][j]

print(visit[n-1][m-1])



