from collections import deque


t = int(input())
for i in range(t):
    p_list = input()
    len_p = len(p_list)
    n = int(input())  # len_n
    LIST = input()[1:-1].split(',')
    n_list = deque(x
                   for x in LIST) if n != 0 else deque()
    i = 0
    start = 0
    while i < len_p:
        if p_list[i] == 'R':
            if start == 0:
                start = 1
            else:
                start = 0
        elif p_list[i] == 'D':
            if n == 0:
                print("error")
                break
            if start == 0:
                n_list.popleft()
            else:
                n_list.pop()
            n -= 1
        i += 1
    else:
        if start == 1:
            n_list.reverse()
        print("[", end='')
        print(",".join(n_list), end='')
        print("]")
