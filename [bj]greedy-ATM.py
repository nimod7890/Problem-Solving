n=int(input())
a=list(map(int,input().split()))
a.sort()
print(sum(list(map(lambda idx:sum(a[:idx[0]+1]),enumerate(a)))))

'''
5
3 1 4 3 2
'''
