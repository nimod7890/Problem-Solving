from math import factorial

n=int(input())
string=str(factorial(n))[::-1]
cnt=0
for i in range(len(string)):
    if string[i]=='0':
        cnt+=1
    else: break
print(cnt)


#흠 이거 말고 다르게 푸는게 정석인듯
# 5의 개수==0의 개수 래
cnt=0
while n>=5:
	cnt += n / 5;
	n /= 5;
print(int(cnt))
#근데 베낀건디 사이트에선 답이 틀렷다 나오넹 ㅋㅋ
