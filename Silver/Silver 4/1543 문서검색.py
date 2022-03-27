from configparser import LegacyInterpolation
from dataclasses import replace


report=input()
word=input()
idx=0
cnt=0
length=len(word)
repLength=len(report)
while idx<=repLength-length:
    if report[idx:idx+length]==word:
        cnt+=1
        idx+=length
    else: 
        idx+=1
print(cnt)