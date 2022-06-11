def solution(param):
    idx=1
    answer=""
    for tmp in param:
        if idx%8==0:
            answer=answer+','
            idx=idx+1

        else:
            if tmp == "BOOL":
                answer = answer+'#'
                idx = idx + 1

            elif tmp == "SHORT":
                # 8에서 쉼표 찍히는 것도 고려
                while idx%2!=0 or idx%8==0:
                    if idx%8==0:
                        answer = answer + ','
                        idx=idx+1

                    else:
                        answer = answer + '.'
                        idx=idx + 1

            elif tmp == "FLOAT":

            elif tmp == "INT":

            elif tmp == "LONG":

    return answer


print(solution(["INT", "INT", "BOOL", "SHORT", "LONG"]))
print(solution(["INT", "SHORT", "FLOAT", "INT", "BOOL"]))
print(solution(["FLOAT", "SHORT", "BOOL", "BOOL", "BOOL", "INT"]))
print(solution(["BOOL", "LONG", "SHORT", "LONG", "BOOL", "LONG", "BOOL", "LONG", "SHORT", "LONG", "LONG"]))