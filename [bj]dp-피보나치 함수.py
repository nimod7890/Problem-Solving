#시간초과야 ㅜ

t=int(input())
f_list=[0 for i in range(41)]
one=[0 for i in range(41)]
zero=[0 for i in range(41)]

def f(n,i):
    if n==0: 
        zero[i]+=1
        f_list[0]=0
        return f_list[0]
    elif n==1:
        one[i]+=1
        f_list[1]=1
        return f_list[1]
    elif f_list[n]!=0:
        idx=a.index(n)
        one[i]+=one[idx]
        zero[i]+=zero[idx]
        return f_list[n]
    else: 
        return f(n-1,i)+f(n-2,i)

a=[]
for i in range(t):
    a.append(int(input()))

for i,v in enumerate(a):
    f_list[v]=f(v,i)
    print(f"{zero[a.index(v)]} {one[a.index(v)]}")



        