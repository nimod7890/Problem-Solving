import sys

input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(input().strip()) for i in range(n)]
chess1 = [
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
]
chess2 = [
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
]


def chess(compare, I, J):
    repaint = 0
    for i in range(I, I + 8):
        for j in range(J, J + 8):
            if compare[i - I][j - J] != board[i][j]:
                repaint += 1
    return repaint


minimum = 64
for i in range(n - 7):
    for j in range(m - 7):
        minimum = min(chess(chess1, i, j), chess(chess2, i, j), minimum)
print(minimum)
