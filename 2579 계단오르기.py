##시간초과나옴 ㅜ 
#dp공부를 해봅시다 .. !

n=int(input())
step=[int(input()) for i in range(n)]
answers=[]
def goUpstairs(idx,ans,num):
    global answers
    if num==3 or idx>=n: 
        return
    ans+=step[idx]
    if idx==n-1:
        answers.append(ans)
        return
    goUpstairs(idx+1,ans,num+1)
    goUpstairs(idx+2,ans,1)
goUpstairs(0,0,1)
goUpstairs(1,0,1)
print(max(answers))