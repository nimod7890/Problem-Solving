#이분탐색 재귀함수로 하지 말 자 ..... ㅜ ㅜ 

import sys
input=sys.stdin.readline
n,m=map(int,input().split())
treeList=list(map(int,input().split())) 
minHeight=1
maxHeight=max(treeList)
while minHeight<=maxHeight:
    cnt=0
    pivot=(minHeight+maxHeight)//2
    for value in treeList:
        if value>=pivot:
            cnt+=value-pivot
    if cnt>=m:
        minHeight=pivot+1
    else:
        maxHeight=pivot-1
print(maxHeight)