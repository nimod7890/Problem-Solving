nlist=[]
for i in range(int(input())):
    a,b=input().split()
    nlist.append([int(a),i,b])
for a, i, b in sorted(nlist):
    print(f"{a} {b}")