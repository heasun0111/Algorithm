def solution(s, idx):
    #brac_L=[]
    brac_idx=[]
    ans_brac=[]
    ans_match=[]
    answer=[]
    for i in range(len(s)):
        if s[i]=='{':
            #brac_L.append('{')
            brac_idx.append(i)
        elif s[i]=='}':
            #brac_L.pop()
            tmp=brac_idx.pop()
            ans_brac.append(tmp)
            ans_match.append(i)
            ans_brac.append(i)
            ans_match.append(tmp)

    for j in idx:
        for k in range(len(ans_brac)):
            if j==ans_brac[k]:
                answer.append(ans_match[k])
    return answer

#print(solution("{cpp{java}}{python}", [0, 4, 9, 10, 11, 18]))
#print(solution("ab{}cd{efg{}h}{ij}", [3, 6, 11, 3, 14, 11]))