def solution(arr, brr):
    diff=[]
    for i in range(len(arr)):
        diff.append(arr[i]-brr[i])

    answer=0
    for j in range(len(diff)-1):
        if diff[j]!=0:
            diff[j + 1] = diff[j + 1] + diff[j]
            answer=answer+1

    return answer

print(solution([3, 7, 2, 4], [4, 5, 5, 2]))
print(solution([6, 2, 2, 6], [4, 4, 4, 4]))


#2번 -> 필요한 키보드와 점수를 계산하고
#조건을 만족하는 최적의 점수를 리턴