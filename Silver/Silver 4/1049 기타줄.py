n,m = map(int,input().split())
l=[list(map(int,input().split())) for i in range(m)]
setmin=sorted(l,key=lambda x:x[0])[0][0]
onemin=sorted(l,key=lambda x:x[1])[0][1]
print(min((n//6)*setmin+min((n%6)*onemin,setmin),n*onemin))