# 풀이 참고
def go(num):
    if num==3:
        return ["***","* *","***"]
    nlist=[]
    star=go(num//3)
    for i in range(3):
        for v in star:
            if i==1:
                nlist.append(v+" "*(num//3)+v)            
            else:
                nlist.append(v*3)
    return nlist

print("\n".join(go(int(input()))))