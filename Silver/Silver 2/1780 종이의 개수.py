import sys
input=sys.stdin.readline

n=int(input())
nlist=[list(input().split()) for i in range(n)]
cnt=[0,0,0]

def isSame(numList,num):
    global cnt
    numSet=set()
    for vlist in numList:
        for v in vlist:
            numSet.add(v)
    if len(numSet)==1:
        idx=int(list(numSet)[0])
        cnt[idx+1]+=1
        return 
    newNum=num//3
    for i in range(0,num-newNum+1,newNum):
        newList=numList[i:i+newNum]
        for j in range(0,num-newNum+1,newNum):
            new=[new[j:j+newNum] for new in newList]
            isSame(new,newNum)

isSame(nlist,n)
print("\n".join(map(str,cnt)))