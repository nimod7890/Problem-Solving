#못풀었음 ^^! 나중에 다 시

# 
from math import factorial

n,m,k=map(int,input().split())
i=(factorial(n-m)/(factorial(n-2*m+k)*factorial(m-k)))
l=(factorial(m)/(factorial(m-k)*factorial(k)))
j=(factorial(n)/(factorial(n-m)*factorial(m)))
print((l*i/j))

'''

지민이가 못 뽑을 가짓수 : 
nCm개를 뽑았는데, 그 중에 

mCk   *   (n-m)C(m-k) / nCm
그 사람들이 1/nCm 이면
'''