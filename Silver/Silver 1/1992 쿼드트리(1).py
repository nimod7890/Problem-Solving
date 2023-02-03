import sys
input=sys.stdin.readline
n=int(input())
nlist=[list(input()) for i in range(n)]
def divide(i,j,num):
    it=nlist[i][j]
    for x in range(i,i+num):
        for y in range(j,j+num):
            if it !=nlist[x][y]:
                num//=2
                return "("+divide(i,j,num)+divide(i,j+num,num)+divide(i+num,j,num)+divide(i+num,j+num,num)+")"
    return it
print(divide(0,0,n))