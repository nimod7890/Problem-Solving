##counter 문법 찾기만 함

from collections import Counter
d=Counter(input().upper()).most_common()
print(d[0][0]) if len(d)<2 or d[0][1]!=d[1][1] else print("?")