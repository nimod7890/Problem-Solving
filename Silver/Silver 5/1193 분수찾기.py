n=int(input())
cnt,num=-1,1
while True:
    cnt+=1
    num+=cnt
    diff=n-num
    if num+cnt<n:
        continue
    if cnt%2==0: 
        print(f"{cnt+1-diff}/{diff+1}")
    else:
        print(f"{diff+1}/{cnt+1-diff}")
    break