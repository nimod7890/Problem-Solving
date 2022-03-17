'''
답을 보기 이전의 머리로 돌아갈 수 없는 나 
'''
from collections import deque
import sys


def bfs(start):
    num = [0] * n
    visit = [0] * n
    will_visit = deque()
    will_visit.append(start)
    while will_visit:
        node = will_visit.popleft()
        for child in relation[node]:
            if visit[child] == 1:
                continue
            num[child] = num[node]+1
            visit[child] = 1
            will_visit.append(child)
    return sum(num)


input = sys.stdin.readline
n, m = map(int, input().split())
relation = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    relation[a-1].append(b-1)
    relation[b-1].append(a-1)

result = -1
for i in range(n):
    num = bfs(i)
    if result == -1 or num < result:
        result = num
        ans = i
print(ans+1)
