#링크드 리스트 or deque 이용해서 다시 풀기!

def solution(n, k, cmd):
    stk=[]
    #range()함수 사용 후 list
    N=list(range(n))
    idx=k
    for i in range(len(cmd)):
        if cmd[i]=="C":
            if i<(len(N)-1):
                stk.append([idx, N[idx]])
                del N[idx]
            else:
                stk.append([idx, N[idx]])
                del N[idx]
                idx=idx-1

        elif cmd[i]=="Z":
            value=stk.pop()
            if value[0]<=idx:
                N.insert(value[0], value[1])
                idx=idx+1
            else:
                N.insert(value[0], value[1])

        else:
            tmp=cmd[i]
            A=tmp.split()
            if A[0]=="U":
                idx=idx-int(A[1])

            elif A[0]=="D":
                idx=idx+int(A[1])

    answer=[]
    ans=[]
    for k in stk:
        ans.append(k[1])

    for l in range(n):
        if l in ans:
            answer.append('X')
        else:
            answer.append('O')
    answer="".join(answer)
    return answer

print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))

#런타임 에러, 시간초과, 실패
#반례 찾기, for문 및 시간 복잡도 찾기
