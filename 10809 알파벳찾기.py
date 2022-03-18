### 내가 풀었슴

n=input()
nlist=[-1 for i in range(26)]
for i,v in enumerate(n):
    if nlist[ord(v)-ord('a')]==-1:
        nlist[ord(v)-ord('a')]=i
print(" ".join([str(x) for x in nlist]))


##더 나은 풀이

n=input()
alph=list(range(97,123))
for x in alph:
    print(n.find(chr(x)),end=" ")