 #아스키 변환 ord chr 헷갈리지마 !!!!!!!!!!!!   
n=int(input())
string=input()
r,M=31,1234567891
ans=0
stringDic={}
for i in range(97,26+97):
    stringDic[chr(i)]=i-96
for idx,value in enumerate(string):
    ans+=stringDic[value]*(r**idx)
print(ans%M)