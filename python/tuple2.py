from collections import Counter

#빈도에 따라서 정렬하는 함수
def frequency_sort(data):
    rt_data = []
    for d, c in Counter(data).most_common():
        rt_data.append(d)
    return rt_data


def solution(s):
    tmp=[]
    for i in range(len(s)):
        flag=True
        if s[i]=='{':
            flag=False
        elif s[i]=='}':
            flag=False

        if flag==True:
            tmp.append(s[i])

    tmp="".join(tmp)
    tmp=tmp.split(",")
    tmp=list(map(int,tmp))

    answer=frequency_sort(tmp)
    return answer

# 매일 한 문제씩 풀기!!
# 좀 더 간결하게 고치기

#자료형 변환
#문자열을 딱 변하는건 없고
#{ } , 등을 기준으로 split을 이용해서 하나씩 입력


