n=input()
while n!="0":
    print("yes") if int(n)==int(n[::-1]) else print("no")
    n=input()