kakao=[0,0,0,0,0,0,0,0]

def cal(alp, N):
    if alp=='E':
        kakao[0]=kakao[0]+N
    elif alp=='I':
        kakao[1]=kakao[1]+N
    elif alp=='N':
        kakao[2]=kakao[2]+N
    elif alp=='S':
        kakao[3]=kakao[3]+N
    elif alp=='F':
        kakao[4]=kakao[4]+N
    elif alp=='T':
        kakao[5]=kakao[5]+N
    elif alp=='P':
        kakao[6]=kakao[6]+N
    elif alp=='J':
        kakao[7]=kakao[7]+N


def solution(survey, choices):
    answer = ''
    for i in range(len(survey)):
        tmp=survey[i]
        if choices[i]==1:
            cal(tmp[0],3)
        elif choices[i]==2:
            cal(tmp[0],2)
        elif choices[i]==3:
            cal(tmp[0],1)
        elif choices[i]==4:
            continue
        elif choices[i]==5:
            cal(tmp[1],1)
        elif choices[i]==6:
            cal(tmp[1],2)
        elif choices[i]==7:
            cal(tmp[1],3)

    if kakao[0] >= kakao[1]:
        answer=answer+'E'
    else:
        answer=answer+'I'

    if kakao[2] >= kakao[3]:
        answer=answer+'N'
    else:
        answer=answer+'S'

    if kakao[4] >= kakao[5]:
        answer=answer+'F'
    else:
        answer=answer+'T'

    if kakao[6] >= kakao[7]:
        answer=answer+'P'
    else:
        answer=answer+'J'

    return answer
