def solution(n):
    answer = ''
    while(n>0):
        if n%2==0:
            answer=answer+'수'
        else:
            answer=answer+'박'
        n=n-1

    print(answer)

    return answer

solution(7)