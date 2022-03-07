# 맞았는데 왜 k==n 이면 걍 maxi 출력하기가 안되는거지 ?? 
import sys

input=sys.stdin.readline
k,n=map(int,input().split())
lineList=[int(input()) for i in range(k)]
mini=1
maxi=max(lineList)
while mini<=maxi:
    pv=(mini+maxi)//2
    num=0
    for value in lineList:
        num+=value//pv
    if num>=n:
        mini=pv+1
    else:
        maxi=pv-1
print(maxi)




