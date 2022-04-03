def lastIdx(str):
    n=-1
    while True:
        if str[n+1:].count('/')==0:
            break
        n += str[n+1:].index('/')+1
    return n

def solution(param):
    dic={}
    answer = []
    for i in range(len(param)):
        tmp=param[i]
        num=lastIdx(tmp)
        fileN=tmp[num+1:]
        fileN_R=fileN[0]+'.'+fileN[-1]

        if fileN_R not in dic:
            dic[fileN_R]=1
        else:
            dic[fileN_R]=dic[fileN_R]+1

    for key, value in dic.items():
        if value>1:
            answer.append(key)
            answer.append(str(value))

    return answer


print(solution(["/a/a_v2.x", "/b/a.x", "/c/t.z", "/d/a/t.x", "/e/z/t_v1.z", "/k/k/k/a_v9.x"]))
print(solution(["/t.z", "/z/z_v2.z", "/a.z", "/d/b.z", "/d/a/t.z"]))
print(solution(["/t.z", "/d/b.z", "/a.z", "/e/k.z", "/d/a/x_v2.z"]))


#배열 슬라이싱 arr[n+1:]
#find, rfind함수 이용해보기!!