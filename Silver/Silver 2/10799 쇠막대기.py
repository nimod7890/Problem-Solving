nStick,currStickNum=0,0
pastString=''
for s in input():
    if s==')':
        currStickNum-=1
        if pastString=='(':
            nStick+=currStickNum
        else:
            nStick+=1
    else:
        currStickNum+=1
    pastString=s
print(nStick)