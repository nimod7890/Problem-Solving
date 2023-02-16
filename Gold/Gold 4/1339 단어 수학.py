from collections import defaultdict
import sys

input=sys.stdin.readline
string=defaultdict(int)
for i in range(int(input())):
    for digit,v in enumerate(input().strip()[::-1]):
        string[v]+=10**digit
ans=0
for i,v in enumerate(reversed(sorted(string.values()))):
    ans+=v*(9-i)
print(ans)