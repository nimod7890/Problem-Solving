###코드가 좀 거지같긴 한데 암튼 하긴 함

from collections import defaultdict
arr=defaultdict(list)
arr[0]=[i+1 for i in range(14)]
N=int(input())
    
for i in range(N):
    k=int(input())
    n=int(input())
    if len(arr[k])==0:
        for j in range(k):
            arr[j+1]=[sum(arr[j][:a+1]) for a in range(14)]
    print(arr[k][n-1])