def solution(nums):
    monSet=set(nums)
    monList=list(monSet)

    if len(monList)<(len(nums)/2):
        answer=len(monList)
    else:
        answer=int(len(nums)/2)

    return answer

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))