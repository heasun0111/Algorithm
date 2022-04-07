def makeNumInfo(str):
    intoStr=str.split()
    num=[]
    for i in range(len(intoStr)):
        if intoStr[0]=='cpp':
            num.append(1)
        elif intoStr[0]=='java':
            num.append(2)
        elif intoStr[0]=='python':
            num.append(3)
        elif intoStr[0]=='-':
            num.append(0)

        if intoStr[1]=='backend':
            num.append(1)
        elif intoStr[1]=='frontend':
            num.append(2)
        elif intoStr[1]=='-':
            num.append(0)

        if intoStr[2]=='junior':
            num.append(1)
        elif intoStr[2]=='senior':
            num.append(2)
        elif intoStr[2]=='-':
            num.append(0)

        if intoStr[3]=='chicken':
            num.append(1)
        elif intoStr[3]=='pizza':
            num.append(2)
        elif intoStr[3]=='-':
            num.append(0)

        num.append(intoStr[4])

    return num

def makeNum(str):
    intoStr=str.split()
    num=[]
    for i in range(len(intoStr)):
        if intoStr[0]=='cpp':
            num.append(1)
        elif intoStr[0]=='java':
            num.append(2)
        elif intoStr[0]=='python':
            num.append(3)
        elif intoStr[0]=='-':
            num.append(0)

        if intoStr[2]=='backend':
            num.append(1)
        elif intoStr[2]=='frontend':
            num.append(2)
        elif intoStr[2]=='-':
            num.append(0)

        if intoStr[4]=='junior':
            num.append(1)
        elif intoStr[4]=='senior':
            num.append(2)
        elif intoStr[4]=='-':
            num.append(0)

        if intoStr[6]=='chicken':
            num.append(1)
        elif intoStr[6]=='pizza':
            num.append(2)
        elif intoStr[6]=='-':
            num.append(0)

        num.append(intoStr[7])

    return num

def solution(info, query):
    answer = []
    infoList=[]
    for i in range(len(info)):
        tmp=info[i]
        infoList.append(makeNumInfo(tmp))

    N=0
    for j in range(len(query)):
        cnt=0
        tmp2=query[j]
        queryList=makeNum(tmp2)
        tmpInfo=infoList[N]

        flag=True
        for k in range(len(queryList)-1):
            if queryList[k]==0:
                continue
            elif queryList[k]==tmpInfo[k]:
                continue
            else:
                flag=False
                break
        if queryList[-1]>tmpInfo[-1]:
            flag = False

        if flag==True:
            cnt=cnt+1
        N = N + 1
        answer.append(cnt)

    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
      ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))

# [1,1,1,1,2,4]