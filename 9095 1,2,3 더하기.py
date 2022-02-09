# 규칙 있는거 같은데 뭔지 몰라서 점화식 베껴옴
def plus123(n):
    return 1 if n==1 else 2 if n==2 else 4 if n==3 else plus123(n-1)+plus123(n-2)+plus123(n-3)
for i in range(int(input())):
    print(plus123(int(input())))