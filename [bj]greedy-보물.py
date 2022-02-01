#내가 풀었슴

N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
A.sort()
B.sort(reverse=True)

print(sum(list(map(lambda x,y:x*y,A,B))))