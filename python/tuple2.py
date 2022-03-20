from collections import Counter

def frequency_sort(data):
    rt_data = []
    for i in data:
        tmp=data[i]
        for d, c in Counter(tmp).most_common():
            rt_data.append(d)
        return rt_data


def solution(s):
    s=set(s)
    l1 = list(s)
    data=[]
    for i in len(l1):
        data.append(list(l1[i]))
    answer=frequency_sort(data)
    return answer

#print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
#print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
#print(solution("{{20,111},{111}}"))
#print(solution("{{123}}"))
#print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))

a=list("{{4,2,3},{3},{2,3,4,1},{2,3}}")
result="".join(a)
print(result)

#자료형 변환
#문자열을 딱 변하는건 없고
#{ } , 등을 기준으로 split을 이용해서 하나씩 입력


