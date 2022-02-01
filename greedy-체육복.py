

#미완성

def solution(n, lost, reserve):
    answer = 0
    num=len(lost)
    for i in range(num):
        if lost[i]+1 in reserve:
            print(lost.pop(i))
            print(reserve.remove(lost[i]+1))
            answer+=1
            continue
        elif lost[i]-1 in reserve:
            print(lost.pop(i))
            print(reserve.remove(lost[i]-1))
            answer+=1
            continue
        else:
            print()

    return answer
print("answer")
print(solution(5,[2,4],[1,3,5]))
print(solution(3,[2,4],[3]))
print(solution(2,[3],[1]))
