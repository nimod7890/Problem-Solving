import itertools
name=list(input())
n=int(input())
team=0
idx=0
teamname=[list(input()) for i in range(n)]
teamname.sort()
for i in range(n):
    namelist=[teamname[i].count(x)+name.count(x) for x in "LOVE"]
    gop=1
    for v in list(itertools.combinations(namelist,2)):
        gop*=(v[0]+v[1])
    gop%=100
    if gop>team :
        team=gop
        idx=i
print("".join(teamname[idx]))