import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

# 시간 초과 남 ~ 나중에 ㄷ시 공부할랭

# def fly(x,num,l):
#     global min
#     if x==y:
#         if 1 not in l: return
#         min=num if num<min or min==-1 else min
#         return
#     if x>y: return
#     for go in l:
#         if go<1 or go>y-x: continue
#         fly(x+go,num+1,[go+1,go,go-1])
    
# N=int(input())

# for i in range(N):
#     x,y=map(int,input().split())
#     y-=(x+1)
#     min=-1
#     fly(0,0,[1,0,-1])
#     print(min+1)
