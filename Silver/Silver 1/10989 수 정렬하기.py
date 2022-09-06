import sys

input=sys.stdin.readline
nlist=[0]*10001
for i in range(int(input())):
    nlist[int(input())]+=1
for i in range(10001):
    for j in range(nlist[i]):
        print(i)