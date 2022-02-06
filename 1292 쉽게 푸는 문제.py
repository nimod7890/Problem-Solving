s,e=map(int,input().split())
string=[]
i=1
while len(string)<=e:
    string+=[i]*i
    i+=1
print(sum(string[s-1:e]))