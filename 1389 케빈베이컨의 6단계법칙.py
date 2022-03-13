'''
시간초과남 
나중에 
할 거 임
'''


from collections import defaultdict
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
relation = defaultdict(set)
for i in range(m):
    a, b = map(int, input().split())
    relation[a-1].add(b-1)
    relation[b-1].add(a-1)
num = [[0 for i in range(n)] for i in range(n)]


def find(start, end, visit_n):
    global num
    if start == end:
        if num[sIdx][eIdx] == 0:
            num[sIdx][eIdx] = visit_n
        else:
            num[sIdx][eIdx] = visit_n if visit_n <= num[sIdx][eIdx] else num[sIdx][eIdx]
        return
    if visited[start] == 1:
        return
    visited[start] = 1
    for x in relation[start]:
        find(x, end, visit_n+1)
    visited[start] = 0


minimum, ans = 0, []

for sIdx in range(n):  # 01234
    for eIdx in range(sIdx+1, n):  # 1234
        visited = [0 for i in range(n)]
        find(sIdx, eIdx, 0)
        num[eIdx][sIdx] = num[sIdx][eIdx]
    summ = sum(num[sIdx])
    if ans == -1:
        minimum = summ
        ans.append(sIdx)
    elif summ <= minimum:
        ans.append(sIdx)

print(min(ans)+1)
