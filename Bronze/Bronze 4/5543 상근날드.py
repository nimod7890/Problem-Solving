import sys

input=sys.stdin.readline
print(min([int(input()) for i in range(3)])+min([int(input()) for i in range(2)])-50)