from collections import deque

wrd=input()
Upper=[]

for i in range(len(wrd)):
    if wrd[i].isupper()==True:
        Upper.append(wrd[i])
    else:
        continue

check=['U','C','P','C']
q=deque(check)
for j in range(len(Upper)):
    # 런타임에러(index)날 수 있어서 len(q)==0 체크!!
    if len(q)==0:
        continue

    else:
        if Upper[j] == q[0]:
            q.popleft()
        else:
            continue

if len(q)==0:
    print('I love UCPC')

else:
    print('I hate UCPC')
