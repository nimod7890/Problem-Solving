from collections import deque
import sys

input=sys.stdin.readline
nlist=deque()
stack=[]
curr=0
for _ in range(int(input())):
    num=int(input())
    for i in range(curr+1,num+1):
        nlist.append(i)
        stack.append('+')
        curr+=1
    if nlist.pop()==num:
        stack.append('-')
    else:
        print("NO")
        break
else:
    print("\n".join(map(str,stack)))