# 오키 시간초과 ~ 시ㅣ 발 ㅋㅋ
# 에라토스테네스의 방법을 사용해야함 !!@!
'''
m,n=map(int,input().split())
num=2
prime=[]
for num in range(2,n+1):
    for v in prime:
        if num%v==0: break
    else:
        if num>=m: print(num)
        prime.append(num)
'''

m,n=map(int,input().split())
primeList=[True for i in range(n-1)]
primeList.insert(0,False)
for i in range(1,n+1):
    if primeList[i-1]==False:continue
    for idx in range(2,n):
        if i*idx-1>=n:
            break
        primeList[i*idx-1]=False
for idx,value in enumerate(primeList):
    if idx>=m-1 and value==True: print(idx+1)
