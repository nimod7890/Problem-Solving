import sys
input=sys.stdin.readline

S=1<<21
for _ in range(int(input())):
  do,*num=input().split()
  if do=='add':
    S|=(1<<int(num[0]))
  if do=='remove':
    S&=~(1<<int(num[0]))
  if do=='check':
    print(1 if S&(1<<int(num[0])) else 0)
  if do=='toggle':
    S^=(1<<int(num[0]))
  if do=='all':
    S=(1<<21)-1
  if do=='empty':
    S=1<<21