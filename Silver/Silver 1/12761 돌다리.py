from collections import defaultdict, deque


a, b, n, m = map(int, input().split())
will = deque([n])
visit = defaultdict(int)
visit[n]=1
while will:
    x = will.popleft()
    if x==m:
        print(visit[m]-1)
        break
    for new in [x*a,x*b,x-a,x+a,x-b,x+b,x-1,x+1]:
        if 0<=new<=10**5 and visit[new]==0:
            will.append(new)
            visit[new]=visit[x]+1
            