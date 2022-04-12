n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    graph = [0]*n
    graph[0] = 1
    graph[1] = 2
    for i in range(2, n):
        graph[i] = (graph[i-1]+graph[i-2]) % 15746
    print(graph[n-1])
