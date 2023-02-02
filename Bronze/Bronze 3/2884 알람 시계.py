h,m=map(int,input().split())
if m<45:
    m+=15
    h=23 if h==0 else h-1
else:
    m-=45
print(f"{h} {m}")