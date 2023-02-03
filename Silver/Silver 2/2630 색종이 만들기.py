import sys
input=sys.stdin.readline
n=int(input())
nlist=[list(map(int,input().split())) for i in range(n)]
cnt=[0,0]

def divide(i,j,num):
    it=nlist[i][j]
    for x in range(i,i+num):
        for y in range(j,j+num):
            if it !=nlist[x][y]:
                num//=2
                divide(i,j,num)            
                divide(i,j+num,num)            
                divide(i+num,j,num)            
                divide(i+num,j+num,num)
                return
    cnt[it]+=1
                
divide(0,0,n)
print(*cnt,sep="\n")