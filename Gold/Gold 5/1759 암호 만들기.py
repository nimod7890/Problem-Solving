from itertools import combinations

l,c=map(int,input().split())
vowels=['a','e','i','o','u']
alist,blist,ans=[],[],[] #자음, 모음

for v in input().rstrip().split():
  if v in vowels:
    blist.append(v)
  else:
    alist.append(v)

for i in range(2,l): # 자음 개수
  j=l-i # 모음 개수
  for li1 in combinations(alist,i):
    for li2 in combinations(blist,j):
      ans.append("".join(sorted(li1+li2)))
print(*sorted(ans),sep='\n')