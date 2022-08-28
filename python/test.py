def solution(s):
    tmp=[]
    for i in range(len(s)-2):
        if s[i]==s[i+1] and s[i+1]==s[i+2]:
            ans=111*int(s[i])
            tmp.append(ans)

    answer=-1
    if len(tmp)==0:
        answer = -1
    else:
        answer=max(tmp)

    return answer