##ㅈㄴ오래걸렸지만 풀긴 풀었슴


string=input()
l=['c=','c-','dz=','d-','lj','nj','s=','z=']
sum=0
check=0
for i in range(len(string)):
    if len(string)>i+2 and string[i:i+3] in l:
        check+=1
    elif len(string)>i+1 and string[i:i+2] in l:
        sum+=1
           

print(len(string)-sum-check)