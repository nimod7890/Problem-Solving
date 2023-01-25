'''
2^n만보다 큰지 확인 
r<2^(n-1) -> ans<2^(n-1) 
    else +2^(n-1)
c<2^(n-1) -> ans<2^(n-2)
    else +2^(n-2)
'''

n,r,c=map(int,input().split())
nlist=[[0,1],[2,3]]
ans=0

def check(num,row,column):
    global ans
    if row<2 and column<2:
        ans+=nlist[row][column]
        return 
    if row>=num:
        ans+=num**2*2
        row-=num
    if column>=num:
        ans+=num**2
        column-=num
    check(num//2,row,column)
    
check(2**(n-1),r,c)
print(ans)