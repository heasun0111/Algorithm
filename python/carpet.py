def solution(brown, yellow):
    answer = []
    for i in reversed(range(yellow+1)):
        if i*(((brown-4)/2)-i)==yellow:
            answer.append(i+2)
            tmp=int(yellow/i)
            answer.append(tmp+2)
            break
    return answer

print(solution(10,2))
print(solution(8,1))
print(solution(24,24))