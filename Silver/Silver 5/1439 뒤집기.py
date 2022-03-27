## 처음에 print(num//2) 로 했는데 답 보고 깨달음 


string=list(input())
num=0
for i in range(len(string)-1):
    if string[i]!=string[i+1]:
        num+=1
print((num+1)//2)