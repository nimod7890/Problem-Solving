import sys

input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(input().strip()) for i in range(n)]
chessBoard = [
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
]


def chess(I, J):
    repaint = 0
    for i in range(I, I + 8):
        for j in range(J, J + 8):
            if chessBoard[i - I][j - J] != board[i][j]:
                repaint += 1
    return repaint


minimum = 64
for i in range(n - 7):
    for j in range(m - 7):
        original = chess(i, j)
        minimum = min(original, 64 - original, minimum)
print(minimum)
