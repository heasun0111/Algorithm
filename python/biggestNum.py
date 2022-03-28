def solution(numbers):
    numbersStr=[]
    for i in numbers:
        numbersStr.append(str(i))

    numbersStr.sort(reverse=True)
    answer=''.join(numbersStr)

    return answer

print(solution([3, 30, 34, 5, 9]))