#나 
def solution(citations):
    #citations=sorted(citations,reverse=True)
    citations.sort(reverse=True)
    max=len(citations)
    for idx in range(max):
        for i in range(citations[idx],-1,-1):
            if len(citations[:idx+1])>=i:
                if idx+1>=max:
                    return i
                if citations[idx+1]<=i:
                    return i

#더 나은 풀이 
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0


#어나더 레벨
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer


print(solution([9,9,9,12]))
print(solution([25, 8, 5, 3, 3]))
print(solution([1, 1, 5, 7, 6]))
print(solution([0,0,0,0,1]))