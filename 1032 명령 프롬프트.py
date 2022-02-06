## 통과는했지만 방법 스레기임

n=int(input())
string=[[] for i in range(n)]
for i in range(n):
    string[i]=list(input())
pattern=[[] for i in range(len(string[0]))]
for value in string:
    for i,v in enumerate(value):
        pattern[i].append(v)
p=""
for value in pattern:
    if len(set(value))==1:
        p+=value[0]
    else:
        p+='?'
print(p)