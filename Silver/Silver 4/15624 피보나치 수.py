# test case 201개 중에 97개만 맞아서 답 찾아봤는데 이렇게 쉽게 풀리는 거였다니 .. 

# import sys
# sys.setrecursionlimit(10**6)
# input=sys.stdin.readline
# cnt=0
# flist=[]
# def f(n):
#     if n==0:
#         flist.append(0)
#         return 0
#     elif n<len(flist):
#         return flist[n]
#     elif n==1:
#         flist.append(1)
#         return 1
#     flist.append((f(n-2)+f(n-1))%1000000007)
#     return flist[n]
# print(f(int(input())))

n = int(input())
a, b = 0, 1
for i in range(n):
    a, b = (a+b)%1000000007, a%1000000007
print(a)