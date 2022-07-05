from collections import deque

T=int(input())

for _ in range(T):
    n, m = map(int, input().split())
    printer=list(map(int, input().split()))
    q=deque(printer)

    answer=0
    num=list(range(n))
    num_q=deque(num)
    while m in num_q:
        flag=True
        for a in range(len(q)):
            if q[0]<q[a]:
                flag=False
                break

        if flag==True:
            q.popleft()
            num_q.popleft()
            answer=answer+1
        else:
            tmp_q=q[0]
            q.popleft()
            q.append(tmp_q)

            tmp_num=num_q[0]
            num_q.popleft()
            num_q.append(tmp_num)
    print(answer)




