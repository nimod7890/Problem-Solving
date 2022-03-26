from collections import defaultdict, deque


def printPath(node):
    cnt = 0
    while path[node] != 0:
        cnt += 1
        node = path[node]
    print(cnt+1)


A, B = map(int, input().split())
will = deque()
will.append(A)
path = defaultdict(int)

while will:
    node = will.popleft()
    if node == B:
        printPath(node)
        break
    for newNode in [node*2, node*10+1]:
        if 1 <= newNode <= B and path[newNode] == 0:
            will.append(newNode)
            path[newNode] = node
else:
    print(-1)
