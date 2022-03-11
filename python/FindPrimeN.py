import itertools

def solution(numbers):
    answer=[]

    nums=[]
    for i in numbers:
        nums.append(i)

    permu_num=[]
    for j in range(len(numbers)):
        for k in itertools.permutations(nums,j+1):
            permu_num.append(int("".join(k)))

    permu_num2=list(set(permu_num))
    permu_num2.sort()

    for l in permu_num2:
        flag = True
        for m in range(l-2):
            if l%(m+2)==0:
                flag=False
                break
        if flag==True and l!=0 and l!=1:
            answer.append(l)
    return len(answer)


#반복문에서 flag위치 -> 다시 초기화 하도록
#set으로 중복 제거하고, 다시 list로 변환
#permutations이용 후 반복문으로 요소 가져올 수 있음
#반복문 범위 확인
#flag=False 이후에 break 추가하면 몇몇 케이스에서 시간초과X
#출력해야하는 거 확인(개수)
