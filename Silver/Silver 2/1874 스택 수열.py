import sys
input=sys.stdin.readline
n=int(input())
stack=[int(input()) for i in range(n)]
end=[0]*n
curr=0
string=""
for get in stack: 
    if get>curr:
        for i in range(curr,get):
            if end[i]==0:
                string+='+'
                end[i]+=1
            curr+=1
    if get<=curr:
        for i in range(get-1,curr):
            if end[i]==1:
                string+='-'
                end[i]-=2
            elif end[i]==-1:
                end[i]-=1
            curr-=1
    if end[curr]!=-1:
        print('NO')
        break
else:
    print("\n".join(string))
        