#나
def solution(array, commands):
    answer=[]
    for command in commands:
        i,j,k=command
        answer.append(sorted(array[i-1:j])[k-1])
    return answer

#더 나은 방법으로 수정한다면
def solution(array, commands):
    answer=[]
    for i,j,k in commands:
        answer.append(sorted(array[i-1:j])[k-1])
    return answer

#어나더레벨 풀이 
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


#print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))