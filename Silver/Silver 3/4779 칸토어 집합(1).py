import sys
input=sys.stdin.readline

def divide(string,line):
    if line==1: return string
    line//=3
    new=divide(string[:line],line)
    return new+" "*(line)+new

while n:=input().rstrip():
    l=3**int(n)
    print("".join(divide("-"*(l),l)))