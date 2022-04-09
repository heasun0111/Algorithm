def solution(call):
    answer=''
    li=[]
    count={}
    tmp_L=call.lower()
    for i in range(len(tmp_L)):
        li.append(tmp_L[i])

    for j in li:
        try: count[j] += 1
        except: count[j] = 1

    maxN=-1
    many=[]
    for value in count.values():
        if value>maxN:
            maxN=value

    for key, value in count.items():
        if value==maxN:
            many.append(key)

    idx=[]
    for k in range(len(tmp_L)):
        for l in range(len(many)):
            if tmp_L[k]==many[l]:
                idx.append(str(k))

    for m in range(len(call)):
        if str(m) not in idx:
            answer=answer+call[m]

    return answer
