import sys

input=sys.stdin.readline
n,m=map(int,input().split())
dic={}
for i in range(n):
    site,pw=map(str,input().split())
    dic[site]=pw
for  i in range(m):
    print(dic[input().rstrip()])