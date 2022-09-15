for a,b in sorted([list(map(int,input().split())) for i in range(int(input()))],key=lambda x:(x[1],x[0])):
    print(f"{a} {b}")