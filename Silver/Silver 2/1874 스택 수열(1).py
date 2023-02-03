from collections import deque
import sys

input=sys.stdin.readline
stack,string,curr=deque(),[],1
for i in range(int(input())):
    get=int(input())
    while curr<=get:
        stack.append(curr)
        string.append('+')
        #string+='+' -> string 을 문자열로 다루면 ㅈㄴ 오래걸림
        curr+=1
    if stack[-1]==get:
        stack.pop()
        string.append("-")
    else:
        print("NO")
        break
else:
    print("\n".join(string))