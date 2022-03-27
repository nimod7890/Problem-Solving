def new_num(n):
    global cnt
    if len(n)==1: n="0"+n
    hap=str(int(n[0])+int(n[1]))
    cnt+=1
    if len(hap)==1: hap="0"+hap
    return n[1]+hap[1]

n=input()
cnt=0
newnum=new_num(n)
while int(newnum)!=int(n):
    newnum=new_num(newnum)
print(cnt)