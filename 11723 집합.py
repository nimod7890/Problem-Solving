import sys


input = sys.stdin.readline

m = int(input())
S = set()
for i in range(m):
    do = input().split()
    if do[0] == "all":
        S = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
             '12', '13', '14', '15', '16', '17', '18', '19', '20'}
    if do[0] == "empty":
        S = set()
    if do[0] == "add":
        S.add(do[1])
    if do[0] == "remove":
        S.discard(do[1])
    if do[0] == "check":
        if do[1] in S:
            print(1)
        else:
            print(0)
    if do[0] == "toggle":
        if do[1] in S:
            S.remove(do[1])
        else:
            S.add(do[1])
