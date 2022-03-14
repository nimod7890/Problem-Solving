from math import factorial
n, m = map(int, input().split())
print(int(factorial(n)//(factorial(m)*factorial(n-m))))
