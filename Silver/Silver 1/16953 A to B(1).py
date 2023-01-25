a,b=map(int,input().split())
ans=-1
def greedy(go,cnt):
    global ans
    if go==b:
        ans=cnt
        return
    if go*2<=b:
        greedy(go*2,cnt+1)
    if go*10+1<=b:
        greedy(go*10+1,cnt+1)
greedy(a,1)
print(ans)