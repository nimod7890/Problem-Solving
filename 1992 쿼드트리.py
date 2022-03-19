import sys

input = sys.stdin.readline
sys.setrecursionlimit(10*6)


def check(num, x, y):
    if num == 1:
        return arr[y][x]
    box = []
    for x_i, y_i in [[x, y], [x+num//2, y], [x, y+num//2],  [x+num//2, y+num//2]]:
        box.append(check(num//2, x_i, y_i))
    piece = "".join(box)
    if len(set(box)) == 1:
        if piece == "1111":
            return "1"
        elif piece == "0000":
            return "0"
    return "("+piece+")"


n = int(input())
arr = []
for i in range(n):
    arr.append(list(input()))
print(check(n, 0, 0))
