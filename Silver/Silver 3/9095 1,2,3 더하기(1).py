import sys

input=sys.stdin.readline
hap=[1,2,4]
for _ in range(int(input())):
    num=int(input())
    for i in range(len(hap),num):
        hap.append(sum(hap[-3:]))
    print(hap[num-1])