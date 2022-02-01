#혼자 풀었다!!!!!!!!!!!!!!!!!!!!!!!!!!

N,K=map(int, input().split())
A,n=[],0
for i in range(N):
    A.insert(0,int(input()))
n=0
for i in range(N):
    print(i,K,A[i])
    if K//A[i]>0: 
        n+=(K//A[i])
        K%=A[i]
    if K==0: break
print(n)