def solution(skills, boss):
    skill_n=0
    total_n=0
    answer=[]
    skills.sort(key=lambda x:-x[0])

    for tmp in skills:
        boss=boss-tmp[0]
        tmp[1]=tmp[1]-1
        skill_n=skill_n + 1
        total_n=total_n + 1

    for tmp2 in skills:
        num=tmp2[1]
        for i in range(num):
            boss=boss-tmp2[0]
            total_n = total_n + 1
            if boss<0:
                break
        if boss<0:
            break

    if boss<0:
        answer.append(skill_n)
        answer.append(total_n)
    else:
        answer.append(-1)

    return answer

#print(solution([[50, 3], [100, 4], [200, 2], [600, 1]], 1024))
#print(solution([[100, 3], [70, 2], [200, 5]], 1000000))
#print(solution([[250, 100]], 1001))