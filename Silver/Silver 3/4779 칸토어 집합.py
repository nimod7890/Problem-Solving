import sys
input=sys.stdin.readline

def divide(string):
    line=len(string)
    if line==1:
        return "-"
    for i in [0,line//3,line//3*2]:
        if i==line//3:
            string[i:i+line//3]=[" "]*(line//3)
        else:
            string[i:i+line//3]=divide(string[i:i+line//3])
    return string

while True:
    n = input().rstrip()
    if n == '': break
    print("".join(divide(["-"]*(3**int(n)))))