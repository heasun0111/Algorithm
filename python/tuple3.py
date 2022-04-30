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
        if not(s[i]=='{' or s[i]=='}'):
            tmp.append(s[i])


    tmp="".join(tmp)
    tmp=tmp.split(",")
    tmp=list(map(int,tmp))

    answer=frequency_sort(tmp)
    return answer

# 매일 한 문제씩 풀기!!


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
