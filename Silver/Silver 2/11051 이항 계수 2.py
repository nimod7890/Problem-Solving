from math import factorial


n,k=map(int,input().split())
print((factorial(n)//(factorial(n-k) * factorial(k))) % 10007)