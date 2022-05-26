#실패 1개 및 시간초과
from _collections import deque

def solution(queue1, queue2):
    #에러나면 sum1을 long타입으로 선언
    deque1=deque(queue1)
    deque2=deque(queue2)
    sum1=sum(queue1)
    sum2=sum(queue2)
    sum_total=sum1+sum2
    cnt=len(queue1)+len(queue2)
    answer=0
    flag=False
    while cnt>0:
        if sum1==sum2:
            flag=True
            break
        else:
            if sum1>(sum_total/2):
                tmp=deque1.popleft()
                deque2.append(tmp)
                sum1=sum1-tmp
                sum2=sum2+tmp
                answer=answer+1
                cnt=cnt-1

            elif sum2>(sum_total/2):
                tmp=deque2.popleft()
                deque1.append(tmp)
                sum2 = sum2 - tmp
                sum1 = sum1 + tmp
                answer=answer+1
                cnt=cnt-1

    if flag==False:
        answer=-1

    return answer






