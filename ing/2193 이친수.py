# 시간 초과 시...발

n=int(input())
startNum=int('1'+'0'*(n-1),2)
endNum=int('1'+'0'*n,2)
cnt=0
for num in range(startNum,endNum):
    if '11' in str(bin(num)):cnt +=1  
print(cnt)
